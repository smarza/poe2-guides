import json
import re
import urllib.request

main = open(r"F:\Repositories\Personal\poe2-guides\Temp\main.js", encoding="utf-8", errors="ignore").read()
bodies = [b.replace("\\n", "\n") for b in re.findall(r'body:"((?:\\n|[^"])*)"', main)]

for body in bodies:
    if "userGeneratedDocumentById" in body or "userGeneratedDocumentBySlugifiedName" in body:
        name = re.search(r"(query|fragment)\s+(\w+)", body)
        print("===", name.group(0) if name else "?", "===")
        print(body[:2500])
        print()

# Test API - minimal query first
queries_to_try = [
    (
        "by-id-minimal",
        """
        query($input: NgfUserGeneratedDocumentInputById!) {
          poe2 {
            documents {
              userGeneratedDocumentById(input: $input) {
                error
                data { id name slugifiedName }
              }
            }
          }
        }
        """,
        {"input": {"id": "8520fdce-220e-4906-a6e5-3207c709cd8f"}},
    ),
    (
        "by-slug-minimal",
        """
        query($input: NgfUserGeneratedDocumentInputBySlugifiedName!) {
          poe2 {
            documents {
              userGeneratedDocumentBySlugifiedName(input: $input) {
                error
                data { id name slugifiedName }
              }
            }
          }
        }
        """,
        {
            "input": {
                "authorProfileName": "bright-gun-0gguoz",
                "slugifiedName": "8520fdce-220e-4906-a6e5-3207c709cd8f",
            }
        },
    ),
]

headers = {
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0",
    "Origin": "https://mobalytics.gg",
    "Referer": "https://mobalytics.gg/poe-2/profile/bright-gun-0gguoz/builds/8520fdce-220e-4906-a6e5-3207c709cd8f",
}

for label, query, variables in queries_to_try:
    body = json.dumps({"query": query, "variables": variables}).encode()
    req = urllib.request.Request(
        "https://mobalytics.gg/api/poe-2/v1/graphql/query",
        data=body,
        headers=headers,
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            data = json.loads(resp.read().decode())
            print(label, "OK", json.dumps(data)[:500])
    except Exception as e:
        print(label, "ERR", e)
