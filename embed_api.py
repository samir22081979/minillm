from flask import Flask, request, jsonify
from sentence_transformers import SentenceTransformer
import os

app = Flask(__name__)
model = SentenceTransformer('all-MiniLM-L6-v2')

@app.route("/")
def index():
    return "Embedding API is running"

@app.route("/embed", methods=["POST"])
def embed():
    data = request.get_json()
    text = data.get("inputs", "")
    if not text:
        return jsonify({"error": "No input text provided"}), 400
    embedding = model.encode(text).tolist()
    return jsonify({"embedding": embedding})

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))  # Railway provides PORT env var
    app.run(host="0.0.0.0", port=port)
