from fastapi import FastAPI, Request
from sentence_transformers import SentenceTransformer
from pydantic import BaseModel
from typing import List

app = FastAPI()
model = SentenceTransformer("cointegrated/LaBSE-en-ru")

class TextRequest(BaseModel):
    texts: List[str]

@app.post("/embed")
async def embed(req: TextRequest):
    vectors = model.encode(req.texts, normalize_embeddings=True)
    return {"embeddings": vectors.tolist()}
