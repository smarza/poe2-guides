import json
import urllib.error
import urllib.request
from pathlib import Path

API_URL = "https://mobalytics.gg/api/poe-2/v1/graphql/query"
BUILD_ID = "8520fdce-220e-4906-a6e5-3207c709cd8f"
REFERER = "https://mobalytics.gg/poe-2/profile/bright-gun-0gguoz/builds/8520fdce-220e-4906-a6e5-3207c709cd8f"

fragments_path = Path(r"F:\Repositories\Personal\poe2-guides\Dev\Scripts\MobalyticsBuildGraphqlFragments.graphql")
base_fragments = fragments_path.read_text(encoding="utf-8")

manual_fragments = """
fragment Poe2DocumentUgWidgetEquipmentCommonV1Fragment on Poe2DocumentUgWidgetEquipmentCommonV1 {
  slug
  name
  explicitDescriptions {
    description
  }
  implicitDescriptions {
    description
  }
}

fragment Poe2DocumentUgWidgetEquipmentRuneV1Fragment on Poe2DocumentUgWidgetEquipmentRuneV1 {
  slug
  name
}

fragment Poe2DocumentUgWidgetEquipmentWeaponProvidedSkillFragment on Poe2DocumentUgWidgetEquipmentWeaponProvidedSkill {
  slug
  name
}
"""

query = """
query Poe2UgNormalDocumentByIdQuery($input: Poe2UserGeneratedDocumentInputById!) {
  poe2 {
    documents {
      userGeneratedDocumentById(input: $input) {
        error
        data {
          id
          slugifiedName
          ... on Poe2UserGeneratedDocument {
            data {
              name
              buildVariants {
                values {
                  id
                  equipment {
                    priorityList {
                      type
                      slug
                      name
                    }
                    helmet {
                      commonItem {
                        slug
                        name
                        explicitDescriptions { description }
                        implicitDescriptions { description }
                      }
                    }
                  }
                  skillGems {
                    gems {
                      activeSkill { name gemSlug level }
                      subSkills { gemSlug }
                    }
                  }
                  passiveTree {
                    mainTree {
                      priorityList { slug name }
                    }
                  }
                }
              }
            }
          }
        }
      }
    }
  }
}
"""

payload = json.dumps({
    "query": query,
    "variables": {"input": {"id": BUILD_ID}},
}).encode("utf-8")

req = urllib.request.Request(
    API_URL,
    data=payload,
    headers={
        "Content-Type": "application/json",
        "Accept": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "Origin": "https://mobalytics.gg",
        "Referer": REFERER,
    },
    method="POST",
)

try:
    with urllib.request.urlopen(req, timeout=120) as resp:
        data = json.loads(resp.read().decode())
        if "errors" in data:
            print(json.dumps(data["errors"], indent=2)[:3000])
        else:
            doc = data["data"]["poe2"]["documents"]["userGeneratedDocumentById"]["data"]
            variants = doc["data"]["buildVariants"]["values"]
            print("OK name:", doc["data"].get("name"))
            print("variants:", len(variants))
            if variants:
                eq = variants[0].get("equipment") or {}
                print("priority", len(eq.get("priorityList") or []))
except urllib.error.HTTPError as e:
    print("HTTP", e.code, e.read().decode()[:3000])
