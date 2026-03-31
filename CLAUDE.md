# Project Rules

## Session Bootstrap                                                                                
                                                            
  Before writing any report script:
  1. Read `Competitive Analysis Newsela Prompt` in full
  2. Copy `generate_noredink_pdf.py` as your starting file
  3. Do not deviate from the section structure, helper signatures, or color palette
  4. Do not add additional content in order to add page count. If the report ends up being shorter, that is okay. 

## Accessibility — WCAG 2.1 AA Color Contrast (NON-NEGOTIABLE)

All generated documents (PDFs, reports, HTML) MUST meet WCAG 2.1 AA minimum contrast ratios **before** writing or running any code. Do not produce a first draft and fix it after feedback.

### Rules

- **Normal text (< 18pt regular, < 14pt bold):** minimum 4.5:1 contrast ratio against its background.
- **Large text (≥ 18pt regular or ≥ 14pt bold):** minimum 3:1 contrast ratio against its background.
- **UI components / decorative elements:** 3:1 minimum.

### ReportLab-specific enforcement

- **Never put a `Paragraph` with a colored `textColor` style inside a table cell that relies on `TEXTCOLOR` in `TableStyle` to set the color.** `TableStyle TEXTCOLOR` only affects plain strings — it does NOT override a `Paragraph`'s own `textColor`. Always use a dedicated paragraph style with the correct `textColor` for table header and body cells.
- All table cells must be `Paragraph` objects (not plain strings) so text wraps and styles apply correctly.
- Define a `table_header_style` (white text) and `table_cell_style` (dark text) and use them consistently.

### Pre-approved palette (verified contrast ratios on white background)

| Color name    | Hex       | Contrast on white | Safe for         |
|---------------|-----------|-------------------|------------------|
| BRAND_BLUE    | #1E3A8A   | ~13:1             | All text sizes   |
| DARK_TEAL     | #0369A1   | ~7.2:1            | All text sizes   |
| LUNA_PURPLE   | #6D28D9   | ~7.6:1            | All text sizes   |
| DARK_GRAY     | #334155   | ~10.4:1           | All text sizes   |
| ACCENT_GREEN  | #065F46   | ~10.8:1           | All text sizes   |
| SLATE_600     | #475569   | ~7.2:1            | All text sizes   |
| BRAND_TEAL    | #0EA5E9   | ~3.3:1            | Decorative / backgrounds ONLY — never for body text |

### Checklist before generating any PDF

- [ ] Every text color + background combination has been verified against the ratios above
- [ ] No `Paragraph` object relies on a `TableStyle TEXTCOLOR` command to be readable
- [ ] All table cells use `Paragraph` objects, not plain strings
