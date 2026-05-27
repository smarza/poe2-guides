import json
import urllib.request

API = "https://mobalytics.gg/api/poe-2/v1/graphql/query"
BUILD_ID = "8520fdce-220e-4906-a6e5-3207c709cd8f"
REFERER = "https://mobalytics.gg/poe-2/profile/bright-gun-0gguoz/builds/8520fdce-220e-4906-a6e5-3207c709cd8f"

fields_to_try = [
    "name",
    "label",
    "title",
    "displayName",
    "slug",
    "tabName",
    "variantName",
]

for field in fields_to_try:
    query = f"""
    query($input: Poe2UserGeneratedDocumentInputById!) {{
      poe2 {{ documents {{ userGeneratedDocumentById(input: $input) {{
        data {{ ... on Poe2UserGeneratedDocument {{ data {{
          buildVariants {{ values {{ id {field} }} }}
        }}}}
      }}}}}}
    }}
    """
    body = json.dumps({"query": query, "variables": {"input": {"id": BUILD_ID}}}).encode()
    req = urllib.request.Request(API, data=body, headers={
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "Origin": "https://mobalytics.gg",
        "Referer": REFERER,
    }, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read().decode())
            if "errors" in data:
                print(field, "ERR", data["errors"][0]["message"][:80])
            else:
                vals = data["data"]["poe2"]["documents"]["userGeneratedDocumentById"]["data"]["data"]["buildVariants"]["values"]
                print(field, "OK", vals)
    except Exception as e:
        print(field, e)

# document widgets / type data
query2 = """
query($input: Poe2UserGeneratedDocumentInputById!) {
  poe2 { documents { userGeneratedDocumentById(input: $input) {
    data {
      typeData { slug displayMetadata { name } }
      ... on Poe2UserGeneratedDocument {
        data {
          name
          childrenIds
          buildVariants { values { id genericBuilder { slots { gameSlotSlug } } } }
        }
      }
    }
  }}}
}
"""
body = json.dumps({"query": query2, "variables": {"input": {"id": BUILD_ID}}}).encode()
req = urllib.request.Request(API, data=body, headers={
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    "Origin": "https://mobalytics.gg",
    "Referer": REFERER,
}, method="POST")
with urllib.request.urlopen(req, timeout=30) as resp:
    data = json.loads(resp.read().decode())
    if "errors" in data:
        print("type", data["errors"][0]["message"][:120])
    else:
        doc = data["data"]["poe2"]["documents"]["userGeneratedDocumentById"]["data"]
        print("typeData", doc.get("typeData"))
        print("inner", json.dumps(doc.get("data"), indent=2)[:1500])
