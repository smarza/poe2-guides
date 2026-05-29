import json, pathlib, re
root = pathlib.Path(r"F:/Repositories/Personal/poe2-guides")
html = (root/"martial-artist.html").read_text(encoding="utf-8")
m = re.search(r'<script id="build-tracker-data" type="application/json">(.*?)</script>', html, re.DOTALL)
data = json.loads(m.group(1))
for act in data["acts"]:
    eq = len(act["equipment"])
    mods = sum(len(e.get("modifiers",[])) for e in act["equipment"])
    gems = len(act["skillGems"])
    sups = sum(len(g.get("supports",[])) for g in act["skillGems"])
    pas = len(act["passiveTree"])
    total = eq + mods + gems + sups + pas
    print(act["act"], "total", total, "| equip", eq, "+", mods, "| gems", gems, "+", sups, "| passives", pas)
