#                               Proyecto Dia 3: “Recomendador de Actividades Inteligente” 
# Consigna: 
# En la empresa que trabajas como programador, tu jefe de equipo te pide que desarrolles  
# un programa en Python que recomiende actividades basandose en tres factores: clima, 
# hora del dia y estado de animo del usuario, utilizando operadores logicos como and, or y 
# not. 

# Estos son los requerimientos que tu jefe desea que tengas en cuenta: 

# Define tres variables: 
# • Clima: Puede ser “soleado”, “lluvioso” o “nublado”. 
# • Hora: Puede ser “mañana”, “tarde” o “noche”. 
# • Estado_animo: Puede ser “activo” o “relajado”. 

# Reglas de decisión: 
# Utiliza operadores lógicos como and, or y not para crear combinaciones interesantes: 

# 1. Si el clima es “soleado” o “nublado” y estás “activo”, sugiere hacer ejercicio. 
# 2. Si el clima es “lluvioso” o no es “soleado”, recomienda leer. 
# 3. Si es “noche” y estás “activo”, sugiere escuchar música animada. 
# 4. Si es “noche” y no estás “activo”, sugiere meditar. 
# 5. En cualquier otro caso, recomienda ver una película o serie. 

# ESCRIBE LA SOLUCIÓN DE TU CÓDIGO AQUÍ DEBAJO :)


clima = "soleado"
hora = "mañana"
estado_animo = "activo"

if clima == "soleado" or clima == "nublado" and estado_animo == "activo":
    print("Sugerencia: Hacer ejercicio")
elif clima == "lluvioso" or not clima == "soleado":
    print("Sugerencia: Leer un libro")
elif hora == "noche" and estado_animo == "activo":
    print("Sugerencia: Escuchar música animada")
elif hora == "noche" and not estado_animo == "activo":
    print("Sugerencia: Meditar")
else:
    print("Sugerencia: Ver una película o serie")