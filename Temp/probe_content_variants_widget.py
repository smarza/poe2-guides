import json
import urllib.request

API = "https://mobalytics.gg/api/poe-2/v1/graphql/query"
BUILD_ID = "8520fdce-220e-4906-a6e5-3207c709cd8f"
REFERER = "https://mobalytics.gg/poe-2/profile/bright-gun-0gguoz/builds/8520fdce-220e-4906-a6e5-3207c709cd8f"

query = """
query($input: Poe2UserGeneratedDocumentInputById!) {
  poe2 { documents { userGeneratedDocumentById(input: $input) {
    data { ... on Poe2UserGeneratedDocument {
      content {
        ... on NgfDocumentCmWidgetContentVariantsV1 {
          data {
            title
            childrenVariants {
              id
              title
            }
          }
        }
      }
    }}
  }}}
}
"""

body = json.dumps({"query": query, "variables": {"input": {"id": BUILD_ID}}}).encode()
req = urllib.request.Request(API, data=body, headers={
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    "Origin": "https://mobalytics.gg",
    "Referer": REFERER,
}, method="POST")
with urllib.request.urlopen(req, timeout=30) as resp:
    data = json.loads(resp.read().decode())
    if "errors" in data:
        print("ERR", json.dumps(data["errors"], indent=2))
    else:
        content = data["data"]["poe2"]["documents"]["userGeneratedDocumentById"]["data"]["content"]
        for item in content:
            if item and item.get("data") and item["data"].get("childrenVariants"):
                print(json.dumps(item["data"], indent=2))
