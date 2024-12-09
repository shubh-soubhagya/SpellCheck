from spellchecker import SpellChecker
from docx import Document

def correct_doc(file_path, output_path):
    spell = SpellChecker()
    doc = Document(file_path)
    
    for paragraph in doc.paragraphs:
        words = paragraph.text.split()
        corrected = [spell.correction(word) if word not in spell else word for word in words]
        paragraph.text = ' '.join(corrected)
    
    doc.save(output_path)
    return output_path
