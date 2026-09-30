# Report template

Hand this folder to Claude with: **"Make a report in this template about &lt;topic / data&gt;."**
Claude: read this file and `template.html`, then follow the rules below exactly.

## Files

| File | Purpose |
|---|---|
| `template.html` | The design: CSS plus one example of every component, with `[PLACEHOLDERS]`. |
| `html2pdf.py` | Prints the HTML to an A4 PDF with headless Microsoft Edge: `python html2pdf.py report.html report.pdf` |

Example of a finished report in this style: `pcm/bench/PCM-Scenario-Results.pdf`, built by `pcm/bench/make_scenario_report.py`.

## Rules for the content

1. **Plain language.** Write for a reader who does not know the jargon. Short sentences. Explain every term the first time.
2. **The answer comes first.** Page 1 is the short answer: one card per thing being judged, each with a verdict chip, one headline number, and one sentence explaining why.
3. **Every page is complete.** One `<section class="page">` = one A4 page. Nothing continues onto the next page. If a page overflows, cut content. Never shrink the font.
4. **Make the effects obvious.** Use color with a meaning: blue = better, red = worse, gray = within noise, dashed = not applicable. Every number is also written as text, so color never carries meaning alone.
5. **Show the noise.** Say how much results move by chance, and fade or gray out anything within that noise.
6. **Real examples.** Each detail page shows 1–3 real before/after examples taken from the actual data, never invented ones.
7. **Numbers come from data.** Generate the HTML from the results file with a small script, never by typing numbers by hand. That keeps the report from drifting away from the data.
8. **Honest limits.** The last page lists the recommendations, anything found or fixed along the way, and the limits of the test.
9. **Authorship note.** End with the "About this report" note: the text was written with Claude's help, and the experiments were really run.

## Page order

1. Cover: headline, lede, verdict cards, "how to read the numbers".
2. How we tested: 4-step flow, table of cases, definitions.
3. The whole picture: colored grid of everything against everything.
4. One detail page per thing judged: chart, examples.
5. What to do: recommendations, findings, limits, authorship note.

Drop pages that don't apply. Keep the order.

## Components (all in `template.html`)

`cards` (verdict chips: `on` / `off` / `limited`), `howto`, `flow`, `scen` table, `two` + `note-box`, `grid` heatmap, `chart` (diverging bars, with the position formula in a comment), `versus` panels, `example` card (answer colors: `ok` / `bad` / `good` / `gold`), `recs`, `found`, `limits`, `authorship`.

Persian or other right-to-left text: add `dir="rtl"` to the element. It switches to the Vazirmatn font.

## Check before handing over

- Render the PDF, then view every page as an image (for example with PyMuPDF). Check that the page count matches the number of sections, and look for clipped labels or overflow.
- If the PDF is open in a viewer, Windows locks it: write to a new filename instead.
