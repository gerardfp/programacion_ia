import logging
import json
from typing import Dict, Any, Callable

logger = logging.getLogger(__name__)

def herramienta_consultar_stock(producto: str) -> str:
    """Herramienta registrada: Consulta el stock de un producto."""
    base_datos = {"laptop": 15, "teclado": 42, "monitor": 8}
    stock = base_datos.get(producto.lower(), 0)
    return f"El stock actual de '{producto}' es {stock} unidades."

class AgenteInteligenteSolucion:
    def __init__(self):
        self.herramientas: Dict[str, Callable] = {}
        self.historial_auditoria = []

    def registrar_herramienta(self, nombre: str, funcion: Callable):
        self.herramientas[nombre] = funcion
        logger.info("Herramienta '%s' registrada.", nombre)

    def ejecutar_accion(self, nombre_herramienta: str, **kwargs) -> Any:
        if nombre_herramienta not in self.herramientas:
            raise ValueError(f"Herramienta '{nombre_herramienta}' no autorizada.")
        
        logger.info("Ejecutando herramienta '%s' con argumentos: %s", nombre_herramienta, kwargs)
        resultado = self.herramientas[nombre_herramienta](**kwargs)
        
        # Auditoría
        self.historial_auditoria.append({
            "herramienta": nombre_herramienta,
            "args": kwargs,
            "resultado": resultado
        })
        return resultado

if __name__ == "__main__":
    agente = AgenteInteligenteSolucion()
    agente.registrar_herramienta("consultar_stock", herramienta_consultar_stock)
    res = agente.ejecutar_accion("consultar_stock", producto="laptop")
    print("Resultado del agente:", res)
    print("Auditoría:", agente.historial_auditoria)
