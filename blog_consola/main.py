# main.py

from blog.datos import posts
from blog.menu import mostrar_menu
from blog.operaciones import listar_posts, buscar_por_titulo, filtrar_por_tag
from blog.validaciones import validar_post


def ejecutar_sistema():
    """Coordina el flujo interactivo del sistema de blog."""
    while True:
        opcion = mostrar_menu()
        
        # OPCIÓN 1: Ver todos los posts
        if opcion == 1:
            listar_posts(posts)
            
        # OPCIÓN 2: Buscar por título
        elif opcion == 2:
            termino = input("\nIngresa el término a buscar en los títulos: ").strip()
            resultados = buscar_por_titulo(posts, termino)
            
            print(f"\nResultados de búsqueda para '{termino}':")
            if resultados:
                for post in resultados:
                    print(f"- {post['titulo']}")
            else:
                print("No se encontraron coincidencias.")
                
        # OPCIÓN 3: Filtrar por tag
        elif opcion == 3:
            tag = input("\nIngresa el tag a filtrar: ").strip()
            resultados = filtrar_por_tag(posts, tag)
            
            print(f"\nPosts con el tag '{tag}':")
            if resultados:
                for post in resultados:
                    print(f"- {post['titulo']}")
            else:
                print("No se encontraron posts con ese tag.")
                
        # OPCIÓN 4: Validar posts
        
        elif opcion == 4:
            print("\n--- AUDITORÍA Y VALIDACIÓN DE POSTS ---")
            for post in posts:
                post_id = post.get("id", "Sin ID")
                es_valido, mensaje = validar_post(post)
                
                if es_valido:
                    print(f"Post {post_id}: Válido")
                else:
                    print(f"Post {post_id}: Error -> {mensaje}")
                    
        # OPCIÓN 5: Salir
        elif opcion == 5:
            print("\nGracias por usar el sistema del blog. ¡Hasta luego!")
            break
            
        # Control de opciones fuera de rango o errores de tipo
        else:
            print("\nOpción inválida, intenta de nuevo")


if __name__ == "__main__":
    ejecutar_sistema()