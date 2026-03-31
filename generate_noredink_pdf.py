"""
Generate NoRedInk_Overview.pdf — Competitive Intelligence Report
Style matches Newsela Writing report format with NoRedInk brand colors.
"""

import os
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor, white, black
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, KeepTogether
)
from reportlab.platypus import Image
from reportlab.lib import colors

# ── Palette ──────────────────────────────────────────────────────────────────
NAVY   = HexColor("#1B3A6B")
RED    = HexColor("#E8274B")
LTGRAY = HexColor("#F4F6F8")
MGRAY  = HexColor("#D0D5DD")
DKGRAY = HexColor("#344054")
AMBER  = HexColor("#FFF8E1")
HINT   = HexColor("#98A2B3")
SUBDUE = HexColor("#667085")
PINKBG = HexColor("#FFF0F3")

BASE = os.path.dirname(os.path.abspath(__file__))
OUT  = os.path.join(BASE, "NoRedInk_Overview.pdf")

# ── Paragraph styles ──────────────────────────────────────────────────────────
body_style = ParagraphStyle(
    "body", fontName="Helvetica", fontSize=9.5, textColor=DKGRAY,
    leading=14, alignment=TA_JUSTIFY, spaceAfter=6
)
bullet_style = ParagraphStyle(
    "bullet", fontName="Helvetica", fontSize=9.5, textColor=DKGRAY,
    leading=14, leftIndent=12, spaceAfter=4
)
label_style = ParagraphStyle(
    "label", fontName="Helvetica-Bold", fontSize=8.5, textColor=RED,
    leading=13, spaceAfter=3, spaceBefore=8
)
caption_style = ParagraphStyle(
    "caption", fontName="Helvetica-Oblique", fontSize=8, textColor=SUBDUE,
    leading=11, alignment=TA_CENTER, spaceAfter=6
)
footer_style = ParagraphStyle(
    "footer", fontName="Helvetica", fontSize=7.5, textColor=HINT,
    leading=10, alignment=TA_CENTER
)
title_main_style = ParagraphStyle(
    "title_main", fontName="Helvetica-Bold", fontSize=22, textColor=NAVY,
    leading=26, spaceAfter=4
)
title_sub_style = ParagraphStyle(
    "title_sub", fontName="Helvetica", fontSize=10, textColor=RED,
    leading=14, spaceAfter=6
)
th_style = ParagraphStyle(
    "th", fontName="Helvetica-Bold", fontSize=9, textColor=white,
    leading=12, alignment=TA_LEFT
)
td_style = ParagraphStyle(
    "td", fontName="Helvetica", fontSize=9, textColor=DKGRAY,
    leading=12, alignment=TA_LEFT
)
td_center_style = ParagraphStyle(
    "td_center", fontName="Helvetica", fontSize=9, textColor=DKGRAY,
    leading=12, alignment=TA_CENTER
)
td_bold_red_style = ParagraphStyle(
    "td_bold_red", fontName="Helvetica-Bold", fontSize=9, textColor=RED,
    leading=12, alignment=TA_LEFT
)
td_bold_style = ParagraphStyle(
    "td_bold", fontName="Helvetica-Bold", fontSize=9, textColor=DKGRAY,
    leading=12, alignment=TA_LEFT
)

W = 6.3 * inch  # usable width

# ── Section header helper ─────────────────────────────────────────────────────
def section_header(title):
    """Returns a navy banner Table with white bold text."""
    t = Table([[Paragraph(title, ParagraphStyle(
        "sh", fontName="Helvetica-Bold", fontSize=11, textColor=white,
        leading=14, alignment=TA_LEFT
    ))]],
        colWidths=[W]
    )
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), NAVY),
        ("TOPPADDING",    (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("LEFTPADDING",   (0, 0), (-1, -1), 8),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 8),
    ]))
    return t

# ── Callout box helper ────────────────────────────────────────────────────────
def callout(text, label="UNLIKE NEWSELA"):
    """Amber callout box with red left accent bar and label."""
    accent_w = 0.12 * inch
    body_w   = W - accent_w

    label_para = Paragraph(
        "<b>{} {}</b>".format("★" if "UNIQUE" in label else "▌", label),
        ParagraphStyle("cl", fontName="Helvetica-Bold", fontSize=8,
                       textColor=RED, leading=11)
    )
    body_para = Paragraph(
        text,
        ParagraphStyle("cb", fontName="Helvetica", fontSize=8.5,
                       textColor=DKGRAY, leading=12)
    )

    inner = Table(
        [[label_para], [body_para]],
        colWidths=[body_w - 12]
    )
    inner.setStyle(TableStyle([
        ("TOPPADDING",    (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
        ("LEFTPADDING",   (0, 0), (-1, -1), 6),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 6),
        ("BACKGROUND",    (0, 0), (-1, -1), AMBER),
    ]))

    outer = Table(
        [["", inner]],
        colWidths=[accent_w, body_w]
    )
    outer.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (0, -1), RED),
        ("BACKGROUND",    (1, 0), (1, -1), AMBER),
        ("TOPPADDING",    (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("LEFTPADDING",   (0, 0), (0, -1), 0),
        ("RIGHTPADDING",  (0, 0), (0, -1), 0),
        ("LEFTPADDING",   (1, 0), (1, -1), 0),
        ("RIGHTPADDING",  (1, 0), (1, -1), 4),
        ("GRID",          (0, 0), (-1, -1), 0.3, MGRAY),
        ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
    ]))
    return outer

