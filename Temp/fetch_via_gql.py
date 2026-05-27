import json
import re
import urllib.request
from pathlib import Path

MAIN_JS = Path(r"F:\Repositories\Personal\poe2-guides\Temp\main.js")
API_URL = "https://mobalytics.gg/api/poe-2/v1/graphql/query"
BUILD_ID = "8520fdce-220e-4906-a6e5-3207c709cd8f"
REFERER = "https://mobalytics.gg/poe-2/profile/bright-gun-0gguoz/builds/8520fdce-220e-4906-a6e5-3207c709cd8f"

main = MAIN_JS.read_text(encoding="utf-8", errors="ignore")
fragments = {}
for match in re.finditer(r'body:"((?:\\n|[^"])*)"', main):
    body = match.group(1).replace("\\n", "\n")
    name_match = re.search(r"fragment\s+(\w+)", body)
    if name_match:
        fragments[name_match.group(1)] = body

needed = set()
queue = ["Poe2UgDocumentDataFragment", "NgfUgDocumentDataFragment", "NgfUgDocumentDataBuildVariantsFragment",
         "Poe2UGDocumentDataBuildVariantEquipmentV1Fragment", "Poe2UserGeneratedDocumentBuildVariantSkillGemsV1Fragment",
         "Poe2UgDocumentBuildVariantPassiveTreeV1Fragment", "Poe2DocumentUgWidgetEquipmentCommonV1Fragment",
         "Poe2DocumentUgWidgetEquipmentRuneV1Fragment", "Poe2DocumentUgWidgetEquipmentWeaponProvidedSkillFragment"]

while queue:
    name = queue.pop()
    if name in needed or name not in fragments:
        continue
    needed.add(name)
    for dep in re.findall(r"\.\.\.(\w+)", fragments[name]):
        queue.append(dep)

query_id = """
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
              ...Poe2UgDocumentDataFragment
            }
          }
        }
      }
    }
  }
}
"""

# NgfUgDocumentFragment fields - check type
query_id2 = """
query Poe2UgNormalDocumentByIdQuery($input: Poe2UserGeneratedDocumentInputById!) {
  poe2 {
    documents {
      userGeneratedDocumentById(input: $input) {
        error
        data {
          ...Poe2UgDocumentFragment
        }
      }
    }
  }
}
"""

fragment_block = "\n\n".join(fragments[name] for name in sorted(needed))
full_query = query_id2 + "\n" + fragment_block

headers = {
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0",
    "Origin": "https://mobalytics.gg",
    "Referer": REFERER,
}

body = json.dumps({
    "query": full_query,
    "variables": {"input": {"id": BUILD_ID}},
}).encode()

req = urllib.request.Request(API_URL, data=body, headers=headers, method="POST")
try:
    with urllib.request.urlopen(req, timeout=90) as resp:
        data = json.loads(resp.read().decode())
        if "errors" in data:
            print("ERRORS", json.dumps(data["errors"], indent=2)[:2000])
        else:
            doc = data["data"]["poe2"]["documents"]["userGeneratedDocumentById"]["data"]
            variants = doc["data"]["buildVariants"]["values"]
            print("OK acts/variants", len(variants))
            print("name?", doc.get("name"), doc.get("slugifiedName"))
except urllib.error.HTTPError as e:
    print("HTTP", e.code, e.read().decode()[:1500])
