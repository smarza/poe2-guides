from pathlib import Path

HELPERS = """
            function getActStorageKey(act) {
                if (act.variantId) {
                    return act.variantId;
                }

                return act.act;
            }

            function findActByStorageKey(storageKey) {
                return buildData.acts.find(entry => getActStorageKey(entry) === storageKey);
            }

            function getActDisplayLabel(storageKey) {
                const act = findActByStorageKey(storageKey);

                if (act) {
                    return act.act;
                }

                return storageKey;
            }
"""

REPLACEMENTS = [
    ("            function getChildId(prefix, index) {\n                return `${prefix}-${index}`;\n            }\n\n            function loadTrackerState()",
     "            function getChildId(prefix, index) {\n                return `${prefix}-${index}`;\n            }\n" + HELPERS + "\n            function loadTrackerState()"),
    ("let activeAct = buildData.acts[0]?.act || 'Act 1';", "let activeActKey = buildData.acts[0] ? getActStorageKey(buildData.acts[0]) : 'act-1';"),
    ("                    state.equipment[act.act] = {};\n                    state.skillGems[act.act] = {};\n                    state.passiveTree[act.act] = {};",
     "                    const actKey = getActStorageKey(act);\n                    state.equipment[actKey] = {};\n                    state.skillGems[actKey] = {};\n                    state.passiveTree[actKey] = {};"),
    ("                        const actLabel = act.act;\n                        const savedAct = saved?.[category.key]?.[actLabel] || {};\n\n                        state[category.key][actLabel] = { ...savedAct };",
     "                        const actKey = getActStorageKey(act);\n                        const savedAct = saved?.[category.key]?.[actKey] || {};\n\n                        state[category.key][actKey] = { ...savedAct };"),
    ("            function countProgress(actLabel, category) {\n                const act = buildData.acts.find(entry => entry.act === actLabel);",
     "            function countProgress(actKey, category) {\n                const act = findActByStorageKey(actKey);"),
    ("                    const itemState = trackerState[category.key][actLabel][itemId] || { self: false, children: {} };",
     "                    const itemState = trackerState[category.key][actKey][itemId] || { self: false, children: {} };"),
    ("                    const equipmentProgress = countProgress(act.act, categories[0]);\n                    const gemsProgress = countProgress(act.act, categories[1]);\n                    const passivesProgress = countProgress(act.act, categories[2]);",
     "                    const actKey = getActStorageKey(act);\n                    const equipmentProgress = countProgress(actKey, categories[0]);\n                    const gemsProgress = countProgress(actKey, categories[1]);\n                    const passivesProgress = countProgress(actKey, categories[2]);"),
    ("                    const isActive = act.act === activeAct;",
     "                    const isActive = actKey === activeActKey;"),
    ("                        activeAct = act.act;",
     "                        activeActKey = actKey;"),
    ("                    const progress = countProgress(activeAct, category);",
     "                    const progress = countProgress(activeActKey, category);"),
    ("                const act = buildData.acts.find(entry => entry.act === activeAct);",
     "                const act = findActByStorageKey(activeActKey);"),
    ("                        const itemState = ensureItemState(category.key, activeAct, itemId);",
     "                        const itemState = ensureItemState(category.key, activeActKey, itemId);"),
    ("                const confirmed = confirm(`Reset all checklist progress for ${activeAct}?`);",
     "                const confirmed = confirm(`Reset all checklist progress for ${getActDisplayLabel(activeActKey)}?`);"),
    ("                    resetAct(activeAct);",
     "                    resetAct(activeActKey);"),
]

for path in [
    Path(r"F:\Repositories\Personal\poe2-guides\monk.html"),
    Path(r"F:\Repositories\Personal\poe2-guides\deadeye.html"),
]:
    text = path.read_text(encoding="utf-8")
    for old, new in REPLACEMENTS:
        if old not in text:
            raise SystemExit(f"Missing pattern in {path.name}: {old[:60]}...")
        text = text.replace(old, new)
    path.write_text(text, encoding="utf-8")
    print("patched", path.name)
