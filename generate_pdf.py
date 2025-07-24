from xhtml2pdf import pisa
from io import BytesIO
from html import escape

def create_pdf(text):
    result = BytesIO()
    html = f"""
    <html>
    <head>
        <style>
            pre {{
                font-family: Arial, sans-serif;
                font-size: 12pt;
                line-height: 1.6;
                margin: 30px;
            }}
        </style>
    </head>
    <body>
        <pre>{escape(text)}</pre>
    </body>
    </html>
    """
    pisa.CreatePDF(src=html, dest=result)
    return result.getvalue()

