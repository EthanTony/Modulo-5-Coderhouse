from blog.datos import estados_post

def validar_post(post):
    """
    Comprueba si un post cumple con la estructura requerida.
    Retorna una tupla: (es_valido: bool, mensaje: str)
    """
    if not isinstance(post, dict):
        return False, "El post no es un diccionario"
    
    claves_obligatorias = ["id", "titulo", "contenido", "autor", "tags", "estado"]
    for clave in claves_obligatorias:
        if clave not in post:
            return False, f"Falta la clave obligatoria '{clave}'"
            
    if not isinstance(post["titulo"], str) or post["titulo"].strip() == "":
        return False, "El 'titulo' está vacío o no es texto"
        
    if not isinstance(post["contenido"], str) or post["contenido"].strip() == "":
        return False, "El 'contenido' está vacío o no es texto"
        
    if not isinstance(post["autor"], dict):
        return False, "El 'autor' debe ser un diccionario"
        
    if "nombre" not in post["autor"] or not post["autor"]["nombre"]:
        return False, "El autor debe incluir la clave 'nombre'"
        
    if not isinstance(post["tags"], list):
        return False, "Los 'tags' deben estar guardados en una lista"
        
    if post["estado"] not in estados_post:
        return False, f"Estado '{post['estado']}' no es válido ({estados_post})"
        
    return True, "Válido"