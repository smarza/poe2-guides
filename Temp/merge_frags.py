import re
from pathlib import Path

files = [
    Path(r"F:\Repositories\Personal\poe2-guides\Temp\main.js"),
    Path(r"F:\Repositories\Personal\poe2-guides\Temp\8626.js"),
    Path(r"F:\Repositories\Personal\poe2-guides\Temp\poe-2-app.js"),
]

fragments = {}
for path in files:
    if not path.exists():
        print("missing", path)
        continue
    content = path.read_text(encoding="utf-8", errors="ignore")
    for match in re.finditer(r'body:"((?:\\n|[^"])*)"', content):
        body = match.group(1).replace("\\n", "\n")
        name_match = re.search(r"fragment\s+(\w+)", body)
        if name_match:
            fragments[name_match.group(1)] = body

print("total fragments", len(fragments))
for name in sorted(fragments):
    if "EquipmentCommon" in name or "EquipmentRune" in name or "WeaponProvided" in name:
        print(" ", name)
