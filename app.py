from flask import Flask, render_template, request, send_file
import os
from werkzeug.utils import secure_filename
from document_check.text import correct_txt
from document_check.doc import correct_doc
from document_check.pdf import correct_pdf
from input_livecheck.input import correct_live_input

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/correct_live', methods=['POST'])
def correct_live():
    content = request.form.get('content')
    corrected_content = correct_live_input(content)
    return {"corrected_content": corrected_content}

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    file_type = request.form.get('file_type')
    filename = secure_filename(file.filename)
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(file_path)
    
    output_path = os.path.join(app.config['UPLOAD_FOLDER'], f"corrected_{filename}")
    
    if file_type == 'docx':
        corrected_path = correct_doc(file_path, output_path)
    elif file_type == 'pdf':
        corrected_path = correct_pdf(file_path, output_path)
    elif file_type == 'txt':
        corrected_path = correct_txt(file_path, output_path)
    else:
        return {"error": "Unsupported file type."}, 400
    
    return {"download_link": corrected_path}

@app.route('/download/<path:filename>')
def download(filename):
    return send_file(filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
