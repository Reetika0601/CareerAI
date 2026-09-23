import os

from pypdf import PdfReader
from docx import Document


def extract_pdf_text(file_path):
    """
    Extract text from a PDF file.
    """

    reader = PdfReader(file_path)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text


def extract_docx_text(file_path):
    """
    Extract text from a DOCX file.
    """

    document = Document(file_path)

    text = ""

    for paragraph in document.paragraphs:
        text += paragraph.text + "\n"

    return text


def extract_txt_text(file_path):
    """
    Extract text from a TXT file.
    """

    with open(
        file_path,
        "r",
        encoding="utf-8"
    ) as file:

        return file.read()


def extract_text(file_path):
    """
    Detect the file type and extract its text.
    """

    extension = os.path.splitext(
        file_path
    )[1].lower()

    if extension == ".pdf":

        return extract_pdf_text(file_path)

    elif extension == ".docx":

        return extract_docx_text(file_path)

    elif extension == ".txt":

        return extract_txt_text(file_path)

    else:

        raise ValueError(
            "Unsupported file format. "
            "Please upload PDF, DOCX, or TXT."
        )