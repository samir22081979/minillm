FROM python:3.10-slim
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install huggingface_hub[s3] sentence-transformers flask
EXPOSE 8080
CMD ["python", "embed_api.py"]
