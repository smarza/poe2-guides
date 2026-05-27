# Prompt — Create static POE 2 campaign site from markdown guide

Use this prompt after creating a guide in `Dev/Guides/`.

---

## Message to send to the agent

```
Create a static single-file HTML campaign guide from the markdown guide below.

## Inputs

- Markdown guide: @Dev/Guides/<slug>_timeline_guide.md
- Reference HTML layout/style: @deadeye.html
- Existing build page to mirror if updating: @monk.html (only if relevant)
- Output HTML file: <slug>.html (repo root, example: monk.html)
- Build short name for sidebar/logo: <SHORT CODE> (example: MK)
- Public slug / URL path: <slug> (example: monk)
- Page title: <BUILD TITLE> (example: Monk Leveling POE 2 — Detailed Act-by-Act Guide)
- Accent theme: <primary color concept> (example: lightning/amber for Monk, ice/cyan for Deadeye)

Optional source links section:
- Planner URL: <PLANNER URL or leave empty>
- YouTube URL: <VIDEO URL or leave empty>

Optional Mobalytics build export (for interactive gameplay checklists):
- JSON export: @Dev/Exports/<mobalytics-slug>/<mobalytics-slug>.json
- Generate with: `pwsh -File Dev/Scripts/Export-MobalyticsBuild.ps1 -Url "<PLANNER URL>" -Format json`
- Expected shape: `acts[]` with `equipment[]`, `skillGems[]`, `passiveTree[]` grouped by act label (`Act 1`, `Act 2`, `Act 3`, `Act 4`, `Interludes`, etc.)

Landing page index: @index.html
Update index.html if this is a new guide.

## Goal

Build a guide meant to be used DURING the campaign.
It must be easy to scan while playing.
Do not overload the page with every markdown paragraph.
Follow the same information architecture as the reference HTML.

When Mobalytics JSON is available, add a **Build Tracker** with persistent checkboxes so the player can mark gear, gems, and passives per act while progressing through the campaign.

## Hard requirements

1. **Single-file static HTML**
   - All CSS inline in `<style>`
   - All JS inline in `<script>`
   - No external assets
   - No frameworks
   - No CDN fonts/images
   - No network calls at runtime
   - `localStorage` is allowed for Build Tracker persistence

2. **Act-oriented step-by-step layout**
   - Sidebar navigation
   - Hero overview
   - One section per act / interlude
   - Sticky timeline panel inside each act section
   - Right-side cards with practical instructions

3. **Do not copy the markdown verbatim**
   - Condense intelligently
   - Keep timestamps, levels, skills, gear priorities, and warnings
   - Remove repetition across sections

4. **Match the reference page standards**
   Use the same section/card pattern as `@deadeye.html` and `@monk.html`.

## Required page structure

### A. Document shell
- `<!DOCTYPE html>`
- responsive viewport meta tag
- descriptive `<title>`
- dark gradient theme similar to reference
- sticky left sidebar + scrollable main content
- print styles
- mobile breakpoints

### B. Sidebar
Include links to:
- Overview
- Sources (only if planner/video links provided)
- Act 1
- Act 2
- Act 3
- Act 4
- Interlude (if guide covers it)
- Boss Rotation
- Build Tracker (interactive checklists — only if Mobalytics JSON provided)
- Transition Checks (practical pre-boss checks from markdown)
- Time Saves

Also include:
- brand block with logo initials
- short subtitle
- one side-note with the most important run rule
- search box that filters `.card` and `.timeline-panel`

Implement active nav highlighting on scroll exactly like the reference pages.

### C. Hero (`#overview`)
Include:
- eyebrow label
- large title with gradient accent on build name
- one paragraph summary
- 4 stat cards with the most important breakpoints

Example stat cards:
- build phases
- first major breakpoint level/time
- major build switch
- final campaign checkpoint

### D. Overview section
Two-column grid with cards for:
- Core route identity (pill row with phase summaries)
- What makes or breaks the run (highlight card + callout)
- Skill progression summary table
- Target pace splits table

Keep this section concise.

### E. Sources section (`#sources`) — only if links provided
Add a section with:
- heading: Build sources
- two external link cards:
  - Mobalytics planner
  - YouTube video
- links open in new tab with `rel="noopener noreferrer"`

If no links are provided, omit this section and nav item.

### F. Act sections
Create one section per act/interlude using this exact layout:

