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
"""
key   -> nombre del archivo / identificador
value -> etiqueta / clasificación
"""

"""
DATA STRUCTURES
Las estructuras de datos ayudan a almacenar y organizar grandes cantidades de información de forma eficiente.
Estructuras destacadas:
    - lists
    - dictionaries
    - sets
Uso en IA:
    - guardar datasets
    - almacenar etiquetas
    - registrar clasificaciones
    - comparar resultados
    - hacer búsquedas rápidas
Ejemplos:
"""
imagenes = ["dog_001.jpg", "dog_002.jpg", "dog_003.jpg"]   # lista
etiquetas = {"dog_001.jpg": "beagle"}                      # diccionario
razas_unicas = {"beagle", "poodle", "husky"}               # set
# los dictionaries son especialmente útiles cuando se necesita mapear un dato con su resultado o etiqueta.

"""
CONTROL FLOW
Control flow = mecanismos para controlar cómo avanza el programa.
Elementos principales:
    - loops
    - conditionals
En IA se usan para:
    - recorrer datos
    - procesar elementos uno por uno
    - verificar resultados
    - decidir acciones según condiciones
Ejemplo conceptual:
"""
clasificaciones = {
    "dog_001.jpg": "beagle",
    "dog_002.jpg": "poodle",
}
for archivo, raza in clasificaciones.items():
    if raza == "beagle":
        pass
        # aquí podría ejecutarse una acción específica
# los loops permiten procesar muchos datos;
# los conditionals permiten tomar decisiones según el resultado.

"""
FUNCTIONS
Una función encapsula una tarea específica.
Ventajas:
    - reutilización
    - modularidad
    - organización
    - mantenimiento más fácil
En IA, las funciones pueden encargarse de:
    - leer archivos
    - procesar datos
    - aplicar clasificación
    - evaluar resultados
"""
def ejemplo_funcion_procesamiento(datos):
    # Ejemplo:
    # una función recibe datos y devuelve un resultado procesado
    return datos
# dividir un problema grande en funciones pequeñas hace que el sistema sea más claro y más fácil de mantener.

"""
OBJECT-ORIENTED PROGRAMMING (OOP)
OOP organiza el código usando:
    - classes
    - objects
Sirve para:
    - estructurar sistemas complejos
    - agrupar datos y comportamiento relacionados
    - hacer el código más mantenible
En IA puede usarse para representar:
    - modelos
    - componentes de preprocesamiento
    - partes de un pipeline
class ModeloIA:
"""
    # Ejemplo conceptual:
    # una clase puede representar un modelo o componente del sistema
def __init__(self, nombre):
    self.nombre = nombre
# OOP ayuda cuando el proyecto crece y necesita mejor organización.

"""
SCRIPTING
Scripting = escribir programas para automatizar tareas.
En IA se usa para:
    - preparar data pipelines
    - automatizar entrenamiento
    - automatizar evaluación
    - gestionar experimentos
Ejemplo conceptual:
un script puede ejecutar varias tareas en secuencia:
    1. cargar datos
    2. procesarlos
    3. clasificar
    4. medir resultados
"""