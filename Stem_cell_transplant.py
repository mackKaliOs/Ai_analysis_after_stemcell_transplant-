from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, ListFlowable, ListItem
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

# Output PDF path (change as needed)
file_path = "/mnt/data/Stem_Cell_Healing_Environment_Pets_Mold_Safety.pdf"

# Document setup
doc = SimpleDocTemplate(file_path, pagesize=LETTER,
                        title="Stem Cell Healing Environment: Home Safety Checklist with Pets & Mold Considerations",
                        author="Prepared by Care Team")

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name='SectionTitle', parent=styles['Heading2'], spaceAfter=6))
styles.add(ParagraphStyle(name='Small', parent=styles['BodyText'], fontSize=10, leading=12))
bullet_style = ParagraphStyle('Bullet', parent=styles['BodyText'], leftIndent=12, bulletIndent=6, spaceBefore=2)

story = []

# Title and disclaimer
story.append(Paragraph("Stem Cell Healing Environment: Home Safety Checklist with Pets & Mold Considerations", styles['Title']))
story.append(Spacer(1, 6))

disclaimer_text = (
    "<b>Medical disclaimer:</b> This checklist is intended as an environmental optimization guide only and "
    "is <b>not</b> medical advice. Always consult the patient's transplant team, infectious disease specialist, "
    "or treating clinician before making changes to care, medications, or infection-control procedures."
)
story.append(Paragraph(disclaimer_text, styles['Small']))
story.append(Spacer(1, 12))

# Sections data as lists for controlled formatting
sections = [
    {
        "title": "1. Purpose",
        "bullets": [
            "Help ensure the safest possible home recovery environment after stem cell transplant (January).",
            "Focus on minimizing exposures to xenoestrogens, known carcinogens, mold/mycotoxins, and harsh household chemicals.",
            "This is an environmental checklist to support clinician guidance during immune suppression."
        ]
    },
    {
        "title": "2. Critical Elimination Targets",
        "bullets": [
            "Remove all scented or aerosolized products (air fresheners, plug-ins, scented candles, perfumes).",
            "Avoid plastics for food storage—prefer glass; especially avoid plastics labelled #3, #6, #7 when possible.",
            "Remove vinyl shower curtains and Teflon / degraded non-stick cookware.",
            "Replace synthetic bedding with organic cotton or natural fibers where possible.",
            "Dispose of expired medication and limit use of bleach-based or harsh-chemical cleaners."
        ]
    },
    {
        "title": "3. Mold and Mycotoxin Prevention",
        "bullets": [
            "Inspect high-risk zones (bathrooms, under-sink, basements, HVAC returns) for visible mold or musty odors.",
            "Use HEPA + activated carbon air purifiers in major living areas and the recovery room.",
            "Keep humidity below ~50%; avoid consumer humidifiers unless distilled water and weekly sanitization are guaranteed.",
            "Consult the medical team before considering dietary mycotoxin binders or supplements."
        ]
    },
    {
        "title": "4. Pet and Litter Box Protocols",
        "bullets": [
            "No direct patient handling of litter boxes or feces—delegate to a healthy, immunocompetent household member.",
            "Keep litter boxes far from the patient's room and away from HVAC intakes; prefer outdoor cleaning if feasible.",
            "Avoid birds, reptiles, amphibians, and exotic pets for at least the first 12 months post-transplant.",
            "Prevent bed-sharing, licking, or face contact; bathe pets regularly with vet-approved, non-toxic shampoos.",
            "Use HEPA filtration in any shared pet spaces and clean pet bowls/toys with natural enzyme cleaners."
        ]
    },
    {
        "title": "5. Food, Water, and Air",
        "bullets": [
            "Use filtered or bottled water stored in glass; avoid long-term storage in plastic.",
            "Follow safe food-handling practices and clinician dietary restrictions for neutropenic or immunosuppressed patients.",
            "Minimize wireless device proximity to the bed if desired; prioritize wired connections and distance for bedside devices."
        ]
    },
    {
        "title": "6. Recommended Additions (Discuss with clinicians)",
        "bullets": [
            "HEPA + activated carbon air purifiers in recovery and common areas.",
            "Non-toxic houseplants (if no mold risk and the patient is not allergic)—e.g., snake plant. Keep soil dry to avoid mold.",
            "Consider environmental controls approved by the medical team (specialty supports or devices only if clinically indicated).",
            "Daily wiping of high-touch surfaces with approved cleaners and regular ventilation when outdoor air quality permits."
        ]
    },
    {
        "title": "7. Emotional & Spiritual Safety",
        "bullets": [
            "Declutter key living spaces to reduce stress and promote easy cleaning.",
            "Provide calming visual anchors (art, photos, nature imagery).",
            "Use gentle music, guided meditation, or journaling to support emotional wellbeing."
        ]
    }
]

# Add sections to story with bullet lists
for i, sec in enumerate(sections):
    story.append(Paragraph(sec["title"], styles['SectionTitle']))
    # Build ListFlowable of ListItems
    items = [ListItem(Paragraph(b, bullet_style), leftIndent=12, bulletColor=colors.black) for b in sec["bullets"]]
    story.append(ListFlowable(items, bulletType='bullet', start='•', leftIndent=12))
    story.append(Spacer(1, 12))
    # Optional page break between major groups (example after section 4)
    if i == 3:
        story.append(PageBreak())

# Footer / contacts (replace with actual contact info if desired)
story.append(Spacer(1, 6))
story.append(Paragraph("For clinical questions contact the transplant team or infectious disease specialist.", styles['Small']))

# Build PDF
doc.build(story)

print("PDF written to:", file_path)
