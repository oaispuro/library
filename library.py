# Programa de Base de Datos de Biblioteca

# Crear una lista vacía para almacenar los libros
libros = []

# Función para agregar un nuevo libro a la lista
def agregar_libro():
    titulo = input("Ingrese el título del libro: ")
    autor = input("Ingrese el autor del libro: ")
    libros.append({"Título": titulo, "Autor": autor, "Disponible": True})
    print("¡Libro agregado con éxito!")

# Función para eliminar un libro de la lista
def eliminar_libro():
    titulo = input("Ingrese el título del libro que desea eliminar: ")
    for libro in libros:
        if libro["Título"].lower() == titulo.lower():
            libros.remove(libro)
            print("¡Libro eliminado con éxito!")
            return
    print("No se encontró el libro en la base de datos.")

# Función para buscar un libro por título o autor
def buscar_libro():
    opcion = input("¿Desea buscar por título (T) o autor (A)? ")
    if opcion.lower() == "t":
        titulo = input("Ingrese el título del libro que desea buscar: ")
        for libro in libros:
            if libro["Título"].lower() == titulo.lower():
                print("Título:", libro["Título"])
                print("Autor:", libro["Autor"])
                if libro["Disponible"]:
                    print("¡Libro disponible!")
                else:
                    print("Libro prestado.")
                return
        print("No se encontró el libro en la base de datos.")
    elif opcion.lower() == "a":
        autor = input("Ingrese el autor del libro que desea buscar: ")
        encontrados = []
        for libro in libros:
            if libro["Autor"].lower() == autor.lower():
                encontrados.append(libro)
        if encontrados:
            print("Libros encontrados por el autor", autor + ":")
            for libro in encontrados:
                print("Título:", libro["Título"])
                print("Autor:", libro["Autor"])
                if libro["Disponible"]:
                    print("¡Libro disponible!")
                else:
                    print("Libro prestado.")
        else:
            print("No se encontraron libros del autor", autor + ".")
    else:
        print("Opción inválida.")

# Función para verificar si un libro está disponible o prestado
def verificar_disponibilidad():
    titulo = input("Ingrese el título del libro que desea verificar: ")
    for libro in libros:
        if libro["Título"].lower() == titulo.lower():
            if libro["Disponible"]:
                print("El libro", libro["Título"], "está disponible.")
            else:
                print("El libro", libro["Título"], "ha sido prestado.")
            return
    print("No se encontró el libro en la base de datos.")

# Menú principal del programa
while True:
    print("\n-- Base de Datos de Biblioteca --")
    print("1. Agregar un libro")
    print("2. Eliminar un libro")
    print("3. Buscar un libro")
    print("4. Verificar disponibilidad de un libro")
    print("5. Salir del programa")
    opcion = input("Seleccione una opción (1-5): ")
    if opcion == "1":
        agregar_libro()
    elif opcion == "2":
        eliminar_libro()
    elif opcion == "3":
        buscar_libro()
    elif opcion == "4":
        verificar_disponibilidad()
    elif opcion == "5":
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
