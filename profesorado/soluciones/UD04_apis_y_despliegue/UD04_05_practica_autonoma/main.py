from fastapi import FastAPI
app = FastAPI()
@app.post("/v1/generate")
def generate(): return {"status": "ok"}
