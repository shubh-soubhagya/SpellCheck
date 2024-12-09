from spellchecker import SpellChecker
from PyPDF2 import PdfReader, PdfWriter

def correct_pdf(file_path, output_path):
    spell = SpellChecker()
    reader = PdfReader(file_path)
    writer = PdfWriter()
    
    for page in reader.pages:
        text = page.extract_text()
        words = text.split()
        corrected = [spell.correction(word) if word not in spell else word for word in words]
        corrected_text = ' '.join(corrected)
        writer.add_page(writer.add_blank_page().add_text(corrected_text))
    
    with open(output_path, "wb") as corrected_pdf:
        writer.write(corrected_pdf)
    
    return output_path
