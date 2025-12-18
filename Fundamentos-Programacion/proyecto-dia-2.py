# Calculadora de Propinas y Operaciones Básicas
# Instrucciones: 
    # 1. Variables Iniciales: 
        # a. Cuenta: Establece un valor fijo para el total de la cuenta (puede ser un número entero o decimal). 
        # b. Propina: Establece el porcentaje de propina que se desea dejar. 

    # 2. Operaciones: 
        # a. Calcula la propina multiplicando el total de la cuenta por el porcentaje de propina dividido entre 100. 
        # b. Calcula el total a pagar sumando la propina al total de la cuenta. 

    # 3. Mostrar los Resultados: 
        # a. Muestra al usuario: 
        # i. El total de la cuenta. 
        # ii. El porcentaje de propina. 
        # iii. La propina calculada. 
        # iv. El total a pagar.

# Consejos para Realizar el Proyecto: 
    # • Formato de Salida: 
        # No es necesario usar round() ya que los números son enteros. Aún así, puedes optar por hacerlo si deseas mostrar más detalles en el resultado. 

# ==> ESCRIBE TU SOLUCION AQUÍ DEBAJO :)
cuenta = 498.12
porcentaje_propina = 15

propina = (cuenta * porcentaje_propina) / 100

total_a_pagar = cuenta + propina

print("Total de la cuenta $", cuenta)
print("Porcentaje de propina", porcentaje_propina)
print("Porpina calculada $", round(propina, 2))
print("Total a pagar $", round(total_a_pagar, 2))