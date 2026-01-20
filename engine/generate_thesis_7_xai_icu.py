#!/usr/bin/env python3
"""Generate Thesis 7: Explainable AI in ICU Machine Learning - A Scoping Review"""
import os
import sys
import zipfile
from pathlib import Path

# Use relative paths for portability
ENGINE_DIR = Path(__file__).parent.absolute()
PROJECT_ROOT = ENGINE_DIR.parent
os.chdir(ENGINE_DIR)
sys.path.insert(0, str(ENGINE_DIR))

from draft_generator import generate_draft

OUTPUT_DIR = PROJECT_ROOT / "theses_output" / "thesis_7_xai_icu_review"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

print("=" * 60)
print("THESIS 7: Explainable AI in ICU Machine Learning")
print("=" * 60)

topic = """Explainable AI Methods Deployed in Intensive Care Machine Learning Models: A Scoping Review

Research Question: What explainable AI (XAI) methods have been applied to machine learning models used in intensive care unit (ICU) clinical decision support, and what are their reported effectiveness, limitations, and implementation challenges?

This is a SCOPING REVIEW following established methodology (Arksey & O'Malley framework, PRISMA-ScR guidelines).

Key areas to cover:
1. Introduction to XAI and the black-box problem in healthcare ML
2. Rationale for explainability in high-stakes ICU decision-making (mortality prediction, sepsis detection, ventilator weaning, etc.)
3. Methodology: Scoping review protocol following Arksey & O'Malley (2005) and PRISMA-ScR
   - Search strategy across PubMed, IEEE Xplore, Scopus, Web of Science
   - Inclusion/exclusion criteria for XAI + ICU/critical care + ML studies
   - Data extraction and charting framework
4. Categorization of XAI methods found in ICU ML literature:
   - Model-agnostic methods (SHAP, LIME, permutation importance)
   - Model-specific methods (attention mechanisms, decision trees, rule extraction)
   - Concept-based explanations and prototype-based methods
5. Clinical applications where XAI has been deployed:
   - Mortality prediction (APACHE, SOFA-based models)
   - Sepsis early warning systems
   - Acute kidney injury prediction
   - Mechanical ventilation decisions
   - Drug dosing recommendations
6. Evaluation of XAI effectiveness:
   - Clinician trust and adoption studies
   - Fidelity and stability of explanations
   - Actionability of explanations for clinical workflow
7. Gaps and limitations identified in the literature
8. Discussion: Challenges for XAI in critical care (real-time requirements, multimodal data, regulatory considerations)
9. Future research directions and recommendations
"""

print(f"Topic: Explainable AI in ICU Machine Learning - Scoping Review")
print(f"Research Question: What XAI methods have been applied to ICU ML models...")
print("\nStarting generation...")

pdf_path, docx_path = generate_draft(
    topic=topic,
    language="en",
    academic_level="master",
    output_dir=OUTPUT_DIR,
    skip_validation=True,
    verbose=True
)

print("\nGeneration complete!")
print(f"PDF: {pdf_path}")
print(f"DOCX: {docx_path}")

# Create ZIP with both files
zip_path = OUTPUT_DIR / "thesis_7_xai_icu_review.zip"
with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
    if pdf_path.exists():
        zipf.write(pdf_path, pdf_path.name)
    if docx_path.exists():
        zipf.write(docx_path, docx_path.name)

print(f"\nZIP created: {zip_path}")
print("=" * 60)
print("THESIS 7 COMPLETE!")
print("=" * 60)
