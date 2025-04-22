
from flask import Flask, request, jsonify
from sentence_transformers import SentenceTransformer

app = Flask(__name__)
model = SentenceTransformer('all-MiniLM-L6-v2')

@app.route('/embed', methods=['POST'])
def embed():
    data = request.get_json()
    text = data.get('inputs', '')
    if not text:
        return jsonify({'error': 'No input text provided'}), 400
    embedding = model.encode(text).tolist()
    return jsonify({'embedding': embedding})
