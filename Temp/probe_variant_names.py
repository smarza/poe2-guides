import json
import urllib.request

API = "https://mobalytics.gg/api/poe-2/v1/graphql/query"
BUILD_ID = "8520fdce-220e-4906-a6e5-3207c709cd8f"
REFERER = "https://mobalytics.gg/poe-2/profile/bright-gun-0gguoz/builds/8520fdce-220e-4906-a6e5-3207c709cd8f"

queries = [
    ("minimal", """
query($input: Poe2UserGeneratedDocumentInputById!) {
  poe2 { documents { userGeneratedDocumentById(input: $input) {
    data { ... on Poe2UserGeneratedDocument { data {
      buildVariants { values { id name label title } }
    }}}
  }}}
}
"""),
    ("tabs", """
query($input: Poe2UserGeneratedDocumentInputById!) {
  poe2 { documents { userGeneratedDocumentById(input: $input) {
    data { ... on Poe2UserGeneratedDocument { data {
      buildVariants { values { id } tabs { id name label } }
    }}}
  }}}
}
"""),
    ("ngf variants", """
query($input: Poe2UserGeneratedDocumentInputById!) {
  poe2 { documents { userGeneratedDocumentById(input: $input) {
    data { ... on Poe2UserGeneratedDocument { data {
      buildVariants { values { id } }
    }}}
  }}}
}
"""),
]

for label, query in queries:
    body = json.dumps({"query": query, "variables": {"input": {"id": BUILD_ID}}}).encode()
    req = urllib.request.Request(API, data=body, headers={
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0",
        "Origin": "https://mobalytics.gg",
        "Referer": REFERER,
    }, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            data = json.loads(resp.read().decode())
            print("===", label, "===")
            if "errors" in data:
                print(json.dumps(data["errors"][:2], indent=2))
            else:
                inner = data["data"]["poe2"]["documents"]["userGeneratedDocumentById"]["data"]["data"]
                print(json.dumps(inner.get("buildVariants"), indent=2)[:2000])
    except Exception as e:
        print(label, e)
