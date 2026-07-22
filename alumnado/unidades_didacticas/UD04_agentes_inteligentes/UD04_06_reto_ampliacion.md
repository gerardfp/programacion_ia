# UD04 - Reto de Ampliación: Consulta SQL Segura a PostgreSQL

## Reto
Registrar una herramienta `consultar_base_datos(query_sql: str)` que conecte a un PostgreSQL local (`psycopg2` / `sqlalchemy`), valide mediante parseo AST que la consulta es estrictamente de lectura (`SELECT`) y devuelva el resultado en JSON.
