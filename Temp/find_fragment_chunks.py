import re
import urllib.request
from pathlib import Path

HTML = Path(r"F:\Repositories\Personal\poe2-guides\Temp\bright-gun-build.html").read_text(encoding="utf-8")
TARGET = "Poe2DocumentUgWidgetEquipmentCommonV1Fragment"

chunk_urls = sorted(set(re.findall(r'href="(/static/js/[^"]+\.js)"', HTML)))
print("chunks", len(chunk_urls))

for url in chunk_urls:
    full = "https://mobalytics.gg" + url
    name = url.split("/")[-1]
    local = Path(r"F:\Repositories\Personal\poe2-guides\Temp\chunks") / name
    local.parent.mkdir(parents=True, exist_ok=True)
    if not local.exists() or local.stat().st_size < 100:
        req = urllib.request.Request(full, headers={"User-Agent": "Mozilla/5.0"})
        try:
            with urllib.request.urlopen(req, timeout=60) as resp:
                local.write_bytes(resp.read())
        except Exception as exc:
            print("fail", name, exc)
            continue
    content = local.read_text(encoding="utf-8", errors="ignore")
    if TARGET in content:
        print("FOUND in", name)
        for match in re.finditer(r'body:"((?:\\n|[^"])*)"', content):
            body = match.group(1).replace("\\n", "\n")
            if f"fragment {TARGET}" in body:
                print(body[:1200])
                break