Left column:
- sticky `.timeline-panel`
- table columns: `Time | Lvl | Milestone`
- use `.time-cell`, `.level-chip`, `.tiny` subnotes

Right column cards:
1. **Primary objective**
2. **Do this session** (or **Do this**)
3. **Early gear priorities** or **Gear priorities** or **Vendor check**
4. Optional extra cards only when important:
   - highlight card for major power spike
   - warn card for failure point
   - danger card for survival/stat wall

Color-code act headers like the reference:
- Act 1 → amber
- Act 2 → violet
- Act 3 → blue
- Act 4 → amber
- Interlude → green

Each act timeline should contain the most important 8–14 milestones for that act only.
Do not dump the entire global milestone table into every act.

### G. Boss Rotation section (`#rotation`)
Convert the final boss loop into 5–7 `.step` cards in `.rotation`.
Use the simplified endgame/campaign boss rotation from the markdown guide.

### H. Build Tracker section (`#build-tracker`) — only if Mobalytics JSON provided

Add an interactive gameplay section so the player can track build progress while playing.
Data source: the Mobalytics JSON export (`acts[]` structure).

This section is separate from the narrative guide. It is a live checklist, not a summary card.

#### H.1 Section layout — two-level tabs (avoid long scroll)

Use **nested tabs** so the player never sees all three categories stacked at once.

**Level 1 — Act tabs** (top row):
- One tab per act from JSON (`Act 1` → `Act 4` → `Interludes` when present)
- Show combined progress on each act tab: `Act 2 (24/58)`
- Default selected act: `Act 1`

**Level 2 — Category tabs** (second row, visible only after an act is selected):
- **Equipment** (`#build-tracker-equipment`)
- **Skill Gems** (`#build-tracker-gems`)
- **Passive Tree** (`#build-tracker-passives`)
- Show per-category progress for the **currently selected act**: `Equipment (9/42)`
- Default selected category: `Equipment`
- Only **one** category panel visible at a time (hide the other two with CSS/JS, do not render all three stacked)

Layout order inside `#build-tracker`:
1. Section header + storage warning
2. Act tabs + reset buttons
3. Category tabs (Equipment / Skill Gems / Passive Tree)
4. Single checklist panel for the active act + active category

Do **not** stack Equipment, Skill Gems, and Passive Tree vertically in the same view — that creates too much scrolling during gameplay.

#### H.2 Checklist item structure (mirror JSON)

Render from JSON fields:

**Equipment** (per act):
- parent item: `equipment[].name`
- child items: each string in `equipment[].modifiers[]`
- optional muted subline: `equipment[].slot` (small, secondary)

**Skill Gems** (per act):
- parent item: `skillGems[].name` (already includes level when present, e.g. `Falling Thunder (Level 4)`)
- child items: each string in `skillGems[].supports[]`

**Passive Tree** (per act):
- flat list only (no children unless JSON adds them later)
- parent item: `passiveTree[].name`

Example markdown-like hierarchy to reproduce in HTML:

```markdown
## Act 1

### Equipment
- [ ] Gothic Quarterstaff
    - [ ] Adds 3 to 7 Physical Damage
    - [ ] Adds 4 to 6 Fire Damage

### Skill Gems
- [ ] Falling Thunder (Level 4)
    - [ ] Lightning Attunement
    - [ ] Shock

### Passive Tree
- [ ] Flow Like Water
- [ ] Essence of the Storm
```

#### H.3 Interactive checkbox behavior

- Use real `<input type="checkbox">` elements (accessible, keyboard-friendly)
- Parent checkbox toggles all children in that group
- If user manually toggles children, parent becomes:
  - checked when all children checked
  - indeterminate when some children checked
  - unchecked when none checked
- Checked items should look visually complete (muted text + strikethrough optional, but keep readable)

#### H.4 localStorage persistence (required)

Persist user progress locally in the browser. No server, no network calls.

Storage key namespace:
- `poe2-guides:<slug>:build-tracker:v1`

Store a compact JSON object, for example:

```json
{
  "equipment": {
    "Act 1": {
      "weapon-fourquarterstaff3": { "self": true, "children": { "mod-0": true, "mod-1": false } }
    }
  },
  "skillGems": {},
  "passiveTree": {}
}
```

