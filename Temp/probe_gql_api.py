import json
import urllib.error
import urllib.request

headers = {
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    "Origin": "https://mobalytics.gg",
    "Referer": "https://mobalytics.gg/poe-2/profile/bright-gun-0gguoz/builds/8520fdce-220e-4906-a6e5-3207c709cd8f",
}

query = """
query($input: Poe2UserGeneratedDocumentInputById!) {
  poe2 {
    documents {
      userGeneratedDocumentById(input: $input) {
        error
        data {
          id
          name
          slugifiedName
          data {
            buildVariants {
              values { id }
            }
          }
        }
      }
    }
  }
}
"""

body = json.dumps({
    "query": query,
    "variables": {"input": {"id": "8520fdce-220e-4906-a6e5-3207c709cd8f"}},
}).encode()

req = urllib.request.Request(
    "https://mobalytics.gg/api/poe-2/v1/graphql/query",
    data=body,
    headers=headers,
    method="POST",
)
try:
    with urllib.request.urlopen(req, timeout=60) as resp:
        print(resp.read().decode()[:2000])
except urllib.error.HTTPError as e:
    print("status", e.code)
    print(e.read().decode()[:2000])
