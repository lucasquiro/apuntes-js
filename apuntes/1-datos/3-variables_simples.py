# =========================================================
# Variables
# =========================================================

# Qué es una variable:
# Una variable guarda un dato que puede cambiar durante el programa.
nombre = "lucas"
edad = 21

# Modificar una variable directamente:
edad = 22

# Operadores abreviados (modifican el valor actual):
numero = 10
numero += 5   # suma 5 a su valor actual

# para mas informacion de los operadores ir a operadores_aritmeticos.py

# Lista de operadores abreviados:
# x -= n   # resta y asigna
# x *= n   # multiplica y asigna
# x /= n   # divide y devuelve float
# x //= n  # división entera
# x %= n   # módulo (resto)

# Ejemplos:

x = 10

x -= 3   # 7
x *= 2   # 10
x /= 4   # 2.5
x //= 4  # 2
x %= 4   # 2

# =========================================================
# Eliminar una variable con del
# =========================================================
nombre = "lucas"
del nombre   # elimina la variable por completo

# =========================================================
# Concatenar (unir) strings
# =========================================================

# Forma 1 (con +)
nombre = "lucas"
mensaje = "Hola " + nombre + ", ¿cómo estás?"

# Si incluye números, deben convertirse a texto:
edad = 21
mensaje = "Tenés " + str(edad) + " años"

# Forma 2 (f-strings): la más clara y recomendada
nombre = "lucas"
mensaje = f"Hola {nombre}, ¿cómo estás?"

edad = 21
mensaje = f"Tenés {edad} años"

# dir te dice todo lo que podes hacer con un dato

dataso = dir(17)

print(dataso)


