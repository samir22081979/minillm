# Embedding API with Flask

## How to Deploy on Railway

1. Upload this folder to [https://railway.app](https://railway.app)
2. Railway will auto-detect `requirements.txt` and `Procfile`.
3. Make sure port is set to 8080 (already handled in `embed_api.py`).
4. Use this to test:
   ```bash
   curl -X POST https://your-subdomain.up.railway.app/embed \
     -H "Content-Type: application/json" \
     -d '{"inputs": "Test your embedding"}'
   ```

Enjoy!