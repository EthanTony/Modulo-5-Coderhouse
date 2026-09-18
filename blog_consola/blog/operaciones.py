def listar_posts(lista):
    """Recorre la lista de posts e imprime su título, autor y estado."""
    print("\nPosts disponibles:")
    for post in lista:
        titulo = post.get("titulo", "[Sin Título]")
        estado = post.get("estado", "[Sin Estado]")
        
        autor_dict = post.get("autor")
        if isinstance(autor_dict, dict):
            nombre_autor = autor_dict.get("nombre", "Anónimo")
        else:
            nombre_autor = "Anónimo"
            
        print(f"- {titulo} | Autor: {nombre_autor} | Estado: {estado}")


def buscar_por_titulo(lista, termino):
    """Busca posts que coincidan con el término ignorando mayúsculas y minúsculas."""
    termino_lower = termino.lower()
    resultados = []
    
    for post in lista:
        titulo = post.get("titulo", "")
        if isinstance(titulo, str) and termino_lower in titulo.lower():
            resultados.append(post)
            
    return resultados


def filtrar_por_tag(lista, tag_buscado):
    """Filtra y devuelve posts que incluyan el tag ignorando mayúsculas/minúsculas."""
    tag_lower = tag_buscado.lower()
    resultados = []
    
    for post in lista:
        tags = post.get("tags", [])
        if isinstance(tags, list):
            tags_lower = [t.lower() for t in tags if isinstance(t, str)]
            if tag_lower in tags_lower:
                resultados.append(post)
                
    return resultados