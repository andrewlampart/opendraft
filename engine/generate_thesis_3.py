#!/usr/bin/env python3
"""Generate Thesis 3: Personalisation in web-based credit card application"""
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

OUTPUT_DIR = PROJECT_ROOT / "theses_output" / "thesis_3_credit_card_personalization"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

print("=" * 60)
print("THESIS 3: Personalisation in Web-Based Credit Card Application")
print("=" * 60)

topic = """The impact of personalisation options in a web-based credit card application - A longitudinal online controlled experiment"""

print(f"Topic: {topic}")
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

zip_path = OUTPUT_DIR / "thesis_3_credit_card_personalization.zip"
with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
    if pdf_path.exists():
        zipf.write(pdf_path, pdf_path.name)
    if docx_path.exists():
        zipf.write(docx_path, docx_path.name)

print(f"\nZIP created: {zip_path}")
print("=" * 60)
print("THESIS 3 COMPLETE!")
print("=" * 60)
