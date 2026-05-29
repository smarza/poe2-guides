# POE 2 Power Charge Martial Artist — Falling Thunder Campaign Guide

Source transcript: `transcript_UJrW6xEk52o_with_timeline.md`  
Video: `https://www.youtube.com/watch?v=UJrW6xEk52o`  
Planner (0.5): `https://mobalytics.gg/poe-2/profile/p4wnyhof/builds/power-charge-martial-artist`

> **Goal of this guide:** reproduce the same Monk campaign pacing and power spikes from the video. This is a **build walkthrough**, not a live speedrun — the transcript explains *what* to craft and *when*, not every zone route. Copy the power spikes and skill transitions; you do not need to mirror every early experiment. The demo run uses **Invoker**; the intended endgame ascendancy is **Martial Artist** (patch 0.5).

---

## Executive Summary

This run levels a **Monk** from Act 1 through Act 4 using **Falling Thunder** as the main burst, fed by **Power Charges** generated through culling, stun combos, and shock extraction.

1. **Early Act 1 — Melee bridge (levels 1–~10)**  
   **Falling Thunder** + **Killing Palm** for charges, **Frozen Locus** for pack control, then **Rage** / **Rapid Attacks** / optional **Frost Bomb**. Weakness: slow single-target until the stun combo arrives.

2. **Late Act 1 — Wind Blast / Wing Blast stun engine (~level 10–15)**  
   Cross-class **Wing Blast** (Druid) + **Wind Blast** (Monk) deletes packs and grants **3 Power Charges vs bosses** on stun. **Devour** replaces **Killing Palm** for corpse diving, healing, and forward momentum. **Herald of Thunder** layers shock scaling. Phase ends when **Storm Wave** + **Siphoning Strike** unlock at tier 7.

3. **Act 2 — Shock extraction core**  
   **Storm Wave** shocks; **Siphoning Strike** steals shock for charges and leaves a shockwave. Path to **Hollow Palm Technique** early. **Full armor** until Act 4. Bosses die in repeated charge → **Falling Thunder** cycles. Weakness: mana hunger on the Storm Wave loop.

4. **Act 3 onward — Hollow Palm nuke**  
   Unequip quarterstaff; scale with **+melee skills** on gear. **Perpetual Charge** on **Falling Thunder**, **Living Lightning** on **Storm Wave**. **Clarity** + **Cannibalism** on **Herald of Thunder**; **Gorge** on **Devour**. Nothing in Act 3 should stop you.

5. **Act 4 — Defensive pivot + optional boss tech**  
   Swap toward **evasion / energy shield** on body armor for **Hollow Palm** scaling. **Ghost Dance** replaces sustain auras. Optional **Whirling Assault** for Martial Artist boss bursts — **not required** for campaign or mapping entry.

**Biggest practical lessons:**

- **Power Charges are the entire build.** Every phase exists to generate charges faster so **Falling Thunder** hits harder.
- **Wing Blast + Wind Blast** is a temporary Act 1 powerhouse; do not cling to it after **Storm Wave** + **Siphoning Strike** come online.
- **Stack full armor in Acts 1–3.** Evasion/ES only matter once **Hollow Palm** is active and you reach Act 4.
- **Always confirm shock is on the boss** before spending charges with **Falling Thunder** after a **Siphoning Strike** extraction.
- **Do not over-stun with Wind Blast** — it primes stun but cannot heavy-stun, keeping enemies ready for **Wing Blast**.
- The creator explicitly says this combo carries cleanly to **mapping** and **Arbitrator of Ash** without swapping to **Whirling Assault**.

---

## Target Milestones at a Glance

