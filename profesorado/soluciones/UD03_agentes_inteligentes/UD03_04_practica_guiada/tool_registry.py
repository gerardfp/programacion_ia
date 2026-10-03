from pydantic import BaseModel, Field

class StockQueryInput(BaseModel):
    producto_id: str = Field(..., description="ID del producto")

def consultar_stock(input_data: StockQueryInput) -> int:
    return 42

HERRAMIENTAS = {"consultar_stock": {"func": consultar_stock, "schema": StockQueryInput}}
