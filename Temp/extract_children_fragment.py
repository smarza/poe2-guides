import re
from pathlib import Path

main = Path(r"F:\Repositories\Personal\poe2-guides\Temp\chunks\main.87e55fa0.js").read_text(encoding="utf-8", errors="ignore")
for match in re.finditer(r'body:"((?:\\n|[^"])*)"', main):
    body = match.group(1).replace("\\n", "\n")
    if "childrenVariants" in body and "title" in body and "fragment" in body:
        print(body[:5000])
        print("---\n")
