from fastapi import FastAPI

app = FastAPI(title="API Inferencia IA Starter")

@app.get("/")
def read_root():
    return {"message": "API Inferencia IA operativa"}

# TODO: Agregar endpoint POST /predict para recibir InferenciaInput
