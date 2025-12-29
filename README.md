# Ai_analysis_after_stemcell_transplant-
Image analysis of home environment after stem cell transplant 

# Stem Cell Healing Environment — Home Safety Checklist (PDF generator)

This repository contains a small script that generates a PDF checklist for home safety during stem cell transplant recovery (pets, mold, household exposures).

## Contents
- `generate_stem_cell_checklist.py` — script that builds the PDF using ReportLab.
- `requirements.txt` — Python dependencies.
- `.github/workflows/python-ci.yml` — optional CI to check that the script runs.

## Quick start (local)
1. Clone the repo:
   ```
   git clone <your-repo-url>
   cd <your-repo-name>
   ```
2. Create & activate a virtual environment (recommended):
   ```
   python -m venv .venv
   source .venv/bin/activate   # macOS / Linux
   .venv\Scripts\activate      # Windows
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Run the generator:
   ```
   python generate_stem_cell_checklist.py --output "Stem_Cell_Healing_Environment_Pets_Mold_Safety.pdf"
   ```

## Notes
- This checklist is for environmental optimization only and is not medical advice. Consult clinicians for anything clinical or patient-specific.
- Update the script, content, or metadata to match your institution's guidance before sharing publicly.

## License
Choose and add a license (e.g., MIT). Replace this section with the chosen license text.