Rules:
- Generate stable item IDs from JSON (`slug` when available; fallback to normalized `name`)
- Generate stable child IDs from modifier/support text hash or index (`mod-0`, `support-1`, etc.)
- Load saved state on `DOMContentLoaded` before rendering interactions
- Save on every checkbox `change` event (debounce max 100ms if needed)
- Handle `localStorage` quota errors gracefully (show one small inline warning, do not crash page)
- If JSON act list changes in a future update, ignore unknown saved IDs safely

Add tracker controls at top of `#build-tracker`:
- **Reset current act** button (only active act tab)
- **Reset all acts** button with `confirm()` dialog

#### H.5 Progress indicators

- **Act tab**: combined progress across all three categories for that act — `Act 1 (18/52)`
- **Category tab**: progress for that category in the active act only — `Skill Gems (7/16)`

Do not repeat all three category blocks on screen at once; progress belongs on the tabs.

#### H.6 UX and styling rules for tracker

- Keep checklist rows compact and scannable during gameplay
- Indent child items clearly (2 levels max)
- Act tabs and category tabs must work on mobile (horizontal scroll pills)
- Category tabs sit directly under act tabs; switching act keeps the same category tab selected when possible
- Single visible checklist panel keeps page height short
- Do not hide tracker behind heavy animations
- Search box in sidebar should also filter tracker items and act panels
- Print stylesheet: show unchecked/checked state as text markers (`[ ]` / `[x]`), not hidden

#### H.7 When JSON is missing

If no Mobalytics JSON is provided:
- omit `#build-tracker` section entirely
- omit sidebar nav item **Build Tracker**
- do not add placeholder TODO checklists in this section

### I. Transition Checks section (`#transition-checks`)

Keep the existing practical transition checklists from markdown (non-persistent tables/cards):
- one checklist before a major transition (example: before Siphoning Strike switch / before Act 3 final / before Tawakai)
- one checklist before a late-campaign checkpoint

These are guidance checks, not Mobalytics item tracking.

### J. Time Saves section (`#timesaves`)
One warn card with a compact table:
- `Problem in run`
- `Correction`

Use transcript-backed time-loss patterns from the markdown guide.

### K. Footer
Exact line:
`Built as a static single-file HTML guide. No external assets, frameworks, or network calls.`

## Content rules

### Include
- exact skill names
- exact support names
- ascendancy choice and key bonuses
- weapon/base names
- vendor strategy
- survival warnings
- timestamp milestones
- level breakpoints when known
- “optional / skip / dropped later” notes when important

### Exclude
- long transcript quotes
- full passive tree in narrative cards (tracker section may list priority passives from JSON)
- duplicate tables already shown elsewhere
- mapping/endgame sections unless the guide explicitly covers them
- excessive theorycrafting
- placeholder lorem ipsum

## Visual / UX rules

- Match spacing, card radius, typography, and layout conventions from `@deadeye.html`
- Keep templates scannable with blank lines between logical blocks
- Use strong tags for important game terms
- Keep sidebar usable on mobile
- Hide level column on very small screens if using the same responsive behavior as reference
- Search filter must hide non-matching cards/timelines
- Build tracker checklists must remain usable with one hand while playing (large tap targets, clear spacing)

## Build tracker JavaScript requirements

Inline JS must include, in addition to existing nav/search behavior:

1. `loadBuildTrackerState()` / `saveBuildTrackerState()`
2. `renderBuildTrackerFromData(buildData)` if JSON is embedded inline
3. two-level tabs: `activeAct` + `activeCategory` state
4. `renderActTabs()` / `renderCategoryTabs()` / `renderActiveCategory()` (only one category panel in DOM)
5. parent/child checkbox synchronization
6. per-act and per-category progress counters on tab labels
7. reset handlers with confirmation

Embed Mobalytics JSON inline when provided:

```html
<script id="build-tracker-data" type="application/json">...</script>
```

Do not fetch JSON at runtime.

## Theme guidance

Choose accent colors based on build identity:
- lightning/shock monk → amber + violet
- ice/bow deadeye → cyan + violet
- fire builds → orange/red
- poison builds → green

Do not clone the Deadeye palette if the build identity differs.

## Index page update

If adding a new guide, update `index.html`:
- add a new guide card linking to `/<slug>`
- short one-line description
- keep page static and self-contained

Do not break existing guide links.

## File placement

- HTML guide goes in repo root: `<slug>.html`
- Do not place published HTML under `Dev/`
- Keep source markdown in `Dev/Guides/`

## Quality checks before finishing

Verify all of the following:

