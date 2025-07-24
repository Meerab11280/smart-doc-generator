from fpdf import FPDF
from io import BytesIO

def generate_pdf(text):
    try:
        pdf = FPDF()
        pdf.add_page()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.set_font("Arial", size=12)

        # Add each line of the text to the PDF
        for line in text.split('\n'):
            pdf.multi_cell(0, 10, line)

        # Save the PDF to a BytesIO buffer
        pdf_output = BytesIO()
        pdf.output(pdf_output)
        pdf_output.seek(0)

        return pdf_output.read()
    except Exception as e:
        print("PDF generation error:", e)
        return None
