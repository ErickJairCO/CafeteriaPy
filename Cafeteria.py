
class Articulo:
    def __init__(self, nombre, marca, metrica, caducidad):
        self.nombre = nombre
        self.marca = marca
        self.metrica = metrica
        self.caducidad = caducidad

class Inventario:
    def __init__(self):
        self.lista_inventario = []
        self.cargar_inventario()
    
    def cargar_inventario(self, nombre_archivo="inventario.txt"):
        try:
            with open(nombre_archivo, "r") as archivo:
                for linea in archivo:
                    # Separar la línea en partes usando ',' como delimitador
                    partes = linea.strip().split(", ")
                    
                    # Crear un diccionario para representar un elemento del inventario
                    nuevo_inventario = {
                        "articulo": Articulo(
                            nombre=partes[0].split(": ")[1],
                            marca=partes[1].split(": ")[1],
                            metrica=partes[2].split(": ")[1],
                            caducidad=partes[3].split(": ")[1]
                        ),
                        "cantidad": int(partes[4].split(": ")[1]),
                        "fecha_entrada": partes[5].split(": ")[1]
                    }

                    # Agregar el elemento del inventario a la lista
                    self.lista_inventario.append(nuevo_inventario)

            print(f"Inventario cargado desde {nombre_archivo}.")
        except FileNotFoundError:
            print(f"El archivo {nombre_archivo} no existe. Se creará uno nuevo al guardar el inventario.")

    def añadir_inventario(self):
        nombre = input("Ingrese el nombre del artículo: ")
        marca = input("Ingrese la marca del artículo: ")
        metrica = input("Ingrese la unidad métrica del artículo: ")
        caducidad = input("Ingrese la fecha de caducidad del artículo: ")

        nuevo_articulo = Articulo(nombre, marca, metrica, caducidad)
        cantidad = int(input("Ingrese la cantidad del artículo en inventario: "))
        fecha_entrada = input("Ingrese la fecha de entrada del artículo: ")

        nuevo_inventario = {"articulo": nuevo_articulo, "cantidad": cantidad, "fecha_entrada": fecha_entrada}
        self.lista_inventario.append(nuevo_inventario)

        print("Artículo añadido al inventario.")

    def mostrar_inventario(self):
        for index, item in enumerate(self.lista_inventario, start=1):
            print(f"\nArtículo {index}:")
            print(f"Nombre: {item['articulo'].nombre}")
            print(f"Marca: {item['articulo'].marca}")
            print(f"Métrica: {item['articulo'].metrica}")
            print(f"Caducidad: {item['articulo'].caducidad}")
            print(f"Cantidad: {item['cantidad']}")
            print(f"Fecha de entrada: {item['fecha_entrada']}")

    def modificar_inventario(self):
        self.mostrar_inventario()
        index = int(input("Ingrese el número del artículo que desea modificar: ")) - 1

        if 0 <= index < len(self.lista_inventario):
            cantidad_nueva = int(input("Ingrese la nueva cantidad del artículo en inventario: "))
            fecha_nueva = input("Ingrese la nueva fecha de entrada del artículo: ")

            self.lista_inventario[index]["cantidad"] = cantidad_nueva
            self.lista_inventario[index]["fecha_entrada"] = fecha_nueva

            print("Inventario modificado exitosamente.")
        else:
            print("Número de artículo no válido.")

    def eliminar_inventario(self):
        self.mostrar_inventario()
        index = int(input("Ingrese el número del artículo que desea eliminar: ")) - 1

        if 0 <= index < len(self.lista_inventario):
            confirmacion = input("¿Estas seguro de querer eliminar este articulo del inventario? (Sí/No): ").lower()
            if confirmacion == "sí" or confirmacion == "si":
                del self.lista_inventario[index]
                print("Artículo eliminado del inventario.")
            else:
                pass
        else:
            print("Número de artículo no válido.")

    def guardar_inventario(self, nombre_archivo="inventario.txt"):
        with open(nombre_archivo, "w") as archivo:
            for item in self.lista_inventario:
                archivo.write(f"Nombre: {item['articulo'].nombre}, Marca: {item['articulo'].marca}, "
                              f"Métrica: {item['articulo'].metrica}, Caducidad: {item['articulo'].caducidad}, "
                              f"Cantidad: {item['cantidad']}, Fecha de entrada: {item['fecha_entrada']}\n")

        print(f"Inventario guardado en {nombre_archivo}.")

if __name__ == "__main__":
    inventario = Inventario()
    guardado = True

    while True:
        print("\n----- Menú -----")
        print("1. Añadir al inventario")
        print("2. Mostrar inventario")
        print("3. Modificar inventario")
        print("4. Eliminar del inventario")
        print("5. Guardar inventario en archivo")
        print("0. Salir")

        opcion = input("Seleccione una opción (0-5): ")

        if opcion == "1":
            inventario.añadir_inventario()
            guardado = False
        elif opcion == "2":
            inventario.mostrar_inventario()
        elif opcion == "3":
            inventario.modificar_inventario()
            guardado = False
        elif opcion == "4":
            inventario.eliminar_inventario()
            guardado = False
        elif opcion == "5":
            inventario.guardar_inventario()
            guardado = True
        elif opcion == "0":
            if(guardado == False):
                confirmacion = input("¿Desea guardar los cambios del inventario antes de salir? (Sí/No): ").lower()
                if confirmacion == "sí" or confirmacion == "si":
                    inventario.guardar_inventario()
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Inténtelo de nuevo.")
