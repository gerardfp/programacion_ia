def fragmentar_texto(texto: str, tamano_chunk: int = 200, solapamiento: int = 50) -> list:
    chunks = []
    inicio = 0
    while inicio < len(texto):
        fin = inicio + tamano_chunk
        chunks.append(texto[inicio:fin])
        inicio += (tamano_chunk - solapamiento)
    return chunks
