from docx import Document

def read_file(filepath):

    if filepath.endswith(".txt"):

        with open(filepath, "r", encoding="utf-8") as file:
            return file.read()

    elif filepath.endswith(".docx"):

        doc = Document(filepath)

        text = ""

        for para in doc.paragraphs:
            text += para.text + "\n"

        return text

    return ""