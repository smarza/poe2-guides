import re
from pathlib import Path

chunks_dir = Path(r"F:\Repositories\Personal\poe2-guides\Temp\chunks")
fragments = {}

for path in sorted(chunks_dir.glob("*.js")):
    content = path.read_text(encoding="utf-8", errors="ignore")
    for match in re.finditer(r'body:"((?:\\n|[^"])*)"', content):
        body = match.group(1).replace("\\n", "\n")
        name_match = re.search(r"fragment\s+(\w+)", body)
        if name_match:
            fragments[name_match.group(1)] = body

print("total", len(fragments))
for name in ["Poe2DocumentUgWidgetEquipmentCommonV1Fragment", "Poe2UgDocumentDataFragment", "Poe2UgDocumentFragment"]:
    print(name, "->", "yes" if name in fragments else "NO")

out = Path(r"F:\Repositories\Personal\poe2-guides\Dev\Scripts\MobalyticsBuildGraphqlFragments.graphql")
roots = ["Poe2UgDocumentDataFragment"]
needed = set()
queue = list(roots)

while queue:
    name = queue.pop()
    if name in needed or name not in fragments:
        continue
    needed.add(name)
    for dep in re.findall(r"\.\.\.(\w+)", fragments[name]):
        queue.append(dep)

# Also need document wrapper fragments for by-id query
for extra in ["Poe2UgDocumentFragment", "NgfUgDocumentFragment"]:
    if extra in fragments:
        queue.append(extra)

needed2 = set()
queue = list(needed) + ["Poe2UgDocumentFragment"]
while queue:
    name = queue.pop()
    if name in needed2 or name not in fragments:
        continue
    needed2.add(name)
    for dep in re.findall(r"\.\.\.(\w+)", fragments[name]):
        queue.append(dep)

combined = "\n\n".join(fragments[n] for n in sorted(needed2))
out.write_text(combined + "\n", encoding="utf-8")
print("written", out, "fragments", len(needed2))
