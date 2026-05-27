import json
import re
from pathlib import Path

html_path = Path(r"F:\Repositories\Personal\poe2-guides\deadeye.html")
json_path = Path(
    r"F:\Repositories\Personal\poe2-guides\Dev\Exports\8520fdce-220e-4906-a6e5-3207c709cd8f\8520fdce-220e-4906-a6e5-3207c709cd8f.json"
)

html = html_path.read_text(encoding="utf-8")
build_data = json.loads(json_path.read_text(encoding="utf-8"))
mini = json.dumps(build_data, ensure_ascii=False, separators=(",", ":"))

pattern = r'<script id="build-tracker-data" type="application/json">.*?</script>'
replacement = f'<script id="build-tracker-data" type="application/json">{mini}</script>'
html = re.sub(pattern, replacement, html, count=1, flags=re.DOTALL)
html_path.write_text(html, encoding="utf-8")
print("done", html_path.stat().st_size)
