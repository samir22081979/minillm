from sentence_transformers import SentenceTransformer
from flask import Flask, request, jsonify

app = Flask(__name__)
model = SentenceTransformer('all-MiniLM-L6-v2')  # This model outputs 384-dim vectors

@app.route('/embed', methods=['POST'])
def embed():
    data = request.get_json()
    text = data.get("inputs", "")
    
    # Get full vector (e.g. 384 dims)
    full_embedding = model.encode(text).tolist()

    # Slice to 144 dims
    trimmed_embedding = full_embedding[:144]

    return jsonify({
        "embedding": trimmed_embedding
    })

@app.route('/')
def home():
    return "Embedding API is running"

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
