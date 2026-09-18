perfil_autor = {
    "nombre": "Anto Aguilar",
    "bio": "Desarrollador web y antropólogo físico",
    "especialidad": "Python y Django",
    "redes_sociales": ["@antonio_de_merode", "@tony_python"]
}

# Constantes del sistema
estados_post = ("borrador", "publicado", "archivado")

# Set de etiquetas
etiquetas_blog = {"Python", "Django", "Web", "Backend", "Python"}

# Catálogo de posts
posts = [
    {
        "id": 1,
        "titulo": "Primeros pasos con Python",
        "contenido": "En este post veremos cómo empezar a programar con Python.",
        "autor": perfil_autor,
        "tags": ["Python", "Principiantes"],
        "estado": "publicado"
    },
    {
        "id": 2,
        "titulo": "Qué es Django",
        "contenido": "Django es un framework web creado con Python.",
        "autor": perfil_autor,
        "tags": ["Python", "Django", "Web"],
        "estado": "borrador"
    },
    {
        "id": 3,
        "titulo": "Organizando datos con listas",
        "contenido": "Las listas permiten guardar varios elementos en una sola variable.",
        "autor": perfil_autor,
        "tags": ["Python", "Listas"],
        "estado": "archivado"
    },
    # Post con error para probar las validaciones
    {
        "id": 4,
        "titulo": "Post incompleto de prueba",
        "autor": perfil_autor,
        "tags": "Python",  # Tipo incorrecto (string en vez de lista)
        "estado": "desconocido"
    }
]