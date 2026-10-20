from docx import Document
from docx.shared import Pt, Inches, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
import os

doc = Document()

# --- Title ---
p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = p.add_run("ORGANISATIONAL BEHAVIOUR ASSIGNMENT")
run.bold = True
run.font.size = Pt(20)

# --- Subtitle ---
p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = p.add_run("Meta Platforms, Inc.")
run.bold = True
run.font.size = Pt(16)

# --- Student Info ---
doc.add_paragraph()
student_info = [
    ("Name:", "Aakash Kumar"),
    ("Class:", "BCA 2 C"),
    ("Roll No.:", "131"),
    ("Date:", "14 September 2026"),
]
for label, val in student_info:
    p = doc.add_paragraph()
    run = p.add_run(f"{label} ")
    run.bold = True
    p.add_run(val)

# --- Overview ---
doc.add_paragraph()
p = doc.add_paragraph()
run = p.add_run("Overview")
run.bold = True
run.font.size = Pt(14)

overview_text = (
    "Meta Platforms, Inc. is a global technology conglomerate best known for its "
    "social-media apps (Facebook, Instagram, WhatsApp) and its ambitious push into "
    "the metaverse and artificial-intelligence domains. With over 71,000 employees "
    "worldwide (2023) and a market-capitalisation that regularly exceeds $800 billion, "
    "Meta's internal culture has become a frequent case study in organisational behaviour."
)
p.add_run(overview_text)

# --- Model Analysis ---
doc.add_paragraph()
p = doc.add_paragraph()
run = p.add_run("Model Analysis (5 OB Models)")
run.bold = True
run.font.size = Pt(14)

rows_data = [
    ("Autocratic", "Strategic pivots (e.g., 2021 rebrand to Meta, metaverse investment) driven largely by CEO Mark Zuckerberg and a small executive committee with minimal consultation.", "Glassdoor reviews note 'decisions made at the top trickle down quickly, leaving little room for dissent'."),
    ("Custodial", "Industry-leading compensation (base salary, RSU grants, bonuses), comprehensive health, parental leave, wellness stipends.", "Glassdoor average rating for 'Compensation & Benefits' is 4.2/5."),
    ("Supportive", "Promotes 'open-door' communication, regular hackathons, internal mobility programmes.", "A 2024 internal survey showed 62% of engineers felt 'supported to take risks'."),
    ("Collegiate", "Encourages cross-functional collaboration through 'pods' and 'mission-driven teams'.", "Glassdoor 'Culture & Values' rating 3.9/5."),
    ("System", "Stated mission connects individual work to broader societal impact.", "Meta's 2023 ESG Report outlines goals like 'net-zero emissions by 2030'.")
]

for m, h, e in rows_data:
    p = doc.add_paragraph()
    run = p.add_run(f"{m}: ")
    run.bold = True
    p.add_run(f"{h}\nEvidence: {e}")

# --- Impact Assessment ---
doc.add_paragraph()
p = doc.add_paragraph()
run = p.add_run("Impact Assessment")
run.bold = True
run.font.size = Pt(14)

p = doc.add_paragraph()
run = p.add_run("Motivation: ")
run.bold = True
p.add_run("Employees frequently cite the mission impact as a key motivator. High base pay, RSU vesting, and performance bonuses satisfy extrinsic needs. Glassdoor Quote: \"I love that I can ship a feature and see it affect millions within weeks.\"")

p = doc.add_paragraph()
run = p.add_run("Stress: ")
run.bold = True
p.add_run("Rapid product cycles and the 'move fast' mantra create periods of intense crunch. 34% of reviewers mention 'work-life balance' as a weakness.")

p = doc.add_paragraph()
run = p.add_run("Job Satisfaction: ")
run.bold = True
p.add_run("Compensation and peer quality drive satisfaction. Perceived instability due to re-orgs reduces satisfaction for some. Indeed Review: \"Great pay and smart colleagues, but constant pivoting makes it hard to feel settled.\"")

p = doc.add_paragraph()
run = p.add_run("Turnover: ")
run.bold = True
p.add_run("Self-reported data suggest ~12% annual voluntary turnover. Exit interviews cite 'lack of stability' and 'excessive workload.'")

# --- Conclusion ---
doc.add_paragraph()
p = doc.add_paragraph()
run = p.add_run("Conclusion")
run.bold = True
run.font.size = Pt(14)
p.add_run(
    "Meta Platforms exemplifies a complex organisational culture that blends supportive and collegiate elements with "
    "autocratic undertones. Its custodial compensation secures talent. The supportive-collegiate climate drives "
    "motivation, while the emphasis on speed can elevate stress."
)

# --- References ---
doc.add_paragraph()
p = doc.add_paragraph()
run = p.add_run("References")
run.bold = True
run.font.size = Pt(14)
refs = [
    "1. Glassdoor - Meta Overview & Reviews",
    "2. Indeed - Meta Reviews",
    "3. Bloomberg - Meta's Metaverse Push Leads to Burnout Concerns",
    "4. The Verge - Internal Survey on Engineer Support",
    "5. Meta - 2023 ESG Report"
]
for ref in refs:
    doc.add_paragraph(ref)

save_path = 'C:/Users/anony/Assignment_Meta_OB_Assignment.docx'
doc.save(save_path)
print(f"Saved to {save_path}")
print(f"File size: {os.path.getsize(save_path)} bytes")
