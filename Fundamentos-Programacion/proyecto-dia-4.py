# Proyecto Día 4: Cajero Automático Simulado

# Objetivo del Proyecto: 
# Crear un programa que simule el funcionamiento de un cajero automático, permitiendo al usuario
# retirar dinero siguiendo ciertas reglas.

# Instrucciones:

# 1. Variables Iniciales:
#   a. Saldo: Define una variable que almacene la cantidad de dinero disponible en la cuenta.
#    Puedes asignarle un valor fijo, por ejemplo, $100.
#    Ejemplo:
#    saldo = 100

#   b. Monto a Retirar: Define una variable con un monto fijo que el usuario desea retirar.
#    Este valor se actualizará dentro del bucle para simular diferentes intentos de retiro.
#    Ejemplo:
#    monto_a_retirar = 50


# 2. Reglas del Retiro:
# El cajero solo permitirá retiros que cumplan las siguientes condiciones:

#   a. Fondos Suficientes: El monto a retirar no puede ser mayor que el saldo disponible.
#    Si el usuario intenta retirar más dinero del que tiene, el sistema mostrará un mensaje de error
#    y le pedirá que intente otro monto.

#   b. Múltiplos de 5: El cajero solo entrega billetes en múltiplos de 5.
#    Si el usuario intenta retirar un monto que no cumple esta regla, el sistema mostrará un mensaje de error.

#   c. Salida del Bucle: Si el usuario ingresa 0 como monto a retirar, el cajero finalizará la operación
#    y mostrará el saldo restante.


# 3. Operaciones:
#   a. Verificación del monto: Se usará un bucle while para procesar los retiros hasta que el usuario decida salir.
#    En cada iteración del bucle, el programa verificará si el monto es válido según las reglas de los retiros.

#   b. Cálculo del nuevo saldo: Si el retiro es válido, el monto se restará del saldo disponible.

#   c. Actualización del intento de retiro: Para simular diferentes intentos, el valor del retiro cambiará dentro del bucle.
#    Puedes crear diferentes valores para el monto a retirar y simular estos intentos cambiando la variable dentro del bucle.


# 4. Mostrar los Resultados:
# El programa debe mostrar mensajes al usuario en cada paso del proceso:

#   a. Mensaje de error si el usuario intenta retirar más dinero del que tiene.
#    Ejemplo: print("Error: No tienes suficiente saldo para realizar este retiro.")

#   b. Mensaje de error si el monto no es múltiplo de 5.
#    Ejemplo: print("Error: El monto a retirar debe ser múltiplo de 5.")

#   c. Mensaje de confirmación cuando el retiro es exitoso, mostrando el nuevo saldo.
#    Ejemplo: print(f"Retiro exitoso de ${monto_a_retirar}. Tu saldo actual es ${saldo}.")

#   d. Mensaje final cuando el usuario decide salir del cajero.
#    Ejemplo: print(f"Operación finalizada. Tu saldo final es ${saldo}.")

# Tu Código Aquí Debajo :)

saldo = 100
monto_a_retirar = 50

while True:

    monto_a_retirar = int(input("Ingrese el monto a retirar (0 para salir): "))

    if monto_a_retirar == 0:
        print(f"Operación finalizada. Tu saldo final es ${saldo}.")
        break

    if monto_a_retirar % 5 != 0:
        print("Error: El monto a retirar debe ser múltiplo de 5.")
    elif monto_a_retirar > saldo:
        print("Error: No tienes suficiente saldo para realizar este retiro.")
    else:
        saldo -= monto_a_retirar
        print(f"Retiro exitoso de ${monto_a_retirar}. Tu saldo actual es ${saldo}.")