# ── Image helper ──────────────────────────────────────────────────────────────
def img_block(filename, w, h, caption_text):
    """Returns list of flowables: [image_table, caption] or [caption] if missing."""
    path = os.path.join(BASE, filename)
    items = []
    if os.path.exists(path):
        img = Image(path, width=w, height=h)
        # Center image in a full-width table cell
        cell_table = Table([[img]], colWidths=[W])
        cell_table.setStyle(TableStyle([
            ("ALIGN",         (0, 0), (-1, -1), "CENTER"),
            ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
            ("TOPPADDING",    (0, 0), (-1, -1), 4),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 2),
            ("LEFTPADDING",   (0, 0), (-1, -1), 0),
            ("RIGHTPADDING",  (0, 0), (-1, -1), 0),
        ]))
        items.append(cell_table)
    items.append(Paragraph(caption_text, caption_style))
    return items

# ── Build story ───────────────────────────────────────────────────────────────
def build():
    doc = SimpleDocTemplate(
        OUT,
        pagesize=letter,
        leftMargin=0.85 * inch,
        rightMargin=0.85 * inch,
        topMargin=0.75 * inch,
        bottomMargin=0.75 * inch,
    )

    story = []

    # ── TITLE BLOCK ───────────────────────────────────────────────────────────
    story.append(Paragraph("NoRedInk", title_main_style))
    story.append(Paragraph(
        "Writing + Grammar Platform for Grades 3\u201312  \u00b7  Product Overview  \u00b7  March 2026",
        title_sub_style
    ))
    story.append(HRFlowable(width=W, thickness=1.5, color=RED, spaceAfter=10))

    # ── WHAT IT IS ────────────────────────────────────────────────────────────
    story.append(section_header("WHAT IT IS"))
    story.append(Spacer(1, 6))

    story.append(Paragraph(
        "NoRedInk is a K-12 writing and grammar platform covering grades 3\u201312. Originally built around "
        "grammar skill mastery, it has evolved into a full writing composition suite featuring an "
        "<b>AI-powered Grading Assistant</b> that scores student essays after submission. It offers a "
        "<b>free tier</b> for individual teachers and a <b>Premium school/district license</b> that "
        "unlocks 1,000+ skills, 2,000+ prompts, AI grading, and LMS integrations.",
        body_style
    ))
    story.append(Spacer(1, 4))

    # Facts table
    facts_data = [
        [Paragraph("<b>URL</b>", th_style),
         Paragraph("www.noredink.com", td_style)],
        [Paragraph("<b>AI Feature</b>", th_style),
         Paragraph("Grading Assistant \u2014 post-submission scoring + comments (Premium)", td_style)],
        [Paragraph("<b>Grades</b>", th_style),
         Paragraph("3\u201312", td_style)],
        [Paragraph("<b>Free Tier</b>", th_style),
         Paragraph("Yes \u2014 individual teacher, limited content, no AI grading", td_style)],
        [Paragraph("<b>Premium</b>", th_style),
         Paragraph("School/district license \u00b7 sales-led \u00b7 per-student pricing", td_style)],
        [Paragraph("<b>Login options</b>", th_style),
         Paragraph("Username/password \u00b7 Google \u00b7 Clever \u00b7 ClassLink", td_style)],
        [Paragraph("<b>Key stats</b>", th_style),
         Paragraph("\u221240% teacher grading time \u00b7 +6 pts ACT English \u00b7 +136% top-tier student performance", td_style)],
    ]
    facts_table = Table(facts_data, colWidths=[1.4 * inch, 4.9 * inch])
    facts_ts = TableStyle([
        ("GRID",          (0, 0), (-1, -1), 0.5, MGRAY),
        ("TOPPADDING",    (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("LEFTPADDING",   (0, 0), (-1, -1), 7),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 7),
        ("VALIGN",        (0, 0), (-1, -1), "TOP"),
    ])
    for i in range(len(facts_data)):
        bg = LTGRAY if i % 2 == 0 else white
        facts_ts.add("BACKGROUND", (0, i), (0, i), NAVY)
        facts_ts.add("BACKGROUND", (1, i), (1, i), bg)
    facts_table.setStyle(facts_ts)
    story.append(facts_table)
    story.append(Spacer(1, 8))

    story.append(callout(
        "NoRedInk offers a <b>free tier</b> for individual teachers \u2014 no school purchase required. "
        "Newsela Writing requires a school/district license.",
        label="UNLIKE NEWSELA"
    ))
    story.append(Spacer(1, 8))

    story += img_block("01_login_page.png", 6.3 * inch, 3.69 * inch,
                       "NoRedInk login page \u2014 Google, Clever, ClassLink, and username/password options")
    story.append(Spacer(1, 10))

    # ── HOW IT WORKS ──────────────────────────────────────────────────────────
    story.append(section_header("HOW IT WORKS"))
    story.append(Spacer(1, 6))

    story.append(Paragraph("<b>Assignment types</b>", label_style))
    assignment_types = [
        ("<b>Quick Write</b>",
         "Respond to a prompt with optional sources and rubric items. 2,000+ prompts (Premium)."),
        ("<b>Guided Short Response</b>",
         "Draft a paragraph with sentence-by-sentence support and scaffolding."),
        ("<b>Guided Essay</b>",
         "Draft a full essay with pre-built sections, genre tutorials, tips, and models."),
        ("<b>Practice</b>",
         "Adaptive mastery exercises across 10 skill categories (grammar + writing). 1,000+ skills Premium. "
         "Rule-based mastery: 2 correct in a row to advance; wrong answers unlock inline hint lessons."),
        ("<b>Assessment</b>",
         "Four types: Planning Diagnostic (semester baseline), Unit Diagnostic (pre/post per unit), "
         "Quiz (graded post-unit), Passage Quiz (grammar in multi-paragraph context). Premium gating for benchmarks."),
    ]
    for bold_name, desc in assignment_types:
        story.append(Paragraph(
            "\u2022 {} \u2014 {}".format(bold_name, desc), bullet_style
        ))
    story.append(Spacer(1, 6))

    story.append(callout(
        "1,000+ grammar skill exercises are built into the same platform as writing. "
        "Newsela Writing does not include grammar instruction.",
        label="UNIQUE TO NOREDINK"
    ))
    story.append(Spacer(1, 8))

    story.append(Paragraph("<b>Student Guided Essay workflow</b>", label_style))
    workflow_bullets = [
        "Genre tutorial teaches argumentative/expository concepts before writing begins",
        "Student reads the full rubric (6 criteria, each with description + \u201cView example\u201d button) before writing",
        "Writing area is pre-structured: Title \u2192 Introduction \u2192 Body Paragraphs \u2192 Counterargument \u2192 Conclusion",
        "Each section opens context-sensitive help: color-coded components (Hook/Bridge/Thesis), 8 tips carousel, examples",
        "Source texts embedded in left panel \u2014 students can highlight and annotate with notes",
        "Student submits; AI Grading Assistant scores the essay and generates comments (Premium)",
    ]
    for b in workflow_bullets:
        story.append(Paragraph("\u2022 " + b, bullet_style))
    story.append(Spacer(1, 6))

    story.append(callout(
        "Essay is pre-structured into labeled sections before the student begins writing. "
        "Newsela Writing uses a free-form text editor.",
        label="UNLIKE NEWSELA"
    ))
    story.append(Spacer(1, 8))

    story += img_block("ai_test_02_student_editor.png", 6.3 * inch, 3.69 * inch,
                       "Student writing editor \u2014 source texts and scaffolding on left, pre-built essay sections on right")
    story.append(Spacer(1, 6))
    story += img_block("ai_test_03_writing_area.png", 6.3 * inch, 3.69 * inch,
                       "Section-level scaffolding \u2014 Hook/Bridge/Thesis components and tips visible while student writes")
    story.append(Spacer(1, 10))

    # ── AI GRADING ASSISTANT ──────────────────────────────────────────────────
    story.append(section_header("AI GRADING ASSISTANT"))
    story.append(Spacer(1, 6))

    story.append(Paragraph(
        "Unlike real-time feedback tools, NoRedInk\u2019s AI scores essays <b>after submission</b>. "
        "It scores each of 6 rubric criteria on a 1\u20134 scale, adds per-criterion comments, generates "
        "a multi-paragraph general comment, and outputs a total percentage score. Teachers can override "
        "any score, request revisions, and rate AI quality (\U0001f44d/\U0001f44e).",
        body_style
    ))
    story.append(Spacer(1, 6))

    story.append(callout(
        "Feedback arrives <b>after the student submits</b> with ~5 minutes latency. Newsela\u2019s Luna AI "
        "provides real-time sentence-level feedback <b>during writing</b> with no submission required.",
        label="UNLIKE NEWSELA"
    ))
    story.append(Spacer(1, 8))

    # Centered portrait image
    portrait_path = os.path.join(BASE, "ai_test_01_assign_wild_animals.png")
    if os.path.exists(portrait_path):
        portrait_img = Image(portrait_path, width=2.5 * inch, height=3.5 * inch)
        portrait_table = Table([[portrait_img]], colWidths=[W])
        portrait_table.setStyle(TableStyle([
            ("ALIGN",         (0, 0), (-1, -1), "CENTER"),
            ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
            ("TOPPADDING",    (0, 0), (-1, -1), 4),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 2),
        ]))
        story.append(portrait_table)
    story.append(Paragraph(
        "Assignment creation \u2014 AI Grading Assistant enabled, 6 rubric criteria, 4 source texts",
        caption_style
    ))
    story.append(Spacer(1, 8))

    # Rubric table
    rubric_header = [
        Paragraph("Rubric Criterion (Argumentative)", th_style),
        Paragraph("Scale", th_style),
    ]
    rubric_rows = [
        ("Thesis statement is a debatable opinion", "1\u20134"),
        ("Each topic sentence is a claim that supports the thesis", "1\u20134"),
        ("Each piece of evidence is a fact that supports the claim", "1\u20134"),
        ("Reasoning connects the evidence to the claim", "1\u20134"),
        ("Counterargument paragraph presents an opposing argument and defends thesis", "1\u20134"),
        ("Conclusion restates argument and explains why readers should care", "1\u20134"),
    ]
    rubric_data = [rubric_header] + [
        [Paragraph(r[0], td_style), Paragraph(r[1], td_center_style)]
        for r in rubric_rows
    ]
    rubric_table = Table(rubric_data, colWidths=[5.3 * inch, 1.0 * inch])
    rubric_ts = TableStyle([
        ("BACKGROUND",    (0, 0), (-1, 0), NAVY),
        ("GRID",          (0, 0), (-1, -1), 0.5, MGRAY),
        ("TOPPADDING",    (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("LEFTPADDING",   (0, 0), (-1, -1), 7),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 7),
        ("VALIGN",        (0, 0), (-1, -1), "TOP"),
    ])
    for i in range(1, len(rubric_data)):
        bg = white if i % 2 == 1 else LTGRAY
        rubric_ts.add("BACKGROUND", (0, i), (-1, i), bg)
    rubric_table.setStyle(rubric_ts)
    story.append(rubric_table)
    story.append(Spacer(1, 8))

    story.append(Paragraph(
        "<b>Premium-only:</b> Originality Insights \u2014 time spent writing + percentage of text pasted "
        "from external sources.",
        body_style
    ))
    story.append(Spacer(1, 4))

    story.append(callout(
        "Originality Insights (plagiarism/paste detection) is available at Premium tier. "
        "Newsela Writing does not have an equivalent feature.",
        label="UNIQUE TO NOREDINK"
    ))
    story.append(Spacer(1, 10))

    # ── LIVE AI TEST FINDINGS ─────────────────────────────────────────────────
    story.append(section_header("LIVE AI TEST FINDINGS (March 2026)"))
    story.append(Spacer(1, 6))

    story.append(Paragraph(
        "Two essays were submitted to probe Grading Assistant scoring calibration \u2014 one with placeholder "
        "content (zero quality) and one with minimal effort (poor quality). Screenshots below show both "
        "the <b>input</b> (what was written) and the <b>output</b> (AI scores), allowing direct comparison.",
        body_style
    ))
    story.append(Spacer(1, 6))

    # Test 1
    story.append(Paragraph(
        "<b>Test 1 \u2014 Input: Mars placeholder essay (placeholder content, no real writing)</b>", label_style
    ))
    story.append(Paragraph(
        "Essay contained no real content: a single placeholder body paragraph (\u2018Saying all my main points "
        "here\u2019), no thesis, no evidence, no reasoning. Only structural shells were present.",
        body_style
    ))
    story += img_block("ai_test_08_mars_graded_view.png", 6.3 * inch, 3.69 * inch,
                       "Test 1 Output \u2014 Mars placeholder essay graded: Note Evidence criterion scored 4/4 despite placeholder content")
    story.append(Spacer(1, 4))
    story += img_block("ai_test_09_mars_rubric_scores.png", 6.3 * inch, 3.69 * inch,
                       "Test 1 Output (detail) \u2014 Full rubric scores for Mars essay: Thesis 2/4, Topic sentence 1/4, Evidence 4/4 (BUG), Reasoning 1/4, Counterarg 1/4, Conclusion 1/4 = 42%")
    story.append(Spacer(1, 8))

    # Test 2
    story.append(Paragraph(
        "<b>Test 2 \u2014 Input: Wild Animals poor essay (minimal effort, no evidence or real argument)</b>", label_style
    ))
    story.append(Paragraph(
        "Deliberately minimal essay: \u2018I think wild animals should not be in captivity. It is bad for them.\u2019 "
        "(Intro) / \u2018Zoos are bad places for wild animals. Animals are sad when they are in cages.\u2019 "
        "(Body \u2014 no text evidence) / \u2018Some people say zoos are good. But I disagree with them.\u2019 "
        "(Counterarg \u2014 no rebuttal) / \u2018In conclusion, wild animals should not be in captivity.\u2019 (Conclusion)",
        body_style
    ))
    story += img_block("ai_test_05_poor_essay_filled.png", 5.0 * inch, 4.27 * inch,
                       "Test 2 Input \u2014 Poor quality Wild Animals essay: minimal content, no text evidence, no real counterargument")
    story.append(Spacer(1, 4))
    story += img_block("ai_test_11_wild_animals_scores_full.png", 6.3 * inch, 3.69 * inch,
                       "Test 2 Output \u2014 Wild Animals poor essay graded: Evidence 1/4 (correct), Counterarg 2/4 (over-credited), Total 42% \u2014 3 AI-generated comments shown")
    story.append(Spacer(1, 8))

    # Findings
    story.append(Paragraph(
        "<b>Finding 1 \u2014 Score floor clustering: Both essays scored exactly 42%</b>", label_style
    ))
    story.append(Paragraph(
        "A placeholder essay (zero effort) and a minimal 4-sentence-per-section essay received identical "
        "total scores. The AI cannot distinguish between zero effort and minimal effort.",
        body_style
    ))

    # Score comparison table
    score_header = [
        Paragraph("Criterion", th_style),
        Paragraph("Mars Essay (placeholder)", th_style),
        Paragraph("Wild Animals (poor)", th_style),
    ]
    score_rows_raw = [
        ("Thesis statement",  "2/4",           "2/4",  False, False),
        ("Topic sentence",    "1/4",           "2/4",  False, False),
        ("Evidence",          "4/4 \u2190 BUG", "1/4",  True,  False),
        ("Reasoning",         "1/4",           "1/4",  False, False),
        ("Counterargument",   "1/4",           "2/4",  False, False),
        ("Conclusion",        "1/4",           "2/4",  False, False),
        ("TOTAL",             "42%",           "42%",  False, True),
    ]
    score_data = [score_header]
    for crit, mars, wild, is_bug, is_total in score_rows_raw:
        crit_p = Paragraph("<b>{}</b>".format(crit) if is_total else crit,
                           td_bold_style if is_total else td_style)
        mars_p = Paragraph("<b>{}</b>".format(mars), td_bold_red_style if (is_bug or is_total) else td_bold_style) \
                 if (is_bug or is_total) else Paragraph(mars, td_center_style)
        wild_p = Paragraph("<b>{}</b>".format(wild), td_bold_style) if is_total else Paragraph(wild, td_center_style)
        score_data.append([crit_p, mars_p, wild_p])

    score_table = Table(score_data, colWidths=[2.5 * inch, 1.9 * inch, 1.9 * inch])
    score_ts = TableStyle([
        ("BACKGROUND",    (0, 0), (-1, 0), NAVY),
        ("GRID",          (0, 0), (-1, -1), 0.5, MGRAY),
        ("TOPPADDING",    (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("LEFTPADDING",   (0, 0), (-1, -1), 7),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 7),
        ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
        # TOTAL row (index 7 = last row)
        ("BACKGROUND",    (0, 7), (-1, 7), PINKBG),
    ])
    for i in range(1, len(score_data) - 1):  # skip header and TOTAL row
        bg = white if i % 2 == 1 else LTGRAY
        score_ts.add("BACKGROUND", (0, i), (-1, i), bg)
    score_table.setStyle(score_ts)
    story.append(score_table)
    story.append(Spacer(1, 8))

    story.append(Paragraph(
        "<b>Finding 2 \u2014 Evidence criterion inconsistency: Same absence of evidence, opposite scores</b>",
        label_style
    ))
    story.append(Paragraph(
        "The Mars essay body paragraph literally said \u2018Saying all my main points here\u2019 \u2014 no quotes, no facts, "
        "no text citations \u2014 yet scored <b>4/4</b> on Evidence (see Test 1 screenshots above). The Wild Animals "
        "essay had the same absence of evidence yet scored <b>1/4</b>. This is a critical calibration failure.",
        body_style
    ))

    story.append(Paragraph(
        "<b>Finding 3 \u2014 Counterargument over-crediting</b>", label_style
    ))
    story.append(Paragraph(
        "\u2018Some people say zoos are good. But I disagree with them.\u2019 received <b>2/4</b> (50%) on the "
        "counterargument criterion \u2014 a two-sentence non-attempt disguised as a counterargument. No specific "
        "opposing argument, no evidence, no rebuttal.",
        body_style
    ))

    story.append(Paragraph(
        "<b>Finding 4 \u2014 Teacher gating required before students see any AI feedback</b>", label_style
    ))
    story.append(Paragraph(
        "After submission, the Grading Assistant scores and comments are NOT visible to students until the "
        "teacher explicitly reviews and returns them. Students see no AI guidance until the teacher completes "
        "a review step.",
        body_style
    ))

    story += img_block("ai_test_10_wild_animals_graded.png", 6.3 * inch, 3.69 * inch,
                       "Teacher gating \u2014 \u2018Start Reviewing\u2019 modal appears before teacher can release AI scores to student. "
                       "Students wait for both AI processing (~5 min) AND teacher review.")
    story.append(Spacer(1, 6))

    story.append(Paragraph(
        "<b>Finding 5 \u2014 Grading latency: ~5 minutes from submission to AI scores appearing</b>", label_style
    ))
    story.append(Paragraph(
        "Timed from student submission to Grading Assistant scores visible in teacher view: approximately "
        "5 minutes. Students must submit, wait for AI processing, and then wait for teacher review before "
        "seeing any feedback.",
        body_style
    ))
    story.append(Spacer(1, 10))

    # ── PRACTICE & ASSESSMENT ─────────────────────────────────────────────────
    story.append(section_header("PRACTICE & ASSESSMENT (LIVE PRODUCT EXPLORATION — March 2026)"))
    story.append(Spacer(1, 6))

    story.append(Paragraph(
        "Separate from the Writing product, NoRedInk includes a full <b>Practice</b> and <b>Assessment</b> "
        "system covering grammar and writing skills. These are entirely distinct from the essay writing "
        "workflow — they are interactive exercises and diagnostics, not composition activities. "
        "Newsela Writing has no equivalent.",
        body_style
    ))
    story.append(Spacer(1, 6))

    story.append(callout(
        "Newsela Writing has no practice exercises, no grammar instruction, no skill diagnostics, and no "
        "mastery tracking system. These three product pillars are exclusive to NoRedInk.",
        label="UNIQUE TO NOREDINK"
    ))
    story.append(Spacer(1, 8))

    # --- PRACTICE ---
    story.append(Paragraph("<b>Practice</b>", label_style))
    story.append(Paragraph(
        "Targeted exercises covering 10 skill categories. Students answer questions interactively "
        "(highlight/click words, fill blanks, select options). The system uses <b>adaptive mastery</b>: "
        "students must answer 2 consecutive questions correctly to advance to the next level within a topic.",
        body_style
    ))
    story.append(Spacer(1, 4))

    story.append(Paragraph("<b>10 Practice Categories:</b>", label_style))
    practice_cats = [
        ("Parts of an Essay", "Thesis statements, topic sentences, introductions, body paragraphs, conclusions, counterarguments"),
        ("Evidence, Citations, and Plagiarism", "Embedding evidence, MLA citation, avoiding plagiarism, context for evidence"),
        ("Clarity and Style", "Vague language, wordiness, formal vs. informal tone"),
        ("Sentences, Phrases, and Clauses", "Fragments, run-ons, dependent clauses, compound/complex sentences"),
        ("Capitalization and Punctuation", "Commas, semicolons, colons, hyphens, rules of capitalization"),
        ("Commonly Confused Words", "5 skill groups (I\u2013V) covering there/their/they\u2019re and dozens more pairs"),
        ("Parts of Speech", "Nouns, pronouns, verbs, adjectives, adverbs, conjunctions, prepositions"),
        ("ACT\u00ae Skills", "Targeted prep aligned to ACT English test question types"),
        ("SAT\u00ae Skills", "Targeted prep aligned to SAT Writing and Language test question types"),
        ("Passages", "Grammar skills assessed in multi-paragraph passage context"),
    ]
    for cat_name, cat_desc in practice_cats:
        story.append(Paragraph(
            "\u2022 <b>{}</b> \u2014 {}".format(cat_name, cat_desc), bullet_style
        ))
    story.append(Spacer(1, 6))

    story += img_block("practice_03_practice_categories.png", 6.3 * inch, 3.69 * inch,
                       "Practice — 10 skill categories browseable by grade level (Grade 3\u201312)")
    story.append(Spacer(1, 6))

    story.append(Paragraph("<b>How adaptive practice works (live test):</b>", label_style))
    practice_mechanics = [
        "Each topic has multiple parts (e.g., Thesis Statements: Part 1 Fact vs. Opinion, Part 2 Vague Words, Part 3 Wordiness)",
        "Student must answer 2 consecutive questions correctly to advance (\u201cAnswer two in a row correctly to continue\u201d)",
        "After a wrong answer: blue \u201cTry again\u201d banner appears; <b>Show Hint</b> button unlocks an inline mini-lesson",
        "Hints include worked examples personalized to the student\u2019s selected books/movies (e.g., Harry Potter examples for a student who selected Harry Potter)",
        "Questions answered counter and star rating (0\u20134 stars) visible per topic",
        "Mastery = demonstrated full understanding, not a set number of questions completed",
    ]
    for b in practice_mechanics:
        story.append(Paragraph("\u2022 " + b, bullet_style))
    story.append(Spacer(1, 6))

    # Side-by-side: question + incorrect feedback with hint
    q_path  = os.path.join(BASE, "practice_11_practice_exercise_question.png")
    fb_path = os.path.join(BASE, "practice_13_incorrect_feedback.png")
    hint_path = os.path.join(BASE, "practice_14_hint_panel.png")
    pair_items = []
    if os.path.exists(q_path) and os.path.exists(fb_path):
        pair_w = 3.0 * inch
        pair_h = pair_w * 0.585
        pair_t = Table([[
            [Image(q_path,  width=pair_w, height=pair_h),
             Paragraph("Student practice question: \u201cHighlight the wordy phrase\u201d", caption_style)],
            [Image(fb_path, width=pair_w, height=pair_h),
             Paragraph("Wrong answer: \u201cTry again!\u201d banner + Show Hint button unlocks", caption_style)],
        ]], colWidths=[3.15 * inch, 3.15 * inch])
        pair_t.setStyle(TableStyle([
            ("VALIGN",        (0, 0), (-1, -1), "TOP"),
            ("TOPPADDING",    (0, 0), (-1, -1), 2),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 2),
            ("LEFTPADDING",   (0, 0), (-1, -1), 0),
            ("RIGHTPADDING",  (0, 0), (-1, -1), 4),
        ]))
        story.append(pair_t)
    story.append(Spacer(1, 4))
    story += img_block("practice_14_hint_panel.png", 6.3 * inch, 3.69 * inch,
                       "Show Hint \u2014 inline mini-lesson with color-coded grammar rule and personalized examples (Harry Potter)")
    story.append(Spacer(1, 8))

    story.append(Paragraph(
        "<b>Important: No AI in Practice exercises.</b> The adaptive mastery system is rule-based "
        "(2 correct in a row = advance). Hints are static instructional content, not AI-generated. "
        "The AI Grading Assistant applies only to essay writing, not to Practice.",
        body_style
    ))
    story.append(Spacer(1, 8))

    # --- ASSESSMENT ---
    story.append(Paragraph("<b>Assessment</b>", label_style))
    story.append(Paragraph(
        "Four distinct assessment types \u2014 all drawing on the same skill content as Practice, "
        "but deployed in different instructional contexts.",
        body_style
    ))
    story.append(Spacer(1, 4))

    assessment_types = [
        ("<b>Planning Diagnostic</b>",
         "Administered at semester start. Gives teacher a class-wide snapshot of strengths and weaknesses across skill categories. Used to plan instructional focus for the semester."),
        ("<b>Unit Diagnostic</b>",
         "Pre/post assessment for a specific skill unit. Students take it at unit start (baseline), then again after instruction to measure growth."),
        ("<b>Quiz</b>",
         "Locked, graded assessment administered at end of unit. Single attempt; no hints; auto-scored. Results appear in teacher gradebook."),
        ("<b>Passage Quiz</b>",
         "Grammar skills assessed in context \u2014 students edit/correct errors in a multi-paragraph passage. Grammar-only (no essay structure categories)."),
    ]
    for bold_name, desc in assessment_types:
        story.append(Paragraph(
            "\u2022 {} \u2014 {}".format(bold_name, desc), bullet_style
        ))
    story.append(Spacer(1, 6))

    story += img_block("assessment_01_assessment_types.png", 6.3 * inch, 2.5 * inch,
                       "Assessment \u2014 four types: Planning Diagnostic, Unit Diagnostic, Quiz, Passage Quiz")
    story.append(Spacer(1, 6))

    story.append(Paragraph(
        "<b>Key insight: Same content, different modes.</b> The same topic content (e.g., \u201cThesis Statements\u201d) "
        "can be assigned as Practice (adaptive, repeatable), Quiz (locked, graded), or Unit Diagnostic "
        "(pre/post baseline). Mode is the teacher\u2019s choice at assignment time.",
        body_style
    ))
    story.append(Spacer(1, 8))

    # --- TEACHER REPORTING ---
    story.append(Paragraph("<b>Teacher Reporting (Student Data)</b>", label_style))
    story.append(Paragraph(
        "The Student Data dashboard has three tabs:",
        body_style
    ))
    reporting_tabs = [
        ("<b>Grades</b>", "Assignment-by-assignment gradebook. Columns per assignment; rows per student. Filters by assignment type and date range. Downloadable."),
        ("<b>Mastery</b>", "Skill-by-skill mastery grid: 80+ individual learning pathways as columns, students as rows. Each cell shows mastery status (Not started / In progress / Mastered). Filterable by pathway group."),
        ("<b>Writing Portfolios</b>", "All student essays in one view for portfolio review and comparison over time."),
    ]
    for bold_name, desc in reporting_tabs:
        story.append(Paragraph(
            "\u2022 {} \u2014 {}".format(bold_name, desc), bullet_style
        ))
    story.append(Spacer(1, 6))

    story += img_block("assessment_07_mastery_grid.png", 6.3 * inch, 2.8 * inch,
                       "Mastery tab \u2014 80+ skill pathways tracked per student. Columns scroll horizontally; color-coded mastery status per cell.")
    story.append(Spacer(1, 10))

    # ── FREE VS. PREMIUM ──────────────────────────────────────────────────────
    story.append(section_header("FREE VS. PREMIUM"))
    story.append(Spacer(1, 6))

    fvp_header = [
        Paragraph("Feature", th_style),
        Paragraph("Free", th_style),
        Paragraph("Premium", th_style),
    ]
    fvp_rows_raw = [
        ("Guided Draft genres",                    "3 genres",  "10+ genres"),
        ("Guided Draft prompts",                   "Limited",   "400+"),
        ("Quick Write prompts",                    "Limited",   "2,000+"),
        ("Grammar skills",                         "Limited",   "1,000+"),
        ("AI Grading Assistant",                   "\u2717",    "\u2713"),
        ("Originality Insights",                   "\u2717",    "\u2713"),
        ("State test rubrics & filters",           "\u2717",    "\u2713"),
        ("Benchmark assessments",                  "\u2717",    "\u2713"),
        ("LMS integrations (Canvas, Schoology)",   "\u2717",    "\u2713"),
    ]
    fvp_data = [fvp_header] + [
        [
            Paragraph(r[0], td_style),
            Paragraph(r[1], td_center_style),
            Paragraph(r[2], td_center_style),
        ]
        for r in fvp_rows_raw
    ]
    fvp_table = Table(fvp_data, colWidths=[3.5 * inch, 1.35 * inch, 1.45 * inch])
    fvp_ts = TableStyle([
        ("BACKGROUND",    (0, 0), (-1, 0), NAVY),
        ("GRID",          (0, 0), (-1, -1), 0.5, MGRAY),
        ("TOPPADDING",    (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("LEFTPADDING",   (0, 0), (-1, -1), 7),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 7),
        ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
    ])
    for i in range(1, len(fvp_data)):
        bg = white if i % 2 == 1 else LTGRAY
        fvp_ts.add("BACKGROUND", (0, i), (-1, i), bg)
    fvp_table.setStyle(fvp_ts)
    story.append(fvp_table)
    story.append(Spacer(1, 10))

    # ── KEY STRENGTHS ─────────────────────────────────────────────────────────
    story.append(section_header("KEY STRENGTHS"))
    story.append(Spacer(1, 6))

    strengths = [
        ("Writing + Grammar + Assessment on one platform",
         "Essays, 1,000+ grammar skill exercises, adaptive mastery practice, and 4 assessment types in a single product. No writing-only competitor matches this breadth."),
        ("Free tier",
         "Teachers adopt without a school purchase \u2014 lowest friction in the space."),
        ("Pre-writing tutorials",
         "Genre instruction is built into the student workflow before writing starts."),
        ("Section-based scaffolding",
         "Essay sections (Intro/Body/Counterargument/Conclusion) are pre-built; students fill in, not format."),
        ("Source annotation",
         "Students highlight and annotate embedded texts without leaving the editor."),
        ("Originality Insights",
         "Plagiarism/paste detection visible to teacher (Premium)."),
        ("Novel Analysis",
         "Chapter-level writing prompts \u2014 unique in the space."),
        ("Mastery-based skill tracking",
         "80+ individual skill pathways tracked per student in a visual mastery grid. Teachers see which skills each student has mastered, is progressing on, or hasn\u2019t started."),
        ("LMS integrations",
         "Canvas/Schoology gradebook sync (Premium) streamlines teacher workflow."),
    ]
    for title, desc in strengths:
        story.append(Paragraph(
            "\u2022 <b><font color='#E8274B'>{}</font></b> \u2014 {}".format(title, desc),
            bullet_style
        ))
    story.append(Spacer(1, 10))

    # ── KNOWN LIMITATIONS ─────────────────────────────────────────────────────
    story.append(section_header("KNOWN LIMITATIONS"))
    story.append(Spacer(1, 6))

    limitations = [
        ("<b>AI feedback is post-submission only</b>",
         "no real-time feedback while student is writing."),
        ("<b>No sentence-level classification</b>",
         "Grading Assistant scores whole criteria, not individual sentences."),
        ("<b>AI Grading Assistant is Premium-only</b>",
         "free tier teachers get zero AI assistance."),
        ("<b>No state rubric library</b>",
         "rubrics are genre-based; Newsela Writing covers all 50 states free."),
        ("<b>Score floor clustering</b>",
         "both placeholder and poor essays scored exactly 42%; AI cannot distinguish effort levels."),
        ("<b>Evidence criterion miscalibration</b>",
         "placeholder body paragraph scored 4/4 on Evidence (live test confirmed)."),
        ("<b>General Comments lack specificity</b>",
         "references student text but does not cite specific articles or facts for students to use."),
        ("<b>No live content integration</b>",
         "sources are NRI-curated static texts; no live article library."),
    ]
    for bold_part, rest in limitations:
        story.append(Paragraph(
            "\u2022 {} \u2014 {}".format(bold_part, rest), bullet_style
        ))
    story.append(Spacer(1, 12))

    # ── FOOTER ────────────────────────────────────────────────────────────────
    story.append(HRFlowable(width=W, thickness=0.5, color=MGRAY, spaceAfter=4))
    story.append(Paragraph(
        "Competitive Intelligence Report \u00b7 NoRedInk \u00b7 Research Date: March 17, 2026 \u00b7 "
        "Prepared by Claude (Competitive Agent)",
        footer_style
    ))

    doc.build(story)
    print("PDF written to: {}".format(OUT))


if __name__ == "__main__":
    build()
