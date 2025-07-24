from xhtml2pdf import pisa
from io import BytesIO

def create_pdf(content: str) -> BytesIO:
    pdf_file = BytesIO()
    html = f"<pre style='font-family: Arial; font-size: 12pt'>{content}</pre>"
    pisa.CreatePDF(html, dest=pdf_file)
    pdf_file.seek(0)
    return pdf_file
