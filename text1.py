from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

# Route for home page
@app.route('/')
def home():
    return render_template('index.html')

# Route to handle file upload
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})
    
    content = file.read().decode('utf-8')
    lines = content.splitlines()
    word_count = sum(len(line.split()) for line in lines)

    return jsonify({
        'line_count': len(lines),
        'word_count': word_count
    })

if __name__ == '__main__':
    app.run(debug=True)
