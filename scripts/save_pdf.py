from fpdf import FPDF

def save_minutes_pdf(content, pdf_path):
    pdf = FPDF()
    pdf.add_page()

    # Load the Unicode-compatible font clearly
    pdf.add_font("DejaVu", style="", fname="DejaVuSans.ttf", uni=True)
    pdf.set_font("DejaVu", size=12)

    # Write content clearly with Unicode support
    pdf.multi_cell(0, 10, txt=content)

    # Save the generated PDF file
    pdf.output(pdf_path)
