from document_reader import extract_text


file_path = "test_resume.docx"

text = extract_text(file_path)

print("Extracted Text:")
print(text)