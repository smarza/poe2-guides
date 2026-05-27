import re
from pathlib import Path

main = Path(r"F:\Repositories\Personal\poe2-guides\Temp\main.js").read_text(encoding="utf-8", errors="ignore")
fragments = {}

for match in re.finditer(r'body:"((?:\\n|[^"])*)"', main):
    body = match.group(1).replace("\\n", "\n")
    name_match = re.search(r"fragment\s+(\w+)", body)
    if name_match:
        fragments[name_match.group(1)] = body

roots = ["Poe2UgDocumentFragment", "NgfUgDocumentFragment", "Poe2UgDocumentDataFragment"]
needed = set()
queue = list(roots)

while queue:
    name = queue.pop()
    if name in needed or name not in fragments:
        continue
    needed.add(name)
    for dep in re.findall(r"\.\.\.(\w+)", fragments[name]):
        queue.append(dep)

# also add query fragments
for body in fragments.values():
    if "userGeneratedDocumentById" in body and "query" in body:
        print("QUERY ID FOUND")
    if "userGeneratedDocumentBySlugifiedName" in body and "query" in body:
        print("QUERY SLUG FOUND")

print("fragments needed:", len(needed))
for n in sorted(needed):
    if "Poe2" in n or "NgfUg" in n or "BuildVariant" in n or "Equipment" in n or "SkillGem" in n or "Passive" in n:
        print(" ", n)

missing = []
for name in needed:
    if name not in fragments:
        missing.append(name)
print("missing:", missing[:20], "count", len(missing))
