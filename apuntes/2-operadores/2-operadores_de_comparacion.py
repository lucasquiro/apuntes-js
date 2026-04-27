# ============================
#      OPERADORES DE COMPARACIÓN
# ============================

# Los operadores de comparación se usan para comparar valores.
# Siempre devuelven un resultado booleano:
#   True  → la comparación es verdadera
#   False → la comparación es falsa

# ----------------------------
#   IGUALDAD ==
# ----------------------------
# Compara si dos valores son exactamente iguales.
5 == 5      # True
5 == 3      # False
"a" == "A"  # False (sensible a mayúsculas)

# ----------------------------
#   DESIGUALDAD !=
# ----------------------------
# Compara si dos valores NO son iguales.
5 != 3      # True
5 != 5      # False

# ----------------------------
#   MAYOR >
# ----------------------------
# Verifica si el valor de la izquierda es estrictamente mayor.
7 > 4       # True
3 > 9       # False

# ----------------------------
#   MAYOR O IGUAL >=
# ----------------------------
# Verdadero si es mayor o si es igual.
7 >= 7      # True
5 >= 9      # False

# ----------------------------
#   MENOR <
# ----------------------------
# Verifica si el valor de la izquierda es estrictamente menor.
2 < 10      # True
8 < 1       # False

# ----------------------------
#   MENOR O IGUAL <=
# ----------------------------
# Verdadero si es menor o si es igual.
3 <= 3      # True
6 <= 2      # False

# ----------------------------
#   COMPARACIONES CON STRINGS
# ----------------------------
# Se comparan en orden lexicográfico (orden alfabético según ASCII/Unicode)
"apple" < "banana"   # True
"Z" < "a"            # True (porque "Z" tiene código ASCII menor)

# ----------------------------
#   COMPARACIONES MIXTAS
# ----------------------------
# Python no permite comparar tipos incompatibles de forma arbitraria.
5 < "a"   # TypeError
