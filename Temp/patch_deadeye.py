from pathlib import Path

html_path = Path(r"F:\Repositories\Personal\poe2-guides\deadeye.html")
json_path = Path(r"F:\Repositories\Personal\poe2-guides\Dev\Exports\8520fdce-220e-4906-a6e5-3207c709cd8f\8520fdce-220e-4906-a6e5-3207c709cd8f.json")
monk_path = Path(r"F:\Repositories\Personal\poe2-guides\monk.html")

html = html_path.read_text(encoding="utf-8")
build_json = json_path.read_text(encoding="utf-8").strip()
monk = monk_path.read_text(encoding="utf-8")

tracker_css_start = monk.index("        .tracker-toolbar {")
tracker_css_end = monk.index("        .violet .section-kicker, .violet .timeline-title {")
tracker_css = monk[tracker_css_start:tracker_css_end]

resource_css_start = monk.index("        .resource-links {")
resource_css_end = monk.index("        .two-col {", resource_css_start)
resource_css = monk[resource_css_start:resource_css_end]

tracker_js_start = monk.index("        (function initBuildTracker() {")
tracker_js_end = monk.index("        })();", tracker_js_start) + len("        })();")
tracker_js = monk[tracker_js_start:tracker_js_end].replace("const pageSlug = 'monk';", "const pageSlug = 'deadeye';")
tracker_js = tracker_js.replace("accent-color: var(--lightning);", "accent-color: var(--ice);")

build_tracker_section = """
            <section id="build-tracker" class="section">
                <div class="section-head">
                    <div class="section-kicker">Tracker</div>
                    <div>
                        <h2>Build tracker</h2>
                        <p>Mobalytics gear, gems, and passives per act. Pick an act, then switch tabs. Progress saves in this browser only.</p>
                    </div>
                </div>

                <div class="tracker-warning" id="tracker-storage-warning" role="status">
                    Could not save progress (browser storage full or blocked). Your checks still work until you reload.
                </div>

                <div class="tracker-toolbar">
                    <div class="tracker-act-tabs" id="tracker-act-tabs" role="tablist" aria-label="Build tracker acts"></div>
                    <div class="tracker-subtoolbar">
                        <div class="tracker-category-tabs" id="tracker-category-tabs" role="tablist" aria-label="Build tracker categories"></div>
                        <div class="tracker-actions">
                            <button type="button" class="tracker-btn" id="tracker-reset-act">Reset current act</button>
                            <button type="button" class="tracker-btn danger" id="tracker-reset-all">Reset all acts</button>
                        </div>
                    </div>
                </div>

                <div id="tracker-categories"></div>
            </section>
"""

sources_section = """
            <section id="sources" class="section">
                <div class="section-head">
                    <div class="section-kicker">Links</div>
                    <div>
                        <h2>Build sources</h2>
                        <p>Mobalytics planner for gear, gems, and passives while you follow the act guide.</p>
                    </div>
                </div>
                <article class="card highlight">
                    <h3>Reference links</h3>
                    <div class="resource-links">
                        <a class="resource-link" href="https://mobalytics.gg/poe-2/profile/bright-gun-0gguoz/builds/8520fdce-220e-4906-a6e5-3207c709cd8f" target="_blank" rel="noopener noreferrer">
                            <strong>Mobalytics planner</strong>
                            <span>Ice Shot Deadeye — equipment, skill gems, and passive priorities by act.</span>
                        </a>
                    </div>
                </article>
            </section>
"""

new_nav = """            <nav>
                <a href="#overview">Overview</a>
                <a href="#sources">Sources</a>
                <a href="#act1">Act 1</a>
                <a href="#act2">Act 2</a>
                <a href="#act3">Act 3</a>
                <a href="#act4">Act 4</a>
                <a href="#interlude">Interlude</a>
                <a href="#mapping">Mapping</a>
                <a href="#rotation">Boss Rotation</a>
                <a href="#build-tracker">Build Tracker</a>
                <a href="#transition-checks">Transition Checks</a>
                <a href="#timesaves">Time Saves</a>
            </nav>"""

nav_old_start = html.index("<nav>")
nav_old_end = html.index("</nav>", nav_old_start) + len("</nav>")
html = html[:nav_old_start] + new_nav + html[nav_old_end:]

html = html.replace(
    '<input class="searchbox" id="search" placeholder="Filter visible cards/timelines…">',
    '<input class="searchbox" id="search" placeholder="Filter cards, timelines, tracker…">',
)

html = html.replace(
    "        .hidden-by-search {\n            display: none !important;\n        }\n\n        .violet .section-kicker",
    "        .hidden-by-search {\n            display: none !important;\n        }\n\n"
    + resource_css
    + "\n"
    + tracker_css
    + "        .violet .section-kicker",
)

print_tracker_css = """
            .tracker-row input[type="checkbox"] {
                appearance: none;
                width: auto;
                height: auto;
                margin: 0;
            }

            .tracker-row input[type="checkbox"]::after {
                content: "[ ] ";
            }

            .tracker-row input[type="checkbox"]:checked::after {
                content: "[x] ";
            }
"""

if ".tracker-row input[type=\"checkbox\"]::after" not in html:
    html = html.replace(
        "            .route-grid {\n                grid-template-columns: .9fr 1.5fr;\n            }\n        }",
        "            .route-grid {\n                grid-template-columns: .9fr 1.5fr;\n            }\n"
        + print_tracker_css
        + "        }",
    )

hero_end = html.index("</header>", html.index('id="overview"')) + len("</header>")
if 'id="sources"' not in html:
    html = html[:hero_end] + "\n" + sources_section + html[hero_end:]

rotation_end = html.index("</section>", html.index('id="rotation"')) + len("</section>")
if 'id="build-tracker"' not in html:
    html = html[:rotation_end] + "\n" + build_tracker_section + html[rotation_end:]

html = html.replace('id="checklists"', 'id="transition-checks"')
html = html.replace(
    "<div><h2>Practical checklists</h2><p>Use these before major transitions",
    "<div><h2>Transition checks</h2><p>Use these before major transitions",
)

old_script_start = html.rindex("    <script>")
html = html[:old_script_start]

json_script = f'    <script id="build-tracker-data" type="application/json">{build_json}</script>\n'
nav_script = """    <script>
        const links = Array.from(document.querySelectorAll('nav a'));
        const sections = links.map(a => document.querySelector(a.getAttribute('href'))).filter(Boolean);
        const onScroll = () => {
            let current = sections[0];
            for (const section of sections) {
                if (section.getBoundingClientRect().top < 140) {
                    current = section;
                }
            }
            links.forEach(a => a.classList.toggle('active', a.getAttribute('href') === '#' + current.id));
        };
        document.addEventListener('scroll', onScroll, { passive: true });
        onScroll();

        const search = document.getElementById('search');
        const searchable = Array.from(document.querySelectorAll('.card, .timeline-panel, .tracker-panel'));
        search.addEventListener('input', () => {
            const q = search.value.trim().toLowerCase();
            searchable.forEach(el => {
                el.classList.toggle('hidden-by-search', q && !el.innerText.toLowerCase().includes(q));
            });
        });
    </script>
"""

html = html + json_script + "    <script>\n" + tracker_js + "\n    </script>\n" + nav_script + "\n</body></html>\n"

html_path.write_text(html, encoding="utf-8")
print("patched", html_path, "size", html_path.stat().st_size)
