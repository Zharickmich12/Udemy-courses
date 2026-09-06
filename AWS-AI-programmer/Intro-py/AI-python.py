# PYTHON FOR AI PROGRAMMING

"""
¿QUÉ ES AI PROGRAMMING?
AI programming = creación de sistemas capaces de realizar tareas que normalmente requieren inteligencia humana.
Tareas típicas:
    - entender lenguaje natural
    - reconocer patrones
    - tomar decisiones
    - aprender de los datos
    - hacer predicciones
Construir algoritmos que aprendan de datos y produzcan clasificaciones, decisiones o predicciones.
"""

"""
¿POR QUÉ PYTHON SE USA EN IA?
Python es muy usado en IA porque:
    - tiene sintaxis simple
    - es fácil de leer
    - sirve tanto para principiantes como para expertos
    - tiene muchas librerías especializadas
Librerías importantes:
    - TensorFlow
    - PyTorch
    - scikit-learn
Python facilita escribir, entender y mantener programas relacionados con machine learning y deep learning.
"""

"""
FUNDAMENTOS DE PYTHON IMPORTANTES PARA IA
    DATA TYPES AND OPERATORS
Los tipos de datos permiten representar información. En IA son importantes para guardar datos, etiquetas y resultados.
Tipos:
    - list
    - dictionary
    - tuple
Ejemplo conceptual:
Un diccionario puede relacionar un archivo con su etiqueta.
"""

archivo_a_etiqueta = {
    "dog_001.jpg": "beagle",
    "dog_002.jpg": "poodle",
}

# Idea importante:
# key   -> nombre del archivo / identificador
# value -> etiqueta / clasificación

# ------------------------------------------------------------
# 3.2 DATA STRUCTURES
# ------------------------------------------------------------

# Las estructuras de datos ayudan a almacenar y organizar
# grandes cantidades de información de forma eficiente.

# Estructuras destacadas:
# - lists
# - dictionaries
# - sets

# Uso en IA:
# - guardar datasets
# - almacenar etiquetas
# - registrar clasificaciones
# - comparar resultados
# - hacer búsquedas rápidas

# Ejemplos mínimos:

imagenes = ["dog_001.jpg", "dog_002.jpg", "dog_003.jpg"]   # lista
etiquetas = {"dog_001.jpg": "beagle"}                      # diccionario
razas_unicas = {"beagle", "poodle", "husky"}               # set

# Idea clave:
# los dictionaries son especialmente útiles cuando se necesita
# mapear un dato con su resultado o etiqueta.

# ------------------------------------------------------------
# 3.3 CONTROL FLOW
# ------------------------------------------------------------

# Control flow = mecanismos para controlar cómo avanza el programa.

# Elementos principales:
# - loops
# - conditionals

# En IA se usan para:
# - recorrer datos
# - procesar elementos uno por uno
# - verificar resultados
# - decidir acciones según condiciones

# Ejemplo conceptual:

clasificaciones = {
    "dog_001.jpg": "beagle",
    "dog_002.jpg": "poodle",
}

for archivo, raza in clasificaciones.items():
    if raza == "beagle":
        pass
        # aquí podría ejecutarse una acción específica

# Idea importante:
# los loops permiten procesar muchos datos;
# los conditionals permiten tomar decisiones según el resultado.

# ------------------------------------------------------------
# 3.4 FUNCTIONS
# ------------------------------------------------------------

# Una función encapsula una tarea específica.

# Ventajas:
# - reutilización
# - modularidad
# - organización
# - mantenimiento más fácil

# En IA, las funciones pueden encargarse de:
# - leer archivos
# - procesar datos
# - aplicar clasificación
# - evaluar resultados

def ejemplo_funcion_procesamiento(datos):
    # Ejemplo mínimo:
    # una función recibe datos y devuelve un resultado procesado
    return datos

# Idea clave:
# dividir un problema grande en funciones pequeñas hace que
# el sistema sea más claro y más fácil de mantener.

# ------------------------------------------------------------
# 3.5 OBJECT-ORIENTED PROGRAMMING (OOP)
# ------------------------------------------------------------

# OOP organiza el código usando:
# - classes
# - objects

# Sirve para:
# - estructurar sistemas complejos
# - agrupar datos y comportamiento relacionados
# - hacer el código más mantenible

# En IA puede usarse para representar:
# - modelos
# - componentes de preprocesamiento
# - partes de un pipeline

class ModeloIA:
    # Ejemplo conceptual:
    # una clase puede representar un modelo o componente del sistema
    def __init__(self, nombre):
        self.nombre = nombre

# Idea importante:
# OOP ayuda cuando el proyecto crece y necesita mejor organización.

# ------------------------------------------------------------
# 3.6 SCRIPTING
# ------------------------------------------------------------

# Scripting = escribir programas para automatizar tareas.

# En IA se usa para:
# - preparar data pipelines
# - automatizar entrenamiento
# - automatizar evaluación
# - gestionar experimentos

# Ejemplo conceptual:
# un script puede ejecutar varias tareas en secuencia:
# 1. cargar datos
# 2. procesarlos
# 3. clasificar
# 4. medir resultados

# ------------------------------------------------------------
# 4. RELACIÓN CON EL PROYECTO DEL CURSO
# ------------------------------------------------------------

# Al final del curso se aplican estos conceptos en un proyecto.

# Proyecto:
# usar un modelo preentrenado para tareas de clasificación
# e identificación.

# Lo importante del proyecto según la lección:
# - clasificar imágenes
# - gestionar flujo de datos
# - trabajar con distintas arquitecturas de redes neuronales
# - medir tiempo de ejecución de algoritmos

# Idea central:
# esta lección presenta la base de Python que luego se usará
# en una tarea real de IA.

# ------------------------------------------------------------
# 5. MAPA RÁPIDO DE LA LECCIÓN
# ------------------------------------------------------------

# Python for AI Programming
# ├─ AI programming
# │  ├─ aprender de datos
# │  ├─ reconocer patrones
# │  ├─ tomar decisiones
# │  └─ hacer predicciones
# │
# ├─ por qué Python
# │  ├─ simple
# │  ├─ legible
# │  ├─ accesible
# │  └─ muchas librerías
# │
# ├─ fundamentos clave
# │  ├─ data types
# │  ├─ data structures
# │  ├─ control flow
# │  ├─ functions
# │  ├─ OOP
# │  └─ scripting
# │
# └─ aplicación
#    └─ proyecto de clasificación de imágenes

# ------------------------------------------------------------
# 6. RESUMEN ULTRA RÁPIDO
# ------------------------------------------------------------

# AI programming:
# crear sistemas que aprenden de datos y producen predicciones.

# Python en IA:
# se usa por simplicidad, legibilidad y ecosistema de librerías.

# Fundamentos más importantes:
# - listas, diccionarios, tuplas, sets
# - loops y conditionals
# - funciones
# - clases y objetos
# - automatización con scripts

# Punto especialmente importante:
# los dictionaries son muy útiles para asociar datos con etiquetas
# o resultados, por ejemplo:
# archivo -> clasificación

# Conexión con el curso:
# todo esto prepara el proyecto final de clasificación de imágenes
# con un modelo preentrenado.
