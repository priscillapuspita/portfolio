# CV Content Alignment Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Align the portfolio's written content with the approved CV brief, publish it to GitHub Pages, and provide a complete replacement `index.html`.

**Architecture:** Make a surgical edit to the existing single-file static site. Preserve all CSS, JavaScript, media paths, PDF targets, and gallery behavior; use the existing HTML conventions for the linked Projects section and reorder only the existing experience cards.

**Tech Stack:** Static HTML/CSS/JavaScript, Python standard library assertions, Git, GitHub Pages

**Spec:** `docs/superpowers/specs/2026-10-28-cv-content-alignment-design.md`

## Global Constraints

- Do not add Calvin Klein / PVH, GoTo Group, or BA International Relations.
- Keep every existing image, video, PDF target, gallery, and script reference unchanged.
- Do not change CSS, JavaScript behavior, or visual design.
- Keep the Techpanda screenshots and all SkyTeam, Jajanan, Occam, and thesis media.
- Keep the January 2026 in-flight caption.
- Report date conflicts rather than silently changing dates outside the approved brief.

## Review Focus

- Experience order must be Techpanda, SkyTeam, Jajanan, Occam, with no excluded experience cards added.
- Media and PDF URL multisets must remain exactly unchanged before and after the edit.
- Removed terms (`OpenClaw`, `Google Ads`, and `SEO`) must not remain anywhere in visible page content.
- Required tools must appear in both the top tool chips or the detailed skills area where appropriate, without changing layout styles.
- Date scans must distinguish approved content dates from filenames and copyright text and report any remaining visible conflicts.

---

### Task 1: Align hero, experience, projects, and education content

**Files:**
- Modify: `index.html`

**Interfaces:**
- Consumes: Exact approved copy and exclusions from the spec.
- Produces: Updated static page content with preserved DOM conventions and media blocks.

- [ ] **Step 1: Run failing content assertions**

Run a Python standard-library assertion script against `index.html` covering the new title, hero copy, experience order, approved labels and bullets, newsletter correction, Ramadan link text, priscillatells.com project, MA thesis title, and explicit exclusions.

Expected: FAIL because the approved text and order are not yet present.

- [ ] **Step 2: Edit the hero and page title**

Replace only the `<title>`, hero tagline, and hero description with the approved exact copy.

- [ ] **Step 3: Reorder and update experience cards**

Move the existing Techpanda card before SkyTeam; keep SkyTeam, Jajanan, and Occam after it. Replace titles, labels, intros, bullets, and corrected captions/link text exactly as approved while retaining every media and article block.

- [ ] **Step 4: Add the evidenced Projects section**

Insert a short section after Experience for `priscillatells.com`, linked to `https://priscillatells.com`, using existing section/card conventions and no new CSS.

- [ ] **Step 5: Update education copy**

Keep the MA card, grade, thesis narrative, three thesis images, and `195.6` versus `14.1` finding; change the visible thesis title to `NASA and SpaceX Science Communication on Instagram` and preserve the approved MA dates.

- [ ] **Step 6: Run content assertions**

Expected: PASS for all requested content and exclusion checks.

- [ ] **Step 7: Commit the content structure milestone**

```bash
git add index.html docs/superpowers/specs/2026-10-28-cv-content-alignment-design.md docs/superpowers/plans/2026-10-28-cv-content-alignment.md
git commit -m "Align portfolio experience with CV"
```

### Task 2: Align skills, languages, contact text, and verify invariants

**Files:**
- Modify: `index.html`

**Interfaces:**
- Consumes: Updated page from Task 1.
- Produces: Final CV-aligned `index.html` with verified references and dates.

- [ ] **Step 1: Run failing skills and contact assertions**

Assert that required tools are present; removed terms are absent; English, Indonesian, and Dutch levels match the brief; and the contact pitch is exactly `Let's work together.`

Expected: FAIL on the current skills, language, and contact copy.

- [ ] **Step 2: Update top tool chips**

Remove `OpenClaw`, `Google Ads`, and `SEO Copywriting`; ensure the required set includes HubSpot, Meltwater, Hootsuite, ClickUp, WordPress, Google Analytics, Canva, Photoshop, Premiere Pro, CapCut, Microsoft Office, Notion, ChatGPT, Claude, and RStudio while preserving each chip's existing inline style.

- [ ] **Step 3: Update detailed skills and languages**

Remove OpenClaw everywhere, replace superseded AI naming with ChatGPT and Claude, add Microsoft Office where appropriate, and apply the exact English and Dutch proficiency copy.

- [ ] **Step 4: Update contact pitch**

Replace the current pitch text with `Let's work together.` while retaining Lelystad, email, phone, and LinkedIn markup and targets.

- [ ] **Step 5: Verify media and link invariants**

Compare pre-edit and post-edit multisets of `src` values and PDF `href` values. Expected: identical, except for the newly added external `https://priscillatells.com` link.

- [ ] **Step 6: Validate HTML and repository diff**

Run HTML parser checks, `git diff --check`, and full content assertions. Expected: no structural errors, whitespace errors, missing references, or failed assertions.

- [ ] **Step 7: Scan visible dates**

List every visible year/date string, compare it with the approved chronology, and record any conflicts for the final report without changing unapproved content.

- [ ] **Step 8: Commit the final content milestone**

```bash
git add index.html
git commit -m "Update portfolio skills and profile copy"
```

### Task 3: Deliver, publish, and verify the live page

**Files:**
- Create: `/Users/priscilla/Documents/Codex/2026-10-22/i-x20/outputs/index.html`

**Interfaces:**
- Consumes: Verified final `index.html` from Task 2.
- Produces: Downloadable replacement file and deployed GitHub Pages site.

- [ ] **Step 1: Copy the complete verified file to outputs**

Copy the repository `index.html` byte-for-byte to the user-facing outputs directory and verify matching SHA-256 hashes.

- [ ] **Step 2: Push `main`**

Run `git push origin main`. Expected: both commits pushed with a clean `main...origin/main` status.

- [ ] **Step 3: Wait for GitHub Pages deployment**

Watch the Pages workflow for the pushed head commit. Expected: build and deployment complete successfully.

- [ ] **Step 4: Verify the deployed HTML and assets**

Fetch the live page with a cache-busting query; run the same content assertions against it; confirm key images and PDFs return HTTP 200.

- [ ] **Step 5: Inspect the rendered page**

Open the live URL, inspect the new order and Projects section, and exercise representative lightboxes and links without modifying external content.

- [ ] **Step 6: Report delivery**

Provide the downloadable complete `index.html`, the live URL, commit hashes, every text change grouped by section, deployment verification evidence, and the date-conflict report.
