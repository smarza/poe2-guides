import json
import re
import urllib.error
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

# Collect ALL fragments from main.js for complete dependency resolution
all_fragment_names = set(fragments.keys())

roots = ["Poe2UgDocumentDataFragment"]
needed = set()
queue = list(roots)

while queue:
    name = queue.pop()
    if name in needed:
        continue
    if name not in fragments:
        continue
    needed.add(name)
    for dep in re.findall(r"\.\.\.(\w+)", fragments[name]):
        if dep in all_fragment_names:
            queue.append(dep)

# Also need NgfUgDocumentFragment for document metadata - minimal query on data only
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
              ...Poe2UgDocumentDataFragment
            }
          }
        }
      }
    }
  }
}
"""

full_query = query + "\n" + "\n\n".join(fragments[n] for n in sorted(needed))
print("fragments included:", len(needed))

payload = json.dumps({
    "query": full_query,
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
            print(json.dumps(data["errors"], indent=2)[:2000])
        else:
            doc = data["data"]["poe2"]["documents"]["userGeneratedDocumentById"]["data"]
            variants = doc["data"]["buildVariants"]["values"]
            print("OK variants:", len(variants))
except urllib.error.HTTPError as e:
    print("HTTP", e.code, e.read().decode()[:2000])
