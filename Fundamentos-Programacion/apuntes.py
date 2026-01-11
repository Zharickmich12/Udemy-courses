# ¿Que es la programación? Es el proceso de diseñar y escribir insrucciones para que una computadora las pueda ejecutar.
# ¿Que es un programa? Serie de isntrucciones que le va a decir a la computadora como hacer una determinada tarea.
# ¿Que implica programar? 1. ¿cuál es el problema? 2. Planificar la solución 3. Codificar la solución 4. Probar y depurar 5. Mantenimiento
# ¿Que significa compilar? Se refiere al proceso de tomar el código escrito en un lenguaje de programación y traducirlo a un lenguaje maquina o a un formato que pueda ser ejecutado por la computadora
# Compilador: 1. Recibe todo el código junto 2. Verifica que esté todo OK 3. Ejecuta el código
# Interprete: 1. Leer la primera línea de código 2. Interpretarla 3. Si no hay errores, ejecuta el código
# Ciclo de vida de un programa: 1. Analizar 2. Diseño 3. Codificar 4. Pruebas/test 5. Mantenimiento.
# ¿Que es un algoritmo? Una serie de pasos ordenados, que siguen un camino lógico para resolver un problemas. 1. Debe ser preciso 2. Debe ser ordenado 3. Debe ser eficiente
# Diagramas de flujo: guía o mapa que permite ver gráfica o visualmente como se ejecuta un programa. óvalo: INICIO - FIN rectángulo: acciones rombo: desiciones si - no flechas: conectores
# Tipos de datos
# String: cadena de caractéres
# Datos numéricos: Integers(enteros): números sin decimales , Float(decimales)
# Booleano: solo puede ser True o False
# Character: representa un caracter
# Array : conjunto de elementos del mismo tipo akmacenados en una secuencia
# Object: representa una colección de datos que puede ser de diferentes tipos
# NULL: representa ausencia de valor
# Undefined: valor predeterminado de las variables que no han sido incializadas
# Variables
# Una variable es un espacionen memoria que se utiliza para alamacenar algún tipo de dato
# nombre = valor
# Condicionales
# condicional if: estructura que le permite al programa tomar una desición
# Simbolos
# > mayor que
# < menor que
# == igualdad
# >= mayor o igual que
# <= menor o igual que
# condicionales and y or: permiten crear condicionales si se cumplen varias condiciones al mismo tiempo
# and: dos condiciones tienen que ser verdaderas
# or: solo una condición debe ser verdadera
# condicional else: indica que sucede cuando la condición principal no se cumple 
# if (condición):
#  print ("codigo")
# else:
#  print ("codigo")
# elif: abreviatura del if y el else, agrega otro conicional if
# not: operador que invierte el valor lógico de una condición
# bucles: iteracion, proceso que se repite varias veces
# bucle for: repite una tarea un número determinado de veces
# partes de un bucle for:
# 1. inicialización: variable que controla el bucle
# 2. condición: expresión lógica que se evalúa antes de cada iteración
# 3. incremento: actualización de la variable de control después de cada iteración 
# estructura de un bucle for:
# for variable in range(inicio, fin, paso): 
#   código a ejecutar
# bucle while: repite una tarea mientras una condición sea verdadera
# estructura de un bucle while:
# while condición:                          
#   código a ejecutar
# break: instrucción que se utiliza para salir de un bucle antes de que haya terminado  
# continue: instrucción que se utiliza para saltar a la siguiente iteración de un bucle
# input(): función que permite al usuario ingresar datos durante la ejecución del programa
# int(): función que convierte un valor a un número entero
# float(): función que convierte un valor a un número decimal
# str(): función que convierte un valor a una cadena de caracteres
# funciones: bloque de código reutilizable que realiza una tarea específica
# def nombre_funcion(parámetros): 
#   código a ejecutar
# return: instrucción que se utiliza para devolver un valor desde una función
# estructuras de datos: formas de organizar y almacenar datos en la memoria de una computadora
# arrays o listas: estructura de datos que permite almacenar múltiples valores en una sola variable
# lista = [elemento1, elemento2, elemento3]
# indices: posición de cada elemento en la lista, comenzando desde 0
# cambiar valor de un elemento en una lista:
# lista[indice] = nuevo_valor  
# agregar elemento a una lista:
# lista.append(nuevo_elemento)
# eliminar elemento de una lista:
# lista.remove(elemento)
# eliminar el ultimo elemento de una lista:
# lista.pop()   
# for con listas:
# for elemento in lista:
#   código a ejecutar
# len(): función que devuelve la cantidad de elementos en una lista
# objetos: estructura de datos que combina datos con comportamientos relacionados
# un objeton tiene propiedades (atributos) y métodos (funciones)
# definir un objeto:
# class NombreObjeto:
#   def __init__(self, propiedad1, propiedad2): 
#     self.propiedad1 = propiedad1
#     self.propiedad2 = propiedad2
#  def metodo(self):            
#     código a ejecutar
# que es una propiedad: característica o atributo que describe al objeto
# que es un método: función asociada a un objeto que define su comportamiento
# crear una instancia de un objeto:
# objeto = NombreObjeto(valor1, valor2)
# acceder a una propiedad:
# valor = objeto.propiedad1
# llamar a un método:
# objeto.metodo()
# cambiar el valor de una propiedad:
# objeto.propiedad1 = nuevo_valor