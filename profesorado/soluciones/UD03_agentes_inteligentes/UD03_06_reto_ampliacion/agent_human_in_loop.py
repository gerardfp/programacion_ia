class AgenteSeguro:
    def __init__(self, max_iterations: int = 5):
        self.max_iterations = max_iterations

    def ejecutar_con_confirmacion(self, accion: str) -> bool:
        return input(f"¿Autoriza '{accion}'? (s/n): ").lower() == 's'
