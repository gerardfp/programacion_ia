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
    print("--- INICIANDO VERIFICACIÓN COMPLETA DE ESTRUCTURA EN PROGRAMACION_IA ---")
    root_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    
    unidades = [
        ("UD01_python_profesional", "UD01"),
        ("UD02_servicios_ia_locales", "UD02"),
        ("UD03_aplicaciones_rag", "UD03"),
        ("UD04_agentes_inteligentes", "UD04"),
        ("UD05_apis_y_despliegue", "UD05"),
        ("UD06_proyecto_final", "UD06")
    ]

    docs_alumnado = [
        "00_preparacion.md",
        "01_material.md",
        "02_presentacion.md",
        "03_actividad_inicial.md",
        "04_practica_guiada.md",
        "05_practica_autonoma.md",
        "06_reto_ampliacion.md"
    ]

    actividades_soluciones = [
        "03_actividad_inicial",
        "04_practica_guiada",
        "05_practica_autonoma",
        "06_reto_ampliacion"
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
    for ud_folder, prefix in unidades:
        print(f"\n -> [Alumnado] Comprobando {ud_folder}:")
        for doc in docs_alumnado:
            doc_filename = f"{prefix}_{doc}"
            file_path = os.path.join(root_dir, "alumnado", "unidades_didacticas", ud_folder, doc_filename)
            if not check_file_exists(file_path):
                errores += 1

    print("\n3. Verificando documentos unificados Markdown del PROFESORADO...")
    for ud_folder, _ in unidades:
        file_path = os.path.join(root_dir, "profesorado", "unidades_didacticas", f"{ud_folder}.md")
        if not check_file_exists(file_path):
            errores += 1

    print("\n4. Verificando carpetas de SOLUCIONES por UNIDAD y CÓDIGO DE ACTIVIDAD...")
    for ud_folder, prefix in unidades:
        print(f"\n -> [Soluciones] Comprobando {ud_folder}:")
        for act in actividades_soluciones:
            act_folder = f"{prefix}_{act}"
            sol_path = os.path.join(root_dir, "profesorado", "soluciones", ud_folder, act_folder)
            if not check_file_exists(sol_path):
                errores += 1

    print("\n------------------------------------------------------------")
    if errores == 0:
        print("VERIFICACIÓN EXITOSA: Todas las carpetas de soluciones por actividad (profesorado/soluciones/UDXX_.../UDXX_YY_...) están íntegras.")
        sys.exit(0)
    else:
        print(f"VERIFICACIÓN FALLIDA: Se encontraron {errores} ausencias.")
        sys.exit(1)

if __name__ == "__main__":
    main()
