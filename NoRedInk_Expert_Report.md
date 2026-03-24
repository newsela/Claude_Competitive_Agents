# NoRedInk — Expert Baseline Report
**Research Date:** March 17, 2026
**Researcher:** Claude (Competitive Agent)
**App URL:** https://www.noredink.com
**Login tested:** Teacher (Mx. Dina Patel) + Student view (Dina)

---

## Executive Summary

NoRedInk is a comprehensive writing and grammar platform for grades 3–12. Originally built around grammar skill mastery, it has evolved into a full writing composition suite with AI-powered grading. It offers a **free tier** for individual teachers and a **Premium school/district license** that unlocks 1,000+ skills, 2,000+ writing prompts, 10+ writing genres, AI Grading Assistant, originality detection, and LMS integrations. Key stats: -40% teacher grading time with AI Grading Assistant; +6 points average ACT English growth; +136% increase in highest-tier test performance for economically disadvantaged students.

---

![NoRedInk login page — Google, Clever, ClassLink, and username/password options](01_login_page.png)

## Product Identity

| Attribute | Detail |
|---|---|
| **Product Name** | NoRedInk |
| **URL** | https://www.noredink.com |
| **Target Grades** | 3–12 |
| **AI Feature** | Grading Assistant (post-submission scoring + comments) |
| **Core Differentiator** | Writing + Grammar on one platform |
| **Free Tier** | Yes — limited content, individual teacher |
| **Premium** | School/district license, sales-led, quote-based |
| **Login options** | Username/password, Google, Clever, ClassLink |

---

## Navigation (Teacher)

| Nav Item | Description |
|---|---|
| **Dashboard** | Welcome screen with "Try These Next" recommendations and class assignment status |
| **My Assignments** | All assignments by class, filterable by type (Diagnostics, Practice, Quizzes, Writing) |
| **Student Data** | Class-level mastery and performance data |
| **Browse & Assign** | Assignment Library (Collections + Assignment Types) |
| **Manage Classes** | Roster management |
| **Go Premium** | Upgrade page |

---

## Assignment Library — Collections

| Collection | Description |
|---|---|
| **Skill Building** | Target specific writing and grammar skills |
| **Daily Writing** | Short response prompts for writing fluency |
| **Writing Genres** | Prompts and scaffolded support by genre |
| **Text-Based Writing** | Engaging texts with analysis/reflection prompts |
| **Novel Analysis** | Chapter-by-chapter and full-novel writing prompts |
| **Standards & Tests** | Activities aligned to standards and standardized tests (ACT, SAT, AP, state tests) |

---

## Assignment Types

### 1. Quick Write
- Students respond to a prompt with optional sources and rubric items
- **Great for:** applying new writing skills, low-stakes practice
- 2,000+ prompts (Premium); limited in Free

### 2. Guided Short Response
- Students draft a **paragraph** with sentence-by-sentence support
- **Great for:** scaffolded writing instruction, text analysis, argumentative writing

### 3. Guided Essay (Guided Draft)
- Students draft a full essay with the support of **tutorials, models, and tips**
- Sections: Title (optional), Introduction, Body Paragraphs, Counterargument, Conclusion
- **Great for:** scaffolded writing instruction, writing across genres
- 400+ prompts, 10+ genres (Premium); 3 genres in Free
- **AI Grading Assistant enabled** (shown in assignment list with 🎯 badge)

### 4. Practice
- Targeted exercises for writing and grammar skill mastery
- 1,000+ skills (Premium)

### 5. Assessment
- Diagnostics and quizzes to assess student skills
- Standards-based benchmark assessments (Premium)

---

## Student Writing Experience (Guided Essay)

### Pre-Writing Tutorial
Before starting, students are shown an interactive tutorial explaining the genre (e.g., "Writing an Argumentative Essay"). Students can click "Tell me more!" to proceed through the tutorial or "Skip this tutorial and begin."

![Student writing editor — initial state](ai_test_02_student_editor.png)

### Writing Editor Layout
- **Left panel** — 3 tabs:
  - **Prompt & Sources** — assignment prompt + embedded source texts (2 sources, highlightable + annotatable, with footnote glossary)
  - **Tips & Examples** — context-sensitive help that changes based on which section the student is writing
  - **Rubric** — rubric criteria with descriptions and "View example" buttons
- **Right panel (Writing Area)** — sectioned essay structure:
  - Title (Optional)
  - Introduction (Required)
  - Body Paragraphs (Required)
  - Counterargument (Required)
  - Conclusion (Required)

