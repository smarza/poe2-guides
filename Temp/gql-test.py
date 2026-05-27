import json
import urllib.request

query = """
query Poe2UgNormalDocumentByIdQuery($input: Poe2UserGeneratedDocumentInputById!) {
  poe2 {
    documents {
      userGeneratedDocumentById(input: $input) {
        error
        data {
          id
        }
      }
    }
  }
}
"""

payload = json.dumps({
    "query": query,
    "variables": {"input": {"id": "8520fdce-220e-4906-a6e5-3207c709cd8f"}},
}).encode("utf-8")

req = urllib.request.Request(
    "https://mobalytics.gg/api/poe-2/v1/graphql/query",
    data=payload,
    headers={
        "Content-Type": "application/json",
        "Accept": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
        "Origin": "https://mobalytics.gg",
        "Referer": "https://mobalytics.gg/poe-2/profile/bright-gun-0gguoz/builds/8520fdce-220e-4906-a6e5-3207c709cd8f",
    },
    method="POST",
)

with urllib.request.urlopen(req, timeout=60) as resp:
    print(resp.read().decode()[:1000])
