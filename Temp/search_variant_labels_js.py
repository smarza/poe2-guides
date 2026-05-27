import re
from pathlib import Path

chunks = Path(r"F:\Repositories\Personal\poe2-guides\Temp\chunks")
terms = ["variantLabel", "variantName", "buildVariant", "default-variant", "Act 1", "tabLabel", "VARIANT_"]

for path in chunks.glob("*.js"):
    text = path.read_text(encoding="utf-8", errors="ignore")
    for term in terms:
        if term in text:
            idx = text.find(term)
            print(path.name, term, repr(text[max(0, idx - 60) : idx + 120])[:200])
