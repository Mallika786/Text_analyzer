from flask import Flask, render_template, request, jsonify
from collections import Counter
import os

app = Flask(__name__)

# Route for home page
@app.route('/')
def home():
    return render_template('index.html')



# # Route to handle file upload
# @app.route('/upload', methods=['POST'])
# def upload_file():
#     if 'file' not in request.files:
#         return jsonify({'error': 'No file part'})
#     file = request.files['file']
#     if file.filename == '':
#         return jsonify({'error': 'No selected file'})

#     content = file.read().decode('utf-8')
#     lines = content.splitlines()
#     words = [word for line in lines for word in line.split()]
#     word_count = len(words)
#     character_count = len(content)
#     file_size = len(content.encode('utf-8'))
#     word_frequency = Counter(words)
#     most_frequent_word = word_frequency.most_common(1)[0] if word_frequency else ("None", 0)
#     unique_words_count = len(word_frequency)
#     longest_word = max(words, key=len) if words else " "

#     return jsonify({
#         'line_count': len(lines),
#         'word_count': word_count,
#         'character_count': character_count,
#         'file_size': file_size,
#         'most_frequent_word': most_frequent_word[0],
#         'most_frequent_word_count': most_frequent_word[1],
#         'unique_words_count': unique_words_count,
#         'longest_word': longest_word
#     })


# if __name__ == '__main__':
#     app.run(debug=True)

# from flask import Flask, render_template, request, jsonify
# from collections import Counter

#app = Flask(__name__)

# # Route for home page
# @app.route('/')
# def home():
#     return render_template('index.html')

# Route to handle text analysis
@app.route('/analyze', methods=['POST'])
def analyze_text():
    data = request.get_json()
    text = data.get('text', '')

    if not text:
        return jsonify({'error': 'No text provided'})

    # Perform text analysis
    lines = text.splitlines()
    words = [word for line in lines for word in line.split()]
    word_count = len(words)
    character_count = len(text)
    file_size = len(text.encode('utf-8'))
    word_frequency = Counter(words)
    most_frequent_word = word_frequency.most_common(1)[0] if word_frequency else ("None", 0)
    unique_words_count = len(word_frequency)
    longest_word = max(words, key=len) if words else "None"

    return jsonify({
        'line_count': len(lines),
        'word_count': word_count,
        'character_count': character_count,
        'file_size': file_size,
        'most_frequent_word': most_frequent_word[0],
        'most_frequent_word_count': most_frequent_word[1],
        'unique_words_count': unique_words_count,
        'longest_word': longest_word
    })

if __name__ == '__main__':
    app.run(debug=True)
