import json
import urllib.request

API = "https://mobalytics.gg/api/poe-2/v1/graphql/query"
BUILD_ID = "8520fdce-220e-4906-a6e5-3207c709cd8f"
REFERER = "https://mobalytics.gg/poe-2/profile/bright-gun-0gguoz/builds/8520fdce-220e-4906-a6e5-3207c709cd8f"

queries = [
    ("content array", """
query($input: Poe2UserGeneratedDocumentInputById!) {
  poe2 { documents { userGeneratedDocumentById(input: $input) {
    data { ... on Poe2UserGeneratedDocument {
      content { ... on NgfDocumentCmWidgetBuildPlannerV1 { data { title childrenVariants { id title } } } }
    }}
  }}}
}
"""),
    ("content list", """
query($input: Poe2UserGeneratedDocumentInputById!) {
  poe2 { documents { userGeneratedDocumentById(input: $input) {
    data { ... on Poe2UserGeneratedDocument {
      content { typename: __typename data { childrenVariants { id title } } }
    }}
  }}}
}
"""),
    ("Poe2UgDocumentFragment path", """
query($input: Poe2UserGeneratedDocumentInputById!) {
  poe2 { documents { userGeneratedDocumentById(input: $input) {
    data {
      id
      content {
        __typename
      }
    }
  }}}
}
"""),
]

headers = {
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    "Origin": "https://mobalytics.gg",
    "Referer": REFERER,
}

for label, query in queries:
    body = json.dumps({"query": query, "variables": {"input": {"id": BUILD_ID}}}).encode()
    req = urllib.request.Request(API, data=body, headers=headers, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read().decode())
            print("===", label, "===")
            if "errors" in data:
                print(data["errors"][0]["message"][:250])
            else:
                print(json.dumps(data["data"], indent=2)[:3000])
    except Exception as e:
        print(label, e)
