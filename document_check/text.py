from spellchecker import SpellChecker

def correct_txt(file_path, output_path):
    """
    Corrects spelling errors in a .txt file and saves the corrected content.
    :param file_path: Path to the input .txt file.
    :param output_path: Path to save the corrected .txt file.
    :return: Path to the corrected file.
    """
    spell = SpellChecker()
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    corrected_lines = []
    for line in lines:
        words = line.split()
        corrected = [spell.correction(word) if word not in spell else word for word in words]
        corrected_lines.append(' '.join(corrected))
    
    with open(output_path, 'w') as corrected_file:
        corrected_file.write('\n'.join(corrected_lines))
    
    return output_path
