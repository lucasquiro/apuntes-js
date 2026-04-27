# =========================================================
# Datos compuestos
# Un dato compuesto es un dato que contiene varios valores dentro.
# =========================================================


# =========================================================
# 1. LISTAS (list)
# Conjunto de datos que SÍ se pueden modificar.
# Se escriben con corchetes []
# =========================================================

lista = ["lucas", "quiroga", True, 1.80]

# Acceder por índice:
print(lista[1])  # "quiroga"
# Nota: en informática los índices empiezan desde 0.

# Modificar una lista:
lista = ["lucas", "quiroga", True, 1.80]
lista[1] = "manolo"
print(lista[1])  # "manolo"


# =========================================================
# 2. TUPLAS (tuple)
# Igual que una lista, pero:
# - Usan paréntesis ()
# - NO se pueden modificar (son inmutables)
# =========================================================

tupla = ("lucas", "quiroga", True, 1.80)
# tupla[1] = "manolo"  → ERROR (no se puede modificar)


# =========================================================
# 3. CONJUNTOS (set)
# Conjunto de datos SIN orden fijo, modificables, pero con reglas:
# - Se escriben con llaves {}
# - No permiten elementos repetidos
# - No se puede acceder por índice (set[1] da error)
# =========================================================

conjunto = {"lucas", "quiroga", True, 1.80}

# 1. No se accede con índices:
# print(conjunto[1]) → ERROR

# 2. No permite elementos repetidos:
conjunto2 = {"lucas", "quiroga", True, 1.80, "lucas"}
print(conjunto2)
# Resultado → {"lucas", "quiroga", True, 1.80}
# Solo aparece una vez "lucas"

# 3. Para acceder a un elemento hay que usar un bucle (para mas info de bucle ir a )


# ---------------------------------------------------------
# Métodos para eliminar elementos de un set
# ---------------------------------------------------------

# 1. remove(elemento)
# Elimina un elemento.
# Si el elemento no existe → ERROR.
conjunto = {"a", "b", "c"}
conjunto.remove("b")
print(conjunto)  # {"a", "c"}

# 2. discard(elemento)
# Elimina un elemento.
# Si NO existe → NO da error.
conjunto = {"a", "b", "c"}
conjunto.discard("z")  # no pasa nada


# =========================================================
# 4. DICCIONARIOS (dict)
# Almacenan datos en formato clave : valor
# Se escriben con {}
# =========================================================

diccionario = {
    "nombre": "lucas",
    "apellido": "quiroga",
    "esta_emocionado": True,
    "altura": 1.80,
    "dato_repetido": "quiroga"
}

# Acceso a valores por clave:
print(diccionario["nombre"])  # "lucas"


# Características del diccionario:
# 1. Funciona como una lista pero el "índice" es un nombre, no un número.
# 2. Cada par clave-valor se separa con coma (excepto el último).
# 3. La clave se llama key, y el valor se llama value.
#    Formato:
#    diccionario = {
#        key: value
#    }
