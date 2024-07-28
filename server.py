from flask import Flask, request, jsonify
import os
import extract_from_transcript
import math_studies_check

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/upload', methods=['POST'])
def upload_file():
    print("Request received")
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected for uploading'}), 400
    
    filename = file.filename
    print(app.config['UPLOAD_FOLDER'])
    path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(path)
    print(path)
    print(math_studies_check.return_missing_courses(path))
    # print(extract_from_transcript.extract_all_information(path))

    return jsonify({'message': 'File successfully uploaded'}), 200

if __name__ == '__main__':
    app.run(debug=True,port=8000)