- [ ] Page opens correctly as a local file and as GitHub Pages URL
- [ ] Sidebar anchor links scroll to all sections
- [ ] Each act section has timeline + primary objective + do-this + gear card
- [ ] Final build loop is reflected in Boss Rotation
- [ ] Build Tracker section exists when Mobalytics JSON input is provided
- [ ] Build Tracker uses two-level tabs (Act → Equipment / Skill Gems / Passive Tree)
- [ ] Only one category checklist is visible at a time (no stacked scroll)
- [ ] Checkbox state persists in `localStorage` and restores after reload
- [ ] Parent checkbox toggles all child modifiers/supports correctly
- [ ] Reset current act / reset all acts works with confirmation
- [ ] Transition Checks section remains separate from Build Tracker
- [ ] Page is not overly long or repetitive
- [ ] No external dependencies
- [ ] No runtime network calls (JSON must be embedded)
- [ ] Sources section present only when links provided
- [ ] `index.html` updated if this is a new guide
- [ ] Output filename is simple lowercase slug (`monk.html`, `deadeye.html`)

## Git publish steps — REQUIRED at the end

After creating/updating the HTML (and `index.html` if needed), commit and push to GitHub.

Repository remote:
- https://github.com/smarza/poe2-guides.git

Run these steps in the repo root:

1. Check changes:
   - `git status`
   - `git diff`

2. Stage relevant files only:
   - `<slug>.html`
   - `index.html` (if changed)
   - do NOT commit transient local files from `Dev/Transcriptions/` unless explicitly requested

3. Commit with a message focused on why:
   - example: `Add Monk leveling static campaign guide page`

4. Push:
   - `git push origin main`

5. Confirm publish:
   - remind the user the GitHub Pages URL will be:
     - `https://smarza.github.io/poe2-guides/<slug>`
   - if Pages is configured with branch deploy from `main`, no GitHub Actions workflow is needed

Do not force push.
Do not amend unless a hook modified files after commit.
Do not change git config.

## Deliverable

Return:
1. path to created/updated `<slug>.html`
2. whether `index.html` was updated
3. commit hash
4. public URL(s)
5. short summary of act sections created
6. whether Build Tracker was generated from Mobalytics JSON and how many checklist items per act/category
```

---

## Example filled prompt

```
Create a static single-file HTML campaign guide from the markdown guide below.

Markdown guide: @Dev/Guides/poe2_monk_leveling_timeline_guide.md
Reference HTML layout/style: @deadeye.html
Existing build page to mirror: @monk.html
Output HTML file: monk.html
Build short name for sidebar/logo: MK
Public slug / URL path: monk
Page title: Monk Leveling POE 2 — Detailed Act-by-Act Guide
Accent theme: lightning/amber

Planner URL: https://mobalytics.gg/poe-2/profile/spud-the-king-nksem3/builds/one-shot-monk-leveling-poe2-0-5-league-starter
YouTube URL: https://www.youtube.com/watch?v=s2LkL7ev27Y
Mobalytics JSON export: @Dev/Exports/one-shot-monk-leveling-poe2-0-5-league-starter/one-shot-monk-leveling-poe2-0-5-league-starter.json

Landing page index: @index.html
Update index.html only if needed.

Include Build Tracker checklists (Equipment, Skill Gems, Passive Tree) grouped by act with localStorage persistence.
Keep Transition Checks as a separate non-persistent section from markdown milestones.
```

---

## Build tracker data contract (reference)

When Mobalytics JSON is provided, treat this as the source of truth for tracker content:

```json
{
  "buildName": "ONE SHOT Monk Leveling [PoE2 0.5 League Starter]",
  "slug": "one-shot-monk-leveling-poe2-0-5-league-starter",
  "acts": [
    {
      "act": "Act 1",
      "equipment": [
        { "name": "Gothic Quarterstaff", "slot": "mainHand", "slug": "weapon-fourquarterstaff3", "modifiers": ["Adds 3 to 7 Physical Damage"] }
      ],
      "skillGems": [
        { "name": "Falling Thunder (Level 4)", "slug": "fallingthunderplayer", "supports": ["Lightning Attunement", "Shock"] }
      ],
      "passiveTree": [
        { "name": "Flow Like Water", "slug": "flow-like-water", "tree": "main" }
      ]
    }
  ]
}
```

Do not invent tracker items that are not in JSON. Narrative guide cards may still condense explanations from markdown.
