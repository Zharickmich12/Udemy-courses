# Instrucciones: 
# 1. Lista Inicial: 
# a. Crea una lista llamada lista_compras que contenga al menos tres productos. 
# Ejemplo: ["Pan", "Leche", "Huevos"]. 


# 2. Funciones: 
# a. mostrar_lista(): Esta función debe mostrar todos los productos en la lista. 

# Pista: Puedes usar un bucle para recorrer los elementos de la lista. Piensa en cómo 
# mostrar cada producto de manera clara para el usuario. 

# b. agregar_producto(nombre): Esta función debe agregar un producto a la lista 
# si no está repetido. Si el producto ya existe, debe mostrar un mensaje indicando 
# que el producto ya está en la lista. 

# Pista: Antes de agregar el producto, verifica si ya existe en la lista. Puedes utilizar un 
# condicional para comprobar si el producto ya está presente en la lista, y si no, 
# agregarlo. Usa el método in para hacer esa verificación. 

# c. eliminar_producto(nombre): Esta función debe eliminar un producto de la 
# lista si existe. Si el producto no está en la lista, debe mostrar un mensaje indicando 
# que no se encuentra. 

# Pista: Al igual que con la adición, antes de eliminar un producto, debes verificar si 
# existe en la lista. Si el producto está presente, puedes usar el método remove() 
# para eliminarlo. Si no está en la lista, asegúrate de dar un mensaje claro indicando 
# que no se puede eliminar. 


# 3. Mostrar los Resultados: 
# a. Después de cada operación, muestra el estado actual de la lista de compras. 

# Pista: Cada vez que se agregue o elimine un producto, asegúrate de mostrar la lista 
# actualizada. Puedes hacerlo simplemente llamando a la función 
# mostrar_lista() después de cada operación. 

# b. Asegúrate de que se muestren mensajes claros indicando si un producto fue 
# agregado o eliminado correctamente.

# Escribe tu código aquí debajo :)

lista_compras = ["Pan", "Leche", "Huevos"]

def mostrar_lista():
    print("Lista de compras actualizada:", lista_compras)

def agregar_producto(nombre):
    producto_existente = False
    for producto in lista_compras:
        if producto == nombre:
            producto_existente = True
            break  
    if producto_existente:
        print(f"El producto '{nombre}' ya está en la lista.")  
    else:
        lista_compras.append(nombre)
        print(f"Producto '{nombre}' agregado a la lista.")

def eliminar_producto(nombre):
    producto_existente = False
    for producto in lista_compras:
        if producto == nombre:
            producto_existente = True
            break
    if producto_existente:
        lista_compras.remove(nombre)
        print(f"Producto '{nombre}' eliminado de la lista.")
    else:
        print(f"El producto '{nombre}' no se encuentra en la lista.")

mostrar_lista()

#agregar_producto("Mantequilla")
#mostrar_lista() 

#eliminar_producto("Leche")
#mostrar_lista()