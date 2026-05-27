#!/usr/bin/env python3
"""Fetch Mobalytics PoE 2 build data via GraphQL when SSR HTML has no embedded buildVariants."""

from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.error
import urllib.request

API_URL = "https://mobalytics.gg/api/poe-2/v1/graphql/query"
UUID_PATTERN = re.compile(
    r"^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$",
    re.IGNORECASE,
)

COMMON_ITEM_FIELDS = """
  slug
  name
  explicitDescriptions {
    description
  }
  implicitDescriptions {
    description
  }
"""

WEAPON_SET_FIELDS = f"""
set1 {{
  commonItem {{
    {COMMON_ITEM_FIELDS}
  }}
}}
set2 {{
  commonItem {{
    {COMMON_ITEM_FIELDS}
  }}
}}
"""

EQUIPMENT_FIELDS = f"""
priorityList {{
  type
  slug
  name
}}
amulet {{
  commonItem {{
    {COMMON_ITEM_FIELDS}
  }}
}}
belt {{
  commonItem {{
    {COMMON_ITEM_FIELDS}
  }}
}}
body {{
  commonItem {{
    {COMMON_ITEM_FIELDS}
  }}
}}
boots {{
  commonItem {{
    {COMMON_ITEM_FIELDS}
  }}
}}
flask1 {{
  commonItem {{
    {COMMON_ITEM_FIELDS}
  }}
}}
flask2 {{
  commonItem {{
    {COMMON_ITEM_FIELDS}
  }}
}}
charm1 {{
  commonItem {{
    {COMMON_ITEM_FIELDS}
  }}
}}
charm2 {{
  commonItem {{
    {COMMON_ITEM_FIELDS}
  }}
}}
charm3 {{
  commonItem {{
    {COMMON_ITEM_FIELDS}
  }}
}}
gloves {{
  commonItem {{
    {COMMON_ITEM_FIELDS}
  }}
}}
helmet {{
  commonItem {{
    {COMMON_ITEM_FIELDS}
  }}
}}
leftRing {{
  commonItem {{
    {COMMON_ITEM_FIELDS}
  }}
}}
extraRing {{
  commonItem {{
    {COMMON_ITEM_FIELDS}
  }}
}}
rightRing {{
  commonItem {{
    {COMMON_ITEM_FIELDS}
  }}
}}
mainHand {{
  {WEAPON_SET_FIELDS}
}}
offHand {{
  {WEAPON_SET_FIELDS}
}}
"""

BUILD_VARIANT_FIELDS = f"""
id
equipment {{
  {EQUIPMENT_FIELDS}
}}
skillGems {{
  gems {{
    activeSkill {{
      name
      gemSlug
      level
    }}
    subSkills {{
      gemSlug
    }}
  }}
  priorityGems {{
    gemSlug
    name
  }}
}}
passiveTree {{
  mainTree {{
    priorityList {{
      slug
      name
    }}
  }}
  ascendancyTree {{
    priorityList {{
      slug
      name
    }}
  }}
}}
"""

CONTENT_VARIANTS_FIELDS = """
content {
  ... on NgfDocumentCmWidgetContentVariantsV1 {
    data {
      childrenVariants {
        id
        title
      }
    }
  }
}
"""

QUERY_BY_ID = f"""
query Poe2UgNormalDocumentByIdQuery($input: Poe2UserGeneratedDocumentInputById!) {{
  poe2 {{
    documents {{
      userGeneratedDocumentById(input: $input) {{
        error
        data {{
          id
          slugifiedName
          ... on Poe2UserGeneratedDocument {{
            {CONTENT_VARIANTS_FIELDS}
            data {{
              name
              buildVariants {{
                values {{
                  {BUILD_VARIANT_FIELDS}
                }}
              }}
            }}
          }}
        }}
      }}
    }}
  }}
}}
"""

