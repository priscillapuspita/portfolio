# CV Content Alignment Design

## Intent

Align the live portfolio's written content with Priscilla Puspita's CV while preserving the current visual design, layout, styling, media, PDF links, JavaScript behavior, and overall HTML structure.

## Goals

- Apply the approved hero, experience, project, education, skills, language, contact, title, and metadata text updates.
- Reorder existing experience cards newest-first as specified.
- Add a short Projects section for the evidenced live project at priscillatells.com.
- Preserve all existing screenshots, event images, thesis images, galleries, and PDF targets.
- Produce a complete updated `index.html`, commit it to `main`, publish it through GitHub Pages, and verify the deployed page.
- Report any date conflicts found during a full-page scan rather than silently changing unspecified dates.

## Explicit exclusions

- Do not add the proposed Calvin Klein / PVH experience.
- Do not add the proposed GoTo Group experience.
- Do not add the proposed BA International Relations education entry.

These entries were removed from scope because the portfolio does not contain evidence or outcomes to support them.

## Constraints

- Text-only changes, except for adding HTML blocks that reuse existing structural patterns for the Projects section.
- No CSS redesign, new visual system, new imagery, changed image paths, altered PDF URLs, or JavaScript changes.
- Keep the two Techpanda screenshots, every SkyTeam image, all Jajanan images, all Occam article links and event images, and all thesis images.
- Preserve the January 2026 in-flight caption.

## Selected approach

Surgically edit the existing `index.html`. Reuse the current experience-card and section conventions, minimizing diff size and avoiding regeneration of untouched markup.

## Alternatives considered

- Regenerate the page from the content brief: rejected because it risks changing structure, styling, links, media, and behavior.
- Add the new CV entries without evidence: rejected at the user's direction.

## Content changes

- Update the document title, hero tagline, and hero description.
- Reorder existing experience cards to Techpanda, SkyTeam, Jajanan, and Occam.
- Replace the approved experience titles, labels, intros, bullets, and corrected captions/link text.
- Add the linked priscillatells.com Projects section after Experience.
- Update the MA date/title wording while preserving thesis details, images, and quantitative finding.
- Remove OpenClaw, Google Ads, and SEO references; ensure all required tools are present.
- Update English and Dutch proficiency text.
- Replace the contact pitch with “Let's work together.” while keeping all contact details.

## Verification

- Run content assertions for every requested text string and excluded term.
- Compare all image, video, and PDF references before and after to ensure none are lost or changed unintentionally.
- Validate HTML structure and run `git diff --check`.
- Scan all visible years/date ranges and report conflicts.
- Inspect the rendered live page and core galleries after GitHub Pages deploys.
