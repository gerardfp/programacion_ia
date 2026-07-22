import sys
import os

def check_file_exists(path: str) -> bool:
    if os.path.exists(path):
        print(f"  [OK] Encontrado: {os.path.basename(os.path.dirname(path))}/{os.path.basename(path)}")
        return True
    else:
        print(f"  [FAIL] Falta: {path}")
        return False

def main():
    print("--- INICIANDO VERIFICACIÓN COMPLETA DE DOCUMENTOS MD EN PROGRAMACION_IA ---")
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    unidades = [
        "UD01_python_profesional",
        "UD02_servicios_ia_locales",
        "UD03_aplicaciones_rag",
        "UD04_agentes_inteligentes",
        "UD05_apis_y_despliegue",
        "UD06_proyecto_final"
    ]

    documentos_estandar = [
        "00_indice.md",
        "01_guia_profesor.md",
        "02_material_alumno.md",
        "03_presentacion.md",
        "04_actividad_inicial.md",
        "05_practica_guiada.md",
        "06_practica_autonoma.md",
        "07_reto_ampliacion.md",
        "08_evaluacion.md",
        "09_rubrica.md"
    ]

    errores = 0

    print("\n1. Verificando documentos macro...")
    archivos_macro = [
        os.path.join(base_dir, "course-manifest.yaml"),
        os.path.join(base_dir, "README.md"),
        os.path.join(base_dir, "programacion_docente", "programacion_general.md"),
        os.path.join(base_dir, "programacion_docente", "resultados_aprendizaje.md"),
        os.path.join(base_dir, "programacion_docente", "criterios_evaluacion.md"),
        os.path.join(base_dir, "programacion_docente", "temporalizacion.md"),
        os.path.join(base_dir, "programacion_docente", "mapa_competencias.md"),
    ]
    for file_path in archivos_macro:
        if not check_file_exists(file_path):
            errores += 1

    print("\n2. Verificando los 10 documentos Markdown por cada Unidad Didáctica...")
    for ud in unidades:
        print(f"\n -> Comprobando {ud}:")
        for doc in documentos_estandar:
            file_path = os.path.join(base_dir, "unidades_didacticas", ud, doc)
            if not check_file_exists(file_path):
                errores += 1

    print("\n------------------------------------------------------------")
    if errores == 0:
        print("VERIFICACIÓN EXITOSA: Los 60 documentos .md de las 6 UDs y los archivos macro existen.")
        sys.exit(0)
    else:
        print(f"VERIFICACIÓN FALLIDA: Se encontraron {errores} ausencias.")
        sys.exit(1)

if __name__ == "__main__":
    main()