| Target time | Milestone | What should be true by then |
|---:|---|---|
| 00:00:46 | Character start | Monk with quarterstaff, **Falling Thunder**, **Killing Palm** socketed. |
| 00:01:05 | Clearfell camp gem | Craft **Frozen Locus** from the level-1 skill gem in the tiny camp. |
| 00:02:03 | Devourer / Beyrah | Use **Frozen Locus** at your feet while attacking; apply **Falling Thunder** for shock. |
| 00:02:24 | First support | **Rage** from the Devourer drop on main attacks. |
| 00:02:40 | Grell wood witch | Second support gem; optional **Frost Bomb** skill if a low-level gem drops. |
| 00:03:09 | Attack speed support | **Rapid Attacks** on quarterstaff strikes. |
| 00:03:17 | Rusted King prep | Build **Power Charges** on nearby packs before the fight; wait out early damage reduction. |
| 00:03:47 | Tier-3 cross-class pick | Spend first level-3 gem on **Wing Blast** (Druid), not a Monk skill yet. |
| 00:04:27 | Weapon set 2 | Equip any **talisman** in weapon set 2 so **Wing Blast** works. |
| 00:04:38 | Monk stun primer | Add **Wind Blast** — daze → stun setup for **Wing Blast**. |
| 00:05:45 | Support reshuffle | Move **Rage** + **Rapid Attacks** to **Wind Blast**; add **Brink** + **Impact Shockwave**. |
| 00:06:33 | Falling Thunder support | **Elemental Armament** on **Falling Thunder** if slots remain. |
| 00:06:41 | Drop Frozen Locus | Remove **Frozen Locus** once **Wind Blast** / **Wing Blast** clear is online. |
| 00:06:51 | Movement skill | Third tier-3 gem → **Pounce** for area speed (slight cooldown nerf in 0.5). |
| 00:07:06 | King of the Mist | Kill boss in **Fraythorn**; pick up first spirit gem slot context. |
| 00:07:21 | Shock aura | Socket **Herald of Thunder** — everything from here is shock-focused. |
| 00:07:29 | Optional boss boost | **Fist of War** on **Falling Thunder** if a spare support drops (ancestral, not spammed). |
| 00:07:47 | Tier-5 gem | After **Executioner**, unlock next major skill tier. |
| 00:08:03 | Devour swap | Replace **Killing Palm** with **Devour**; add **Thrill of the Kill**. |
| 00:08:30 | Zone-clear loop | **Wind Blast** → **Wing Blast** packs, then **Devour** corpses → **Falling Thunder** forward. |
| 00:09:25 | Gear rule Act 1 | Full **armor** on every slot — ignore ES/evasion for now. |
| 00:09:48 | Early passives | Skill speed → attack damage → shock chance → lightning damage; strength node for talisman if needed. |
| 00:10:17 | Act 1 complete | Roughly **level 14–15**; **Count** boss is a stun → charge → **Falling Thunder** execution. |
| 00:10:41 | Act 2 start | Keep **Devour** + **Falling Thunder** + **Wind Blast** / **Wing Blast** while pushing. |
| 00:10:54 | Tier-7 core switch | Craft **Storm Wave** + **Siphoning Strike** — this becomes the real build. |
| 00:12:12 | Support assignment | **Rage** + **Shock to 100%** on **Storm Wave**; **Rapid Attacks** + **Charge Perfusion** on **Siphoning Strike**. |
| 00:12:42 | Frost Bomb dropped | Stop **Frost Bomb**; move **Wing Blast** to **Devour** for faster dive animation. |
| 00:13:12 | Hollow Palm rush | Path passives toward **Hollow Palm Technique** as early as Act 2 allows. |
| 00:13:56 | Shock reapply node | Take **chance on consuming shock to reapply it** before **Jaman' Rai**. |
| 00:14:28 | Ascendancy note | Martial Artist **Way of the Mountain** + **Hollow Focus** belt stun tech (demo used Invoker). |
| 00:15:27 | Act 3 start | More support slots; first quality investments land here. |
| 00:15:33 | Jeweler's orbs | 1st → **Perpetual Charge** on **Falling Thunder**; 2nd → **Living Lightning** on **Storm Wave**. |
| 00:16:17 | Spirit upgrade | After **Ashen Bach**, +30 spirit; skip **Lingering Illusion** (charges are trivial). |
| 00:16:39 | Herald sustain | **Clarity** + **Cannibalism** on **Herald of Thunder** while still on full armor. |
| 00:16:51 | Devour flask tech | **Gorge** on **Devour** for flask charges from corpses. |
| 00:17:09 | Second ascension | **Way of the Mountain** + **Way of the Stone Fist** or bonus runes or **Hollow Focus**; +2 max Power Charges. |
| 00:18:00 | Shock scaling | Top-tree node: increased **magnitude of shock** you inflict. |
| 00:18:24 | Hollow Palm online | No weapon equipped; talisman in set 2; **+melee skills** on gloves/amulet. |
| 00:18:39 | Doryani | Easiest fight in the run if shock loop is maintained. |
| 00:19:22 | Act 4 start | Begin shifting gear toward ES/evasion on body armor. |
| 00:19:26 | Defensive pivot | Passives toward ES/evasion; swap **Clarity**/**Cannibalism** for **Ghost Dance**. |
| 00:20:16 | Herald damage | **Elemental Armament** + **Elemental Focus** on **Herald of Thunder**. |
| 00:20:24 | Optional boss skill | **Whirling Assault** + Martial Artist ghost copies — optional, not mandatory. |
| 00:20:48 | Campaign carry | **Falling Thunder** combo valid through mapping to **Arbitrator of Ash**. |
| 00:21:32 | Guide endpoint | Act 4 interludes easy with **Devour**; full 0.5 Martial Artist mapping guide pending patch. |

---

## Core Build Concept

### Early concept

You are a melee Monk who spends **Power Charges** for burst:

1. **Killing Palm** culled enemies → charges.
2. **Falling Thunder** consumes charges for massive lightning burst + shock.
3. **Frozen Locus** bridges weak early clear until the stun engine arrives.
4. **Frost Bomb** (optional) adds exposure while you still rely on melee staff strikes.

### Midgame concept

The build becomes a **range + melee hybrid** that still counts as melee for **Rage**:

1. **Wind Blast** dazes at range and builds stagger.
2. At ~**70% stagger** (deeper orange bar), **Wing Blast** heavy-stuns and grants **3 Power Charges vs bosses**.
3. Pack clear: **Wind Blast** → **Wing Blast** repeat.
4. **Devour** replaces palm culling — jump forward, eat corpses, heal, gain charges.
5. Zone flow: clear with stun combo → **Devour** → **Falling Thunder** → repeat forward.

This is powerful but gets replaced for clearing once shock extraction is faster.

### Final practical concept

The winning campaign loop after Act 2:

1. **Storm Wave** applies shock (supported by **Rage**, **Shock to 100%**, **Living Lightning**).
2. **Siphoning Strike** steals shock → **Power Charges** + shockwave → feeds **Herald of Thunder**.
3. Stack charges (repeat 2–3×, or **Wing Blast** a stunned boss for instant 3).
4. Confirm shock is still on the target.
5. **Falling Thunder** with **Perpetual Charge** for multi-hit burst.
6. **Hollow Palm Technique** — no quarterstaff equipped; talisman stays in weapon set 2; scale **+melee skills** and Hollow Palm ES/evasion bonuses in Act 4.

---

## Skill and Support Progression

| Time | Skill/support | Use |
|---:|---|---|
| 00:00:46 | **Falling Thunder** | Main charge-spending burst; applies shock. |
| 00:00:52 | **Killing Palm** | Early culling for Power Charges. **Dropped** at 00:08:03. |
| 00:01:22 | **Frozen Locus** | Ice crystal explosions (~350% attack damage); bridge clear. **Removed** at 00:06:41. |
| 00:02:24 | **Rage** | +30% attack damage; moves from staff → **Wind Blast** → **Storm Wave**. |
| 00:02:50 | **Frost Bomb** (optional) | Elemental exposure during early staff phase. **Dropped** in Act 2. |
| 00:03:11 | **Rapid Attacks** | Staff → **Wind Blast** → **Siphoning Strike**. |
| 00:03:47 | **Wing Blast** (Druid) | Pack delete + 3 boss charges on stun; needs talisman in set 2. |
| 00:04:38 | **Wind Blast** | Daze/stagger primer for **Wing Blast**; cannot over-stun. |
| 00:05:57 | **Brink** | Stun buildup on **Wind Blast**. |
| 00:06:17 | **Impact Shockwave** | On heavy stun from **Wind Blast** — clear breakthrough. |
| 00:06:36 | **Elemental Armament** | +20% damage on **Falling Thunder**. |
| 00:06:53 | **Pounce** | Primary movement skill through Acts 1–2. |
| 00:07:21 | **Herald of Thunder** | Shock scaling aura; later hosts **Clarity**/**Cannibalism** or **Ghost Dance** tech. |
| 00:07:31 | **Fist of War** (optional) | Ancestral boost on **Falling Thunder** for boss swings. |
| 00:08:03 | **Devour** | Replaces **Killing Palm**; corpse consume, heal, charges. |
| 00:08:22 | **Thrill of the Kill** | +25% of damage as lightning for 8s on kill. |
| 00:10:54 | **Storm Wave** | Ranged shock applicator — core Act 2+ clear and boss setup. |
| 00:10:57 | **Siphoning Strike** | Steals shock → charges + shockwave; boss and pack engine. |
| 00:12:15 | **Shock to 100%** | On **Storm Wave** — reliable shock. |
| 00:12:35 | **Charge Perfusion** | More charges per shock extraction on **Siphoning Strike**. |
| 00:12:49 | **Wing Blast** → **Devour** | Speeds dive/eat animation between packs. |
| 00:13:01 | **Mark of Siphoning** (optional) | On pawns/minions for mana leech — helps mana-hungry loop. |
| 00:15:39 | **Perpetual Charge** | **Falling Thunder** may not consume charges — multi-cast burst. |
| 00:15:58 | **Living Lightning** | Extra shock targets from **Storm Wave** (creator tried **Branching Fissures**, dropped it). |
| 00:16:39 | **Clarity** | Mana sustain on **Herald of Thunder** (Act 3; respec mana nodes). |
| 00:16:40 | **Cannibalism** | Life on kill via **Herald of Thunder**. |
| 00:16:53 | **Gorge** | Flask charges from **Devour** corpse eats. |
| 00:20:01 | **Ghost Dance** | Replaces **Clarity**/**Cannibalism** in Act 4 (regen-over-time version). |
| 00:20:16 | **Elemental Focus** | Herald damage boost in Act 4. |
| 00:20:27 | **Whirling Assault** (optional) | Martial Artist boss option with ghost copies — skip for campaign efficiency. |

---

## Passive Tree / Ascendancy Priorities

The transcript describes priorities, not a full tree export.

### Early passive priorities

- Bonus **skill speed** first.
- **Attack damage** with more attack/skill speed.
- Path through **increased chance to shock** and **lightning damage**.
- Temporary **strength** node if needed to equip talisman — respec once requirements are met naturally.
- Take attribute nodes (**dexterity**, **intelligence**, **strength**) only as required for gear/gems.

### Weapon set ideas

- **Weapon set 1:** empty (no weapon) once **Hollow Palm Technique** is taken — quarterstaff skills still work.
- **Weapon set 2:** **talisman** (any power level) solely to cast **Wing Blast** / **Devour** dive tech.

### Ascendancy choice and timing

**Intended (patch 0.5): Martial Artist**

First ascendancy options discussed:

- **Way of the Mountain** — 200% of Surpassing Chance per enemy power to gain **Mountain's Teachings** on immobilizing (stun) enemies, up to 30 stacks → **20% more attack damage**, stun immunity, damage reduction.
- **Bonus runes** (2 points) — slot runes on body pieces.
- **Hollow Focus** belts — belts are always primed for stun; **Wing Blast** them for **3 instant Power Charges**.

Second ascendancy (Act 3):

- **Way of the Mountain** + **Way of the Stone Fist** (if not taken yet).
- **+2 maximum Power Charges**.
- Respec mana-efficiency nodes after **Clarity** — take more **lightning damage**, **lightning penetration**.

**Demo ascendancy: Invoker**

- Used **I'm the Thunder** for bonus damage and shock ground.
- Creator notes Martial Artist will replace this on 0.5 release.

### Act 2 passive priorities

- Rush **Hollow Palm Technique** — more damage than a good quarterstaff at that stage.
- **Reduced mana cost of skills** (right side).
- **Increased chance to inflict ailments** + **elemental damage**.
- Middle path: **chance on consuming shock to reapply it** (before **Jaman' Rai**).

### Act 3 passive priorities

- Respec mana nodes after **Clarity**.
- **Lightning damage** (two clusters) + **lightning penetration**.
- **Killer Instinct** — remove redundant attack speed if connected via jewel socket.
- Top: **increased magnitude of shock** inflicted.

### Act 4 defensive priorities

- **Evasion rating** and **energy shield** on passives and gear.
- Supports **Hollow Palm** body-armor scaling (attack speed per evasion, crit per ES).

---

## Gear Rules

### General item priorities (Acts 1–3)

- **Full armor** on helmet, body, gloves, boots.
- Creator states armor is simple damage reduction; ES/evasion do not help much yet.
- Life and resistances as available.
- Do not slow down for perfect rares — smooth progression beats min-maxing early bases.

### General item priorities (Act 4+)

- Shift body armor (and overall gear) toward **evasion** and **energy shield** for **Hollow Palm** bonuses.
- Still prioritize life/resists; the pivot is for damage scaling, not only defense.
- Keep a **talisman** in weapon set 2 at all times.

### Weapon priorities

- Early: any quarterstaff until **Hollow Palm** — then **unequip weapon** entirely.
- After **Hollow Palm**: hunt **+melee skills** on gloves, amulet, and other slots.
- **Hollow Focus** belt type mentioned for stun → **Wing Blast** charge fishing.

### Vendor strategy

- Transcript does **not** emphasize vendor weapon checks (unlike other Monk guides).
- Focus vendor/time investment on **armor upgrades** Acts 1–3 and **+melee skills** Acts 3–4.
- Any talisman works for **Wing Blast**; stronger talisman = more **Wing Blast** damage.

### Important items / bases

| Approx time | Item / base | Notes |
|---:|---|---|
| 00:04:27 | **Talisman** (any) | Required in weapon set 2 for **Wing Blast**. |
| 00:09:25 | Full **armor** pieces | All slots — stack armor, ignore ES/evasion. |
| 00:13:18 | **Hollow Palm Technique** | Keystone — remove quarterstaff afterward. |
| 00:14:10 | **Hollow Focus** belt | Can be **Wing Blast**-stunned for 3 charges. |
| 00:18:32 | **+melee skills** | Gloves, amulet, other gear after Hollow Palm. |
| 00:19:26 | ES/evasion body armor | Act 4 pivot for Hollow Palm scaling. |

---

## Rotation by Phase

### Phase 1: Early Act 1 (before Wing Blast)

```text
Quarterstaff strike → Killing Palm (cull) → Falling Thunder (burst) → repeat
```

With **Frozen Locus**:

```text
Approach pack → Frozen Locus → strike crystal / let enemies hit it → finish with Falling Thunder or Killing Palm
```

With **Frost Bomb** (optional):

```text
Frozen Locus → Frost Bomb → staff strikes (Rage) → Falling Thunder (shock) → repeat
```

### Phase 2: Wind Blast / Wing Blast (late Act 1)

**Packs:**

```text
Wind Blast (daze) → Wing Blast (stun/delete) → Wind Blast → Wing Blast → done
```

**Bosses:**

```text
Wind Blast (build stagger to ~70%) → Wing Blast (3 Power Charges) → Falling Thunder → repeat
```

**If adds spawn:**

```text
Killing Palm / later Devour → refresh charges → Falling Thunder
```

### Phase 3: Devour + Falling Thunder zone clear (late Act 1 – early Act 2)

```text
Wind Blast → Wing Blast (clear pack) → Devour corpses (charges + heal) → Falling Thunder → Pounce forward → repeat
```

Keep **Wind Blast** / **Wing Blast** for bosses even while zones use the dive loop.

### Phase 4: Storm Wave + Siphoning Strike (Act 2+)

**Packs / zones:**

```text
Storm Wave (shock) → Siphoning Strike (extract → charges + shockwave) → Falling Thunder → Devour forward → repeat
```

**Bosses:**

```text
Storm Wave → Siphoning Strike ×2–3 (stack charges) → confirm shock still applied → Storm Wave (damage multiplier) → Falling Thunder
```

**Alternative boss charge refill:**

```text
Wind Blast (stagger) → Wing Blast (instant 3 charges) → Falling Thunder
```

**Hollow Focus belt tech (optional):**

```text
Wing Blast belt (3 charges) → Falling Thunder
```

### Phase 5: Act 3+ boss loop (Perpetual Charge)

```text
Storm Wave → Siphoning Strike ×2–3 → verify shock on target → Storm Wave (if shock reapplied) → Falling Thunder ×multi (Perpetual Charge) → repeat
```

---

## Full Timeline / Step-by-Step Run Guide

### 00:00:00–00:01:05 — Intro and character start

- Build premise: **Falling Thunder** from level 1 through mapping; **Power Charges** made easy; **Martial Artist** ascendancy planned for patch **0.5**.
- Pick **Monk**, grab starting quarterstaff + **Falling Thunder**.
- Add **Killing Palm** as second skill — cull for **Power Charges** that empower **Falling Thunder**.
- Video covers Act 1 → Act 4 interludes → endgame concept; live demo uses **Invoker** until Martial Artist releases.

### 00:01:05–00:02:24 — Clearfell and first supports

- Enter **Clearfell**; basic loop: staff strike → **Killing Palm** → **Falling Thunder** on packs.
- Grab level-1 gem from tiny camp → craft **Frozen Locus** (ice crystal, ~350% attack damage explosion).
- Use **Frozen Locus** when approaching packs; finish with **Falling Thunder** or palm for charges.
- Kill **Devourer** and **Beyrah**: spawn **Frozen Locus** at your feet while holding staff attacks so you do not knockback-jump away.
- Apply **Falling Thunder** for shock (multiplicative damage).
- Devourer drops first support → **Rage** (+30% attack damage on staff, **Falling Thunder**, and locus explosions).

### 00:02:40–00:03:39 — Grell wood, Frost Bomb, Rusted King

- Witch in **Grell wood** drops second support; optional extra skill gem → **Frost Bomb** for elemental exposure.
- Rotation with bomb: locus → frost bomb → staff (**Rage**) → **Falling Thunder** (shock) → more locus/bombs while holding attacks.
- Add **Rapid Attacks** to staff strikes.
- **Rusted King** tip: farm charges on surrounding enemies first; hit through his early damage reduction (~5 seconds), then burst.
- When he spawns adds, **Killing Palm** them for charges and finish quickly.

### 00:03:39–00:06:41 — Wing Blast + Wind Blast revolution

- **Do not** pick a Monk skill for first level-3 gem — take **Wing Blast** from **Druid**.
- Why: primes/stuns delete packs; vs bosses grants **3 Power Charges** every stun.
- Equip **talisman** in **weapon set 2** (power level affects **Wing Blast** damage only).
- Next Monk gem: **Wind Blast** — ranged staff attack that **dazes**, increasing stun buildup.
- Pack loop: **Wind Blast** → **Wing Blast** → repeat.
- Boss loop: build orange stagger bar to ~**70%** (deeper color) → **Wing Blast** → **3 charges** → **Falling Thunder**.
- Move **Rage** + **Rapid Attacks** from staff to **Wind Blast**.
- Add **Brink** (stun buildup) — **Wind Blast** cannot over-stun, so enemies stay primed for **Wing Blast**.
- Add **Impact Shockwave** on heavy stun from **Wind Blast** for clear.
- **Falling Thunder** gets **Elemental Armament** if supports remain.
- **Frozen Locus** and **Frost Bomb** support slots stay empty; drop **Frozen Locus** entirely once this combo works — keep **Frost Bomb** only for exposure until Act 2.

### 00:06:41–00:08:30 — Pounce, Herald, Devour swap

- Third tier-3 gem → **Pounce** for movement (still best area-speed skill; minor cooldown nerf in 0.5).
- Kill **King of the Mist** in **Fraythorn** for first spirit gem context.
- Socket **Herald of Thunder** — all damage going forward stacks shock.
- Optional: **Fist of War** on **Falling Thunder** (ancestral, used once per boss window not spammed).
- After **Executioner**, tier-5 gem enables **Devour** (Wyvern) replacing **Killing Palm**.
- **Devour**: dive forward, cull or eat corpses for charges, **heals** you.
- Support **Devour** with **Thrill of the Kill** (25% damage as lightning on kill, 8 seconds).
- New zone loop: **Wind Blast**/**Wing Blast** clear → **Devour** corpses → **Falling Thunder** → jump forward again.
- Advantage over pure **Wind Blast** clear: always moving **forward**, never knocking back.
- Keep **Wind Blast**/**Wing Blast** for bosses.

### 00:08:30–00:10:41 — Act 1 gear, passives, Count boss

- Gear: **full armor** every slot — not ES, not evasion.
- Passives: skill speed → attack damage → shock → lightning; temporary strength for talisman if needed.
- End Act 1 around **level 14–15**.
- **Count** boss: hit → **Wing Blast** stun → charges → big **Falling Thunder**; repeat when he transforms to wolf form.

### 00:10:41–00:13:12 — Act 2 opens; Storm Wave + Siphoning Strike

- Continue **Devour** + **Falling Thunder** + boss **Wind Blast**/**Wing Blast** until tier-7 gems.
- Craft **Storm Wave** + **Siphoning Strike** — "absolute insane combo."
- **Storm Wave** shocks at range; **Siphoning Strike** melee jump steals shock → **Power Charges** + lightning shockwave → procs **Herald of Thunder** chains.
- Boss pattern: shock → extract ×3 → **Falling Thunder**; repeat or **Wing Blast** stunned boss for instant 3 charges.
- **Storm Wave** supports: **Rage**, **Shock to 100%**.
- **Siphoning Strike** supports: **Rapid Attacks**, **Charge Perfusion**.
- Stop **Frost Bomb**; move **Wing Blast** to **Devour** for faster eat animation between packs.
- Optional: **Mark of Siphoning** on pawns for mana leech — loop is mana-hungry.

