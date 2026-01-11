# Proyecto Día 6: Modelar Una Tienda De Mascotas

# Instrucciones: 
# 1) Crear una clase llamada Mascota. 

# 2) La clase Mascota debe tener las siguientes propiedades: 
#       - Nombre: El nombre de la mascota (una cadena de texto).
#       - Especie: La especie de la mascota (perro, gato, conejo, etc.) (una cadena de 
#         texto). 
#       - Edad: La edad de la mascota (un número entero). 
#       - Precio: El precio de la mascota (un número flotante). 
#       - Disponibilidad: Un valor booleano que indica si la mascota está disponible 
#         para la venta (True o False). 

# 3) La clase Mascota debe tener los siguientes métodos:  
#       - mostrar_info(): Muestra la información completa de la mascota (nombre, 
#         especie, edad, precio). 
#       - actualizar_precio(): Cambia el precio de la mascota. 
#       - actualizar_disponibilidad(): Cambia el estado de la propiedad disponibilidad 
#         a True o False, dependiendo de si la mascota está disponible para la venta. 
#       - vender(): Marca la mascota como vendida (no disponible para la venta). 
#       - devolver(): Cambia el estado de disponibilidad de la mascota a True (la 
#         mascota ha sido devuelta y está disponible nuevamente).

# Tu Código Aquí Debajo :)

class Mascota:
    def __init__(self, nombre, especie, edad, precio, disponibilidad=True):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        self.precio = precio
        self.disponibilidad = disponibilidad
    
    def mostrar_info(self):
        return f"Nombre: {self.nombre}\nEspecie: {self.especie}\nEdad: {self.edad}\nPrecio: ${self.precio}\nDisponible: {'Disponible' if self.disponibilidad else 'No disponible'}"
    
    def actualizar_precio(self, nuevo_precio):
        self.precio = nuevo_precio
    
    def actualizar_disponibilidad(self, disponibilidad):
        self.disponibilidad = disponibilidad
    
    def vender(self):
        if self.disponibilidad:
            self.disponibilidad = False
            print(f"{self.nombre} ha sido vendida.")
        else:
            print(f"{self.nombre} no está disponible para la venta.")

    def devolver(self):
        if not self.disponibilidad:
            self.disponibilidad = True
            print(f"{self.nombre} ha sido devuelta y está disponible nuevamente.")
        else:
            print(f"{self.nombre} ya está disponible.")

mascota1 = Mascota("Firulais", "Perro", 3, 150, True)
mascota2 = Mascota("Michi", "Gato", 2, 100, False)

print(mascota1.mostrar_info())
print(mascota2.mostrar_info())

mascota1.actualizar_precio(200)
print(mascota1.mostrar_info())

mascota1.vender()
print(mascota1.mostrar_info())

mascota1.devolver()
print(mascota1.mostrar_info())

mascota2.actualizar_disponibilidad(True)
print(mascota2.mostrar_info())