### Section-Level Scaffolding (when student opens Introduction)
- Left panel auto-switches to "Tips & Examples"
- Shows: **Key Parts of the Introduction** — color-coded component accordion:
  - 🟡 Hook
  - 🟢 Bridge
  - 🩷 Thesis Statement
- "View tutorial" button (opens in new tab)
- "View examples" button
- **Tips and Tricks carousel** (8 tips, paginated)
- "What's an argumentative essay?" section with link to full genre tutorial

![After "I've read everything" — rubric panel visible](ai_test_03_writing_area.png)

### Rubric (student-facing)
All 6 criteria are visible before writing begins, each with a plain-language description and "View example" button:
1. Thesis statement is a debatable opinion
2. Each topic sentence is a claim that supports the thesis
3. Each piece of evidence is a fact that supports the claim
4. Reasoning connects the evidence to the claim
5. Counterargument paragraph presents an opposing argument and defends the essay's thesis
6. Conclusion restates the argument and explains why readers should care

![Full editor with 5 essay sections](ai_test_04_writing_sections.png)

![Poor essay filled in all sections](ai_test_05_poor_essay_filled.png)

![Strong essay filled in all sections](ai_test_12_strong_essay_filled.png)

### Other Student Features
- Auto-save every 30 seconds
- Bold, Italic, Underline, List formatting toolbar per section
- **Interest-based home screen** — wallpaper tiles from student's declared interests (e.g., SpongeBob, Harry Potter)
- **Topics Mastered** gamification counter on student home
- PDF version of source texts available for download

---

## AI Grading Assistant (Teacher View)

![Assignment creation with Grading Assistant enabled](ai_test_01_assign_wild_animals.png)

Triggered when teacher opens a submitted student essay.

### What It Does
- Scores each rubric criterion **1–4** automatically
- Adds per-criterion **comments** (e.g., "Not bad let's continue to work on this")
- Generates **General Comments** (multi-paragraph narrative feedback to the student)
- Shows total **% score** (e.g., 42%)
- Teacher can **override** any score, add comments, and **request revisions**
- "How did Grading Assistant do? 👍 / 👎" feedback button for quality reporting

![Submit confirmation modal](ai_test_06_submit_confirm.png)

![Student home after submission](ai_test_07_submitted_home.png)

### Sample Grading Assistant Output (Student Test, A Home on Mars)

**Rubric Scores:**
| Criterion | Score |
|---|---|
| Thesis statement is a debatable opinion | 2/4 |
| Each topic sentence is a claim that supports the thesis | 1/4 |
| Each piece of evidence is a fact that supports the claim | 4/4 |
| Reasoning connects the evidence to the claim | — |
| Counterargument | — |
| Conclusion | — |
| **Total** | **42%** |

![Teacher view of Mars essay graded](ai_test_08_mars_graded_view.png)

![Full page Mars graded view with rubric scores](ai_test_09_mars_rubric_scores.png)

**General Comments (AI-generated):**
> "You've got a good sense of what an argumentative essay needs, Student! Now it's time to fill in your ideas. Start by writing a clear thesis in your first paragraph that states your opinion: should humans colonize Mars? Your essay will need body paragraphs that support your thesis. Each body paragraph should start with a topic sentence that gives one reason why humans should (or shouldn't) colonize Mars. To make your argument convincing, add evidence from the texts to each body paragraph."

![Wild Animals graded with "Start reviewing" modal](ai_test_10_wild_animals_graded.png)

![Wild Animals scores — full view](ai_test_11_wild_animals_scores_full.png)

### Premium-Only Grading Features
- **Originality Insights** — time spent writing + percentage of text pasted from external sources
- **Insights toggle** (locked in Free)

---

## Assignment Results Dashboard (Teacher)

| Column | Description |
|---|---|
| Student | Name with link to individual submission |
| Time Submitted | Timestamp |
| Score | Percentage score (Grading Assistant or manual) |

- Tabs: **Student Results** / **Prompt & Sources**
- Export/print available
- Premium: Originality Insights adds time-spent and paste-rate per student

---

## Free vs. Premium Comparison

| Feature | Free | Premium |
|---|---|---|
| Writing & Grammar Skills | Limited | 1,000+ |
| Quick Write Prompts | Limited | 2,000+ |
| Guided Draft Prompts/Genres | Limited (3 genres) | 400+ prompts, 10+ genres |
| AI-powered Grading Assistant | ✗ | ✓ |
| Originality Insights | ✗ | ✓ |
| State Test Filters, Prompts, Rubrics | ✗ | ✓ |
| School/District Benchmark Assessments | ✗ | ✓ |
| Schoology, Canvas, Clever Integrations | ✗ | ✓ |

