#!/usr/bin/env python3
"""Generate Thesis 8: Virtual Influencers - Autonomy, Interactivity, and Consumer Behavior"""
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

OUTPUT_DIR = PROJECT_ROOT / "theses_output" / "thesis_8_virtual_influencers"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

print("=" * 60)
print("THESIS 8: Virtual Influencers - Autonomy & Interactivity")
print("=" * 60)

topic = """The Impact of Autonomy and Interactivity of Virtual Influencers on Consumer Attitudes and Behavioral Intentions

Research Question: How do perceived autonomy and interactivity of virtual influencers (AI-generated digital personas) affect consumer attitudes, trust, and behavioral intentions compared to human influencers?

Key areas to cover:
1. Introduction to virtual influencers (Lil Miquela, Imma, Shudu, etc.) and their rise in digital marketing
2. Literature review:
   - Influencer marketing theory and source credibility
   - Parasocial interaction theory and relationships with virtual entities
   - Uncanny valley effect and anthropomorphism
   - Technology acceptance and perceived autonomy
   - Consumer-brand relationships in digital contexts
3. Theoretical framework:
   - Perceived autonomy (AI vs human-controlled)
   - Interactivity dimensions (responsiveness, customization, engagement)
   - Authenticity perceptions and trust formation
4. Methodology: Quantitative experimental design
   - Survey/experimental manipulation of autonomy levels
   - Measurement of attitudes, purchase intention, brand trust
   - Control variables (prior experience, technology readiness)
5. Hypotheses on:
   - Autonomy → perceived authenticity → trust
   - Interactivity → parasocial relationship → purchase intention
   - Moderating role of consumer technology readiness
6. Results analysis using SEM/PLS or regression
7. Discussion of findings in context of influencer marketing evolution
8. Implications for brands using virtual influencers
9. Ethical considerations (disclosure, transparency, manipulation)
"""

print(f"Topic: Virtual Influencers - Autonomy & Interactivity")
print(f"Research Question: Impact on consumer attitudes and behavioral intentions...")
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
zip_path = OUTPUT_DIR / "thesis_8_virtual_influencers.zip"
with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
    if pdf_path.exists():
        zipf.write(pdf_path, pdf_path.name)
    if docx_path.exists():
        zipf.write(docx_path, docx_path.name)

print(f"\nZIP created: {zip_path}")
print("=" * 60)
print("THESIS 8 COMPLETE!")
print("=" * 60)
