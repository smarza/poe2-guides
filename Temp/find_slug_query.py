import re
from pathlib import Path

main = Path(r"F:\Repositories\Personal\poe2-guides\Temp\chunks\main.87e55fa0.js").read_text(encoding="utf-8", errors="ignore")
for match in re.finditer(r'body:"((?:\\n|[^"])*)"', main):
    body = match.group(1).replace("\\n", "\n")
    if "userGeneratedDocumentBySlugifiedName" in body and "query" in body:
        print(body[:2000])
        print("---")
