import json
import re
import urllib.request
from pathlib import Path

# Raw graphql with extra variant fields
API = "https://mobalytics.gg/api/poe-2/v1/graphql/query"
BUILD_ID = "8520fdce-220e-4906-a6e5-3207c709cd8f"
REFERER = "https://mobalytics.gg/poe-2/profile/bright-gun-0gguoz/builds/8520fdce-220e-4906-a6e5-3207c709cd8f"

query = """
query($input: Poe2UserGeneratedDocumentInputById!) {
  poe2 { documents { userGeneratedDocumentById(input: $input) {
    data { ... on Poe2UserGeneratedDocument { data {
      buildVariants {
        values { id }
      }
      childrenIds
    }}}
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
try:
    with urllib.request.urlopen(req, timeout=60) as resp:
        data = json.loads(resp.read().decode())
        print("graphql keys on data:", list(data.get("data", {}).keys()) if "errors" not in data else data["errors"][:1])
        if "errors" not in data:
            inner = data["data"]["poe2"]["documents"]["userGeneratedDocumentById"]["data"]["data"]
            print("childrenIds", inner.get("childrenIds"))
            print("variants", [v["id"] for v in inner["buildVariants"]["values"]])
except Exception as e:
    print("gql err", e)

# Page HTML
page = Path(r"F:\Repositories\Personal\poe2-guides\Temp\deadeye-page.html")
if page.exists():
    html = page.read_text(encoding="utf-8", errors="ignore")
    print("html size", len(html))
    for pattern in [
        r'id="react-aria[^"]*-tab-([^"]+)"[^>]*>.*?x1psj106">([^<]+)<',
        r'"variantId":"([^"]+)"[^}]*"name":"([^"]+)"',
        r'buildVariantTabs',
        r'"label":"([^"]+)"',
    ]:
        matches = re.findall(pattern, html)
        if matches:
            print("pattern", pattern[:40], matches[:8])
