# Starter Code: Agente con Tool Calling

class AgenteAutomatizacion:
    def __init__(self):
        self.herramientas = {}

    def registrar_herramienta(self, nombre: str, funcion):
        self.herramientas[nombre] = funcion

    def ejecutar_ciclo(self, instruccion_usuario: str):
        # TODO: Decidir qué herramienta invocar y ejecutar de forma segura
        pass