QUERY_BY_SLUG = f"""
query Poe2UgNormalDocumentBySlugQuery($input: NgfUserGeneratedDocumentInputBySlugifiedName!) {{
  poe2 {{
    documents {{
      userGeneratedDocumentBySlugifiedName(input: $input) {{
        error
        data {{
          id
          slugifiedName
          ... on Poe2UserGeneratedDocument {{
            {CONTENT_VARIANTS_FIELDS}
            data {{
              name
              buildVariants {{
                values {{
                  {BUILD_VARIANT_FIELDS}
                }}
              }}
            }}
          }}
        }}
      }}
    }}
  }}
}}
"""


def extract_variant_labels_by_id(document_data: dict) -> dict[str, str]:
    labels: dict[str, str] = {}

    for content_item in document_data.get("content") or []:
        if not content_item:
            continue

        widget_data = content_item.get("data") or {}

        for child_variant in widget_data.get("childrenVariants") or []:
            variant_id = child_variant.get("id")
            variant_title = child_variant.get("title")

            if not variant_id or not variant_title:
                continue

            labels[variant_id] = str(variant_title).strip()

    return labels


def build_request_payload(
    *,
    build_id: str | None,
    author: str,
    slug: str,
) -> tuple[str, dict]:
    if build_id:
        return QUERY_BY_ID, {"input": {"id": build_id}}

    return QUERY_BY_SLUG, {
        "input": {
            "authorProfileName": author,
            "slugifiedName": slug,
        }
    }


def fetch_build_data(
    *,
    build_id: str | None,
    author: str,
    slug: str,
    referer: str,
) -> dict:
    query, variables = build_request_payload(build_id=build_id, author=author, slug=slug)
    payload = json.dumps({"query": query, "variables": variables}).encode("utf-8")

    request = urllib.request.Request(
        API_URL,
        data=payload,
        headers={
            "Content-Type": "application/json",
            "Accept": "application/json",
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
            ),
            "Origin": "https://mobalytics.gg",
            "Referer": referer,
        },
        method="POST",
    )

    try:
        with urllib.request.urlopen(request, timeout=120) as response:
            response_body = json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as error:
        error_text = error.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"GraphQL HTTP {error.code}: {error_text[:500]}") from error

    if "errors" in response_body:
        messages = "; ".join(
            error.get("message", str(error)) for error in response_body["errors"]
        )
        raise RuntimeError(f"GraphQL errors: {messages}")

    documents = response_body["data"]["poe2"]["documents"]
    document_result = (
        documents["userGeneratedDocumentById"]
        if build_id
        else documents["userGeneratedDocumentBySlugifiedName"]
    )

    if document_result.get("error"):
        raise RuntimeError(f"API error: {document_result['error']}")

    document_data = document_result.get("data")
    if not document_data:
        raise RuntimeError("Build nao encontrado (documento vazio).")

    inner_data = document_data.get("data") or {}
    build_variants = inner_data.get("buildVariants")

    if not build_variants or not build_variants.get("values"):
        raise RuntimeError("buildVariants nao encontrados na resposta GraphQL.")

    variant_labels_by_id = extract_variant_labels_by_id(document_data)

    return {
        "buildName": inner_data.get("name") or "Mobalytics Build",
        "slugifiedName": document_data.get("slugifiedName") or slug,
        "documentId": document_data.get("id"),
        "buildVariants": build_variants,
        "variantLabelsById": variant_labels_by_id,
    }


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--author", required=True, help="Mobalytics profile slug")
    parser.add_argument("--referer", required=True, help="Full build page URL")
    parser.add_argument("--slug", help="Build slugified name")
    parser.add_argument("--build-id", help="Build UUID (profile/.../builds/{uuid})")
    return parser.parse_args()


def main() -> int:
    arguments = parse_arguments()
    slug = arguments.slug or arguments.build_id or ""
    build_id = arguments.build_id

    if build_id and not UUID_PATTERN.match(build_id):
        build_id = None

    if not build_id and not arguments.slug:
        print("Informe --build-id ou --slug.", file=sys.stderr)
        return 1

    try:
        result = fetch_build_data(
            build_id=build_id,
            author=arguments.author,
            slug=arguments.slug or slug,
            referer=arguments.referer,
        )
    except RuntimeError as error:
        print(str(error), file=sys.stderr)
        return 1

    json.dump(result, sys.stdout, ensure_ascii=False)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