---

## Pricing & Access

- **Free tier**: Individual teacher, limited content, no AI grading
- **Premium**: School/district license, sales-led, quote-based (no public pricing)
- Unlike Newsela Writing, NoRedInk has a **standalone free tier** — teachers can use it without a school purchase
- Premium is purchased per student (per license)

---

## Platform Integrations (Premium)

LMS: Canvas, Schoology (assignment creation, rostering, gradebook sync)
SSO/Rostering: Clever, ClassLink, Google Classroom, Infinite Campus

---

## Research & Efficacy Claims

| Stat | Context |
|---|---|
| +136% | Increase in economically disadvantaged students in highest test performance tier (Wylie case study) |
| +6 points | Average ACT® English Test growth (Jersey Community HS case study) |
| -40% | Reduction in grading time with AI Grading Assistant (PVSchools AZ) |

---

## Key Differentiators (Strengths)

1. **Writing + Grammar on one platform** — NoRedInk's grammar roots give it 1,000+ skill exercises no writing-only tool has
2. **Free tier** — teachers can adopt without school purchase; lowers barrier to entry significantly
3. **Pre-writing tutorials** — students learn genre concepts before writing; not just "write and get feedback"
4. **Structured essay sections** — essay is broken into labeled parts (Intro/Body/Counterargument/Conclusion) before writing begins
5. **In-context tips and examples** — section-specific help (Hook, Bridge, Thesis) available while writing
6. **Source text annotation** — students can highlight and annotate embedded texts
7. **Originality Insights** — plagiarism/paste detection (Premium)
8. **Novel Analysis collection** — chapter-level writing prompts; no equivalent in Newsela Writing
9. **Interest-based personalization** — students declare interests; home screen wallpaper reflects them
10. **LMS integrations** — Canvas/Schoology gradebook sync (Premium)

---

## Potential Weaknesses / Gaps

1. **AI feedback is post-submission only** — no real-time feedback while student is writing (unlike Newsela's Luna AI)
2. **No sentence-level classification** — Grading Assistant scores whole criteria, not individual sentences
3. **General Comments are generic** — AI feedback reads as paragraph summaries, not specific sentence-level guidance
4. **Grading Assistant is Premium-only** — free tier teachers get no AI grading at all
5. **No state rubric library** — rubrics are genre-based, not 50-state-aligned like Newsela
6. **Teacher must grade manually (or wait)** — in free tier, teacher grades everything; in Premium, AI pre-grades but teacher must review
7. **No content integration** — sources are NRI-curated, not from a live article library like Newsela
8. **No cross-curricular documentation** — product positioned primarily for ELA

---

## Screenshots Index

| File | Description |
|---|---|
| `01_login_page.png` | Login page — Google, Clever, ClassLink, username/password options |
| `02_teacher_dashboard.png` | Teacher dashboard — Mx. Patel, Class101, Shortcuts |
| `03_assignment_library.png` | Assignment Library — Collections and Assignment Types |
| `04_writing_types.png` | Writing types — Quick Write, Guided Short Response, Guided Essay |
| `05_grading_assistant.png` | Grading Assistant library — Argumentative text sets (Premium gate visible) |
| `06_my_assignments.png` | My Assignments — A Home on Mars Guided Essay, past due |
| `07_assignment_results.png` | Assignment Results — Student Results table with Grading Assistant note |
| `08_grading_view.png` | Individual student grading — essay + rubric scores side by side |
| `09_student_home_teacher_view.png` | Student home (teacher preview) — Topics Mastered, interest wallpaper |
| `10_student_tutorial.png` | Pre-writing tutorial — "Writing an Argumentative Essay" |
| `11_student_rubric_panel.png` | Student rubric panel — all 6 criteria with examples before writing |
| `12_student_writing_editor.png` | Full writing editor — prompt left, structured sections right |
| `13_student_intro_scaffolding.png` | Introduction section — Hook/Bridge/Thesis scaffolding, 8 tips |
| `14_premium_page.png` | Premium page — Free vs. Premium table, stats, quote form |

---

## Competitive Baseline Summary

NoRedInk competes in the **K-12 writing and grammar** space, positioned as:
- A **broader** platform than Newsela Writing (grammar + writing vs. writing only)
- A **more accessible** product (free tier vs. school-license-only)
- A **post-feedback** AI model vs. Newsela's real-time guidance
- More focused on **essay structure scaffolding** vs. Newsela's **sentence-type classification**

Direct competitors: Newsela Writing, Writable, Quill, Turnitin Feedback Studio, CommonLit Writing
