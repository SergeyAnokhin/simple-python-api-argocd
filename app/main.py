from fastapi import FastAPI
from routers import items

app = FastAPI(title="simple-python-api-argocd", version="1.0.0")

app.include_router(items.router, prefix="/items")


@app.get("/")
def root():
    return {"status": "ok", "version": "1.0.1"}


@app.get("/health")
def health():
    return {"healthy": True}
