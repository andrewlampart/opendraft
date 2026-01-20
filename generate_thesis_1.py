#!/usr/bin/env python3
"""Generate Thesis 1: Self-financing portfolio with sustainability aspects"""
import os
import sys
import zipfile
from pathlib import Path

# Use relative paths for portability
PROJECT_ROOT = Path(__file__).parent.absolute()
sys.path.insert(0, str(PROJECT_ROOT))
os.chdir(PROJECT_ROOT)

from engine.draft_generator import DraftGenerator

OUTPUT_DIR = PROJECT_ROOT / "theses_output" / "thesis_1_sustainability_portfolio"
os.makedirs(OUTPUT_DIR, exist_ok=True)

print("=" * 60)
print("THESIS 1: Self-Financing Portfolio with Sustainability")
print("=" * 60)

topic = """The self-financing portfolio with additional consideration of sustainability aspects between 2010 and 2020 - A performance analysis

This thesis examines the construction and performance of self-financing portfolios that incorporate Environmental, Social, and Governance (ESG) criteria during the period 2010-2020. The research analyzes:
1. Theoretical foundations of self-financing portfolios and ESG integration
2. Methodology for constructing ESG-weighted self-financing strategies
3. Empirical performance comparison against traditional benchmarks
4. Risk-return characteristics and Sharpe ratios
5. Impact of different ESG scoring methodologies
6. Sector allocation effects and sustainability tilts
7. Transaction costs and rebalancing frequency implications
8. Market conditions and their effect on sustainable portfolio performance"""

print(f"Topic: {topic[:100]}...")
print("\nStarting generation...")

generator = DraftGenerator()
draft = generator.generate(
    topic=topic,
    paper_type="master",
    language="en"
)

print("\nGeneration complete! Exporting files...")

# Export files
pdf_path = os.path.join(OUTPUT_DIR, "thesis_sustainability_portfolio.pdf")
docx_path = os.path.join(OUTPUT_DIR, "thesis_sustainability_portfolio.docx")
tex_path = os.path.join(OUTPUT_DIR, "thesis_sustainability_portfolio.tex")

draft.to_pdf(pdf_path)
print(f"PDF saved: {pdf_path}")

draft.to_docx(docx_path)
print(f"DOCX saved: {docx_path}")

draft.to_latex(tex_path)
print(f"LaTeX saved: {tex_path}")

# Create ZIP
zip_path = os.path.join(OUTPUT_DIR, "thesis_1_sustainability_portfolio.zip")
with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
    zipf.write(pdf_path, os.path.basename(pdf_path))
    zipf.write(docx_path, os.path.basename(docx_path))
    zipf.write(tex_path, os.path.basename(tex_path))

print(f"\nZIP created: {zip_path}")
print("=" * 60)
print("THESIS 1 COMPLETE!")
print("=" * 60)
