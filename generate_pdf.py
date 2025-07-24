from xhtml2pdf import pisa
from io import BytesIO
from html import escape

def create_pdf(text):
    result = BytesIO()
    html = f"<pre>{escape(text)}</pre>"
    pisa.CreatePDF(src=html, dest=result)
    return result.getvalue()
