import sys
import os

def check_file_exists(path: str) -> bool:
    if os.path.exists(path):
        rel_path = os.path.relpath(path, start=os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
        print(f"  [OK] Encontrado: {rel_path}")
        return True
    else:
        print(f"  [FAIL] Falta: {path}")
        return False

def main():
    print("--- INICIANDO VERIFICACIÓN COMPLETA DE ESTRUCTURA DUAL EN PROGRAMACION_IA ---")
    root_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    
    unidades = [
        "UD01_python_profesional",
        "UD02_servicios_ia_locales",
        "UD03_aplicaciones_rag",
        "UD04_agentes_inteligentes",
        "UD05_apis_y_despliegue",
        "UD06_proyecto_final"
    ]

    docs_alumnado = [
        "02_material_alumno.md",
        "03_presentacion.md",
        "04_actividad_inicial.md",
        "05_practica_guiada.md",
        "06_practica_autonoma.md",
        "07_reto_ampliacion.md"
    ]

    docs_profesorado = [
        "00_indice.md",
        "01_guia_profesor.md",
        "08_evaluacion.md",
        "09_rubrica.md"
    ]

    errores = 0

    print("\n1. Verificando documentos macro y raíces...")
    archivos_macro = [
        os.path.join(root_dir, "course-manifest.yaml"),
        os.path.join(root_dir, "README.md"),
        os.path.join(root_dir, "alumnado", "README.md"),
        os.path.join(root_dir, "profesorado", "README.md"),
        os.path.join(root_dir, "profesorado", "programacion_docente", "programacion_general.md"),
        os.path.join(root_dir, "profesorado", "programacion_docente", "resultados_aprendizaje.md"),
        os.path.join(root_dir, "profesorado", "programacion_docente", "criterios_evaluacion.md"),
        os.path.join(root_dir, "profesorado", "programacion_docente", "temporalizacion.md"),
        os.path.join(root_dir, "profesorado", "programacion_docente", "mapa_competencias.md"),
    ]
    for file_path in archivos_macro:
        if not check_file_exists(file_path):
            errores += 1

    print("\n2. Verificando documentos del ALUMNADO por cada Unidad Didáctica...")
    for ud in unidades:
        print(f"\n -> [Alumnado] Comprobando {ud}:")
        for doc in docs_alumnado:
            file_path = os.path.join(root_dir, "alumnado", "unidades_didacticas", ud, doc)
            if not check_file_exists(file_path):
                errores += 1

    print("\n3. Verificando documentos del PROFESORADO por cada Unidad Didáctica...")
    for ud in unidades:
        print(f"\n -> [Profesorado] Comprobando {ud}:")
        for doc in docs_profesorado:
            file_path = os.path.join(root_dir, "profesorado", "unidades_didacticas", ud, doc)
            if not check_file_exists(file_path):
                errores += 1

    print("\n------------------------------------------------------------")
    if errores == 0:
        print("VERIFICACIÓN EXITOSA: La estructura dual (alumnado/profesorado) está íntegra y completa.")
        sys.exit(0)
    else:
        print(f"VERIFICACIÓN FALLIDA: Se encontraron {errores} ausencias.")
        sys.exit(1)

if __name__ == "__main__":
    main()
