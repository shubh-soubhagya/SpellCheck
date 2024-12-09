from spellchecker import SpellChecker

def correct_live_input(content):
    spell = SpellChecker()
    words = content.split()
    corrected = [spell.correction(word) if word not in spell else word for word in words]
    return ' '.join(corrected)
