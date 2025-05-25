FROM python:3.9-slim

RUN pip install fastapi uvicorn sentence-transformers

COPY embed_server.py .

CMD ["uvicorn", "embed_server:app", "--host", "0.0.0.0", "--port", "8001"]