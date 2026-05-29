import pathlib
import re

root = pathlib.Path(__file__).resolve().parents[2]
monk = (root / "monk.html").read_text(encoding="utf-8")
build_json = (
    root / "Dev/Exports/power-charge-martial-artist/build-data.min.json"
).read_text(encoding="utf-8")

css_match = re.search(r"<style>(.*?)</style>", monk, re.DOTALL)
tracker_js_match = re.search(
    r"\(function initBuildTracker\(\).*?\}\)\(\);", monk, re.DOTALL
)
nav_js_match = re.search(
    r"const links = Array\.from\(document\.querySelectorAll\('nav a'\)\);.*?search\.addEventListener\('input'.*?\}\);\s*",
    monk,
    re.DOTALL,
)

css = css_match.group(1)
tracker_js = tracker_js_match.group(0).replace(
    "const pageSlug = 'monk';", "const pageSlug = 'martial-artist';"
)
nav_js = nav_js_match.group(0)

body_path = root / "Dev/Scripts/martial-artist-body.html"
body = body_path.read_text(encoding="utf-8")

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Power Charge Martial Artist POE 2 — Detailed Act-by-Act Guide</title>
    <style>{css}</style>
</head>
<body>
{body}
    <script id="build-tracker-data" type="application/json">{build_json}</script>
    <script>
        {tracker_js}
    </script>
    <script>
        {nav_js}
    </script>
</body>
</html>
"""

out = root / "martial-artist.html"
out.write_text(html, encoding="utf-8")
print(f"written {out} ({out.stat().st_size} bytes)")