### 00:13:12–00:15:27 — Hollow Palm path, Jaman' Rai, ascendancy preview

- Rush passives to **Hollow Palm Technique** — stronger than holding a good quarterstaff.
- Also path: reduced mana cost, ailment chance, elemental damage, shock reapply on consume (grab before **Jaman' Rai**).
- **Jaman' Rai**: **Storm Wave** → extract (1–2 charges with **Charge Perfusion**) → **Falling Thunder** → repeat; trivial with shock reapply node.
- Demo used **Invoker Sentinels**; Martial Artist adds **Way of the Mountain** (stun stacks = **Mountain's Teachings** = 20% more damage + defenses).
- **Hollow Focus** belts can be **Wing Blast**-stunned for 3 charges anytime.

### 00:15:27–00:19:22 — Act 3: supports, sustain, Hollow Palm gear

- First **Jeweler's Orb** → **Perpetual Charge** on **Falling Thunder** (keep 6 charges, multi-cast burst).
- Second **Jeweler's Orb** → **Living Lightning** on **Storm Wave** (creator rejected **Branching Fissures**).
- Kill **Ashen Bach** → +30 spirit; skip **Lingering Illusion** (always have charges).
- Full armor means **Ghost Dance** does nothing yet — use **Clarity** + **Cannibalism** on **Herald of Thunder**.
- **Gorge** on **Devour** for flask sustain from corpses.
- Second ascension: combine **Way of the Mountain** + **Way of the Stone Fist** (or runes / **Hollow Focus** if skipped); +2 max charges.
- Respec mana nodes → lightning damage + penetration; take **Killer Instinct**; shock magnitude node at top.
- **Hollow Palm** live: no weapon, talisman in set 2, **+melee skills** on gloves/amulet.
- **Doryani**: trivial if shock loop maintained.
- **Critical boss tip:** after extracting shock, do another **Storm Wave** if shock did not reapply — shock is a damage multiplier before **Falling Thunder**.

### 00:19:22–00:21:32 — Act 4, defensive pivot, mapping carry

- Start replacing armor focus with **ES/evasion** — boosts **Hollow Palm** (attack speed per evasion, crit per ES on body).
- Passives: ES, evasion, tankiness.
- Swap **Clarity**/**Cannibalism** for **Ghost Dance** (regen-over-time version — creator unsure if strictly better but uses it).
- **Herald of Thunder**: **Elemental Armament** + **Elemental Focus**.
- **Whirling Assault** + Martial Artist ghost copies — cool for bosses, **not needed** for normal clearing or campaign.
- Creator cleared all of Act 4 with **Falling Thunder** combo; viable through mapping to **Arbitrator of Ash** without swapping to **Whirling Assault**.
- Interludes "easily devoured" with **Devour**.
- Guide stops at Act 4; full 0.5 Martial Artist mapping expansion pending patch release.

---

## Practical Reproduction Checklist

### Before starting

- [ ] Roll **Monk** with intent to ascend **Martial Artist** on 0.5 (or **Invoker** as interim).
- [ ] Plan cross-class gem pick: save first level-3 gem for **Wing Blast** (Druid).
- [ ] Keep any talisman for weapon set 2 before **Wing Blast** unlocks.
- [ ] Accept early game is staff-melee until **00:03:47** stun combo comes online.

### Act 1 checklist

- [ ] Socket **Falling Thunder** + **Killing Palm** immediately.
- [ ] Craft **Frozen Locus** from Clearfell camp gem.
- [ ] Add **Rage** from Devourer; **Rapid Attacks** on staff.
- [ ] Optional **Frost Bomb** from Grell wood witch drop.
- [ ] Build charges before **Rusted King**; shock with **Falling Thunder**.
- [ ] Take **Wing Blast** (Druid) as first level-3 gem — equip talisman in set 2.
- [ ] Add **Wind Blast** + **Brink** + **Impact Shockwave**; move **Rage**/**Rapid Attacks** to **Wind Blast**.
- [ ] **Elemental Armament** on **Falling Thunder**; remove **Frozen Locus**.
- [ ] Craft **Pounce** from third tier-3 gem.
- [ ] Socket **Herald of Thunder** after **King of the Mist**.
- [ ] Replace **Killing Palm** with **Devour** + **Thrill of the Kill** after **Executioner**.
- [ ] Wear **full armor** on every slot.
- [ ] Finish Act 1 ~level **14–15** using boss stun → charge → **Falling Thunder**.

### Act 2 checklist

- [ ] Craft **Storm Wave** + **Siphoning Strike** at tier 7.
- [ ] Support **Storm Wave** with **Rage** + **Shock to 100%**.
- [ ] Support **Siphoning Strike** with **Rapid Attacks** + **Charge Perfusion**.
- [ ] Move **Wing Blast** to **Devour**; drop **Frost Bomb**.
- [ ] Path to **Hollow Palm Technique** ASAP.
- [ ] Take shock-reapply-on-consume node before **Jaman' Rai**.
- [ ] Use **Storm Wave** → extract → **Falling Thunder** as default boss loop.

### Act 3 checklist

- [ ] **Perpetual Charge** on **Falling Thunder** (first Jeweler's Orb).
- [ ] **Living Lightning** on **Storm Wave** (second Jeweler's Orb).
- [ ] **Clarity** + **Cannibalism** on **Herald of Thunder**; **Gorge** on **Devour**.
- [ ] Second ascension: **Way of the Mountain** line + **+2 Power Charges**.
- [ ] Respec mana nodes → lightning damage + penetration + shock magnitude.
- [ ] Unequip weapon; enable **Hollow Palm**; stack **+melee skills** on gear.
- [ ] Before **Falling Thunder** on bosses, confirm shock is still applied after extraction.

### Act 4 / Interlude checklist

- [ ] Begin ES/evasion gear on body armor for **Hollow Palm** scaling.
- [ ] Replace **Clarity**/**Cannibalism** with **Ghost Dance**.
- [ ] Add **Elemental Armament** + **Elemental Focus** to **Herald of Thunder**.
- [ ] Optional: **Whirling Assault** for Martial Artist boss bursts — skip if pacing matters.
- [ ] Carry **Falling Thunder** shock loop through campaign end and into maps.
- [ ] Interludes: use **Devour** forward momentum — no special tech required.

---

## Boss / Key Fight Notes

| Timestamp | Fight / event | Notes |
|---:|---|---|
| 00:02:03 | **Devourer** / **Beyrah** | **Frozen Locus** at feet while attacking; **Falling Thunder** for shock; drops **Rage**. |
| 00:03:17 | **Rusted King** | Pre-build **Power Charges** on nearby mobs; wait out ~5s damage reduction; palm adds for charges. |
| 00:07:06 | **King of the Mist** (**Fraythorn**) | First spirit gem context; socket **Herald of Thunder** after. |
| 00:07:44 | **Executioner** | Drops tier-5 gem tier — enables **Devour** swap. |
| 00:10:17 | **Count** (Act 1 finale) | **Wind Blast** stagger → **Wing Blast** → **Falling Thunder**; repeat in wolf form. Not a real fight — an execution. |
| 00:13:56 | **Jaman' Rai** | Shock reapply passive makes this trivial; **Storm Wave** extract loop. Demo used Invoker, not Martial Artist. |
| 00:16:17 | **Ashen Bach** | +30 spirit; skip **Lingering Illusion**. |
| 00:18:39 | **Doryani** | "Easiest fight ever" with maintained shock + **Falling Thunder** bursts. |
| 00:18:51 | General boss rule | After **Siphoning Strike**, verify shock remains before **Falling Thunder**; extra **Storm Wave** if not reapplied. |
| 00:20:48 | **Arbitrator of Ash** (mapping) | Build carries without **Whirling Assault** swap per creator. |

---

## Common Mistakes to Avoid

1. **Picking a Monk level-3 gem before Wing Blast**  
   The creator explicitly delays Monk tier-3 for **Wing Blast** — it defines Act 1 bossing and charge generation.

2. **Forgetting talisman in weapon set 2**  
   **Wing Blast** will not work without it; any talisman suffices early.

3. **Heavy-stunning with Wind Blast**  
   **Wind Blast** primes stun but cannot over-stun — that is intentional so **Wing Blast** always has a target.

4. **Keeping Frozen Locus too long**  
   Drop it once **Wind Blast** / **Wing Blast** clear is stable; exposure-only **Frost Bomb** lasts until Act 2 shock loop.

5. **Falling Thunder without shock on bosses**  
   After shock extraction, confirm shock is still on the target (or reapply with **Storm Wave**) before bursting — charges scale damage, shock multiplies it.

6. **Stacking evasion/ES before Act 4**  
   Acts 1–3 want **full armor**; premature ES/evasion slows the simple armor-stacking defense plan.

7. **Mandatory Whirling Assault**  
   Creator cleared Act 4 and mapping with the **Falling Thunder** combo alone — **Whirling Assault** is optional boss flair.

8. **Branching Fissures on Storm Wave**  
   Creator tested it in Act 3 and switched to **Living Lightning** for better shock targets.

---

## Minimal “Same Build” Version

```text
Early Act 1:
Falling Thunder + Killing Palm + Frozen Locus → Rage + Rapid Attacks on staff

Late Act 1:
Wing Blast (Druid, talisman set 2) + Wind Blast (Rage, Brink, Impact Shockwave, Rapid Attacks)
Falling Thunder (Elemental Armament) + Herald of Thunder
Devour replaces Killing Palm (Thrill of the Kill)
Pounce for movement; full armor gear

Core switch (Act 2 tier 7):
Storm Wave (Rage, Shock to 100%, later Living Lightning)
Siphoning Strike (Rapid Attacks, Charge Perfusion)
Path to Hollow Palm Technique — unequip weapon
Zone: Storm Wave → Siphoning Strike → Falling Thunder → Devour forward
Boss: extract shocks for charges OR Wing Blast stunned target → Falling Thunder

Act 3:
Perpetual Charge on Falling Thunder
Clarity + Cannibalism on Herald; Gorge on Devour
+melee skills on gloves/amulet

Act 4:
ES/evasion body for Hollow Palm; Ghost Dance; Elemental Focus on Herald
Optional Whirling Assault for Martial Artist bosses only

Boss rotation:
Storm Wave → Siphoning Strike ×2–3 → confirm shock → Storm Wave (if needed) → Falling Thunder (multi with Perpetual Charge)

Gear:
Acts 1–3: full armor
Act 4+: ES/evasion body + Hollow Palm scaling
Always: talisman in weapon set 2
```

---

## Recommended Pace Targets

This video is a **22-minute build guide**, not a full campaign VOD. Targets below map **video topic timestamps** to when you should hit the same build state in your own run. "Your target" columns are realistic in-game ranges, not video runtime.

| Segment | Target from transcript | Your target |
|---|---|---|
| Start + Clearfell gems | 00:00:46–00:01:22 | First 15–25 min of play |
| Devourer + Rage | 00:02:24 | Act 1 first third |
| Wing Blast + Wind Blast online | 00:03:47–00:05:45 | Act 1 mid (~level 10–12) |
| Devour + Herald swap | 00:07:21–00:08:03 | Late Act 1 |
| Act 1 complete | 00:10:17 | Level 14–15, pre-Act 2 |
| Storm Wave + Siphoning Strike | 00:10:54 | Early Act 2 (tier 7) |
| Hollow Palm taken | 00:13:12 | Mid Act 2 |
| Jaman' Rai ready | 00:13:56 | Late Act 2 |
| Act 3 support upgrades | 00:15:33 | Early Act 3 |
| Hollow Palm gear finalized | 00:18:24 | Mid Act 3 |
| Act 4 defensive pivot | 00:19:26 | Act 4 start |
| Campaign carry confirmed | 00:20:48 | Act 4 / mapping entry |

---

## Final Notes

Copy these **seven power spikes** for the same feel as the video:

1. **Frozen Locus** bridge → immediate pack control (temporary).
2. **Wing Blast** + **Wind Blast** stun engine — 3 boss charges per stun.
3. **Devour** + **Falling Thunder** forward-clear loop + **Herald of Thunder**.
4. **Storm Wave** + **Siphoning Strike** shock extraction (permanent core).
5. **Hollow Palm Technique** — drop the weapon, spike damage.
6. **Perpetual Charge** + **Living Lightning** — multi-cast **Falling Thunder** nukes.
7. Act 4 **ES/evasion** + **Ghost Dance** — scale Hollow Palm without dying.

The final winning pattern is simple: **shock everything, steal shocks for Power Charges, then delete targets with chained Falling Thunder bursts** — using **Wing Blast** only when you need instant charges or **Devour** when you need to move forward through corpses.
