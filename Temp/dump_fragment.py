import re
from pathlib import Path

main = Path(r"F:\Repositories\Personal\poe2-guides\Temp\main.js").read_text(encoding="utf-8", errors="ignore")
names = [
    "Poe2UGDocumentDataBuildVariantEquipmentV1Fragment",
    "Poe2UgDocumentBuildVariantEquipmentV1Fragment",
    "Poe2DocumentUgWidgetEquipmentCommonV1Fragment",
]

for match in re.finditer(r'body:"((?:\\n|[^"])*)"', main):
    body = match.group(1).replace("\\n", "\n")
    for name in names:
        if f"fragment {name}" in body:
            print("===", name, "===")
            print(body[:2500])
            print()
