import fitz

def extract_pdf_text(uploads_file):
    pdf_bytes = uploads_file.read()
    doc = fitz.open(stream=pdf_bytes, filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text