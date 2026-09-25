import re

def clean_resume_text(text: str) -> str:
    text = re.sub(r"\n+", "\n", text)  # Replace multiple newlines with a single newline
    text = re.sub(r"\s+", " ", text)  # Replace multiple whitespace with a single space
    return text