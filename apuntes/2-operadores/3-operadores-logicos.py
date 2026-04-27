# ============================
#        OPERADORES LÓGICOS
# ============================

# Los operadores lógicos permiten combinar condiciones.
# Siempre trabajan con valores booleanos (True / False).

# ----------------------------
#         AND
# ----------------------------
# Devuelve True solo si AMBAS condiciones son verdaderas.
True  and True   # True
True  and False  # False
False and True   # False
False and False  # False

# Ejemplo práctico:
edad = 20
tiene_documento = True
(edad >= 18) and tiene_documento   # True

# ----------------------------
#         OR
# ----------------------------
# Devuelve True si AL MENOS UNA de las condiciones es verdadera.
True  or False   # True
False or True    # True
False or False   # False

# Ejemplo:
es_admin = False
es_moderador = True
es_admin or es_moderador   # True

# ----------------------------
#         NOT
# ----------------------------
# Invierte el valor lógico.
not True   # False
not False  # True

# Ejemplo:
lloviendo = False
not lloviendo   # True → significa "no está lloviendo"

# not in → verifica que un elemento NO esté en una secuencia
"banana" not in ["manzana", "pera"]   # True
"a" not in "hola"                     # False

# ----------------------------
#   COMBINACIÓN DE OPERADORES
# ----------------------------
# Las expresiones se pueden combinar y Python respeta prioridad:
# 1) not
# 2) and
# 3) or

True or False and False       # True (porque evalúa: False and False → False; luego True or False → True)
not False and True            # True (not False → True; luego True and True → True)

# ----------------------------
#   USO CON COMPARACIONES
# ----------------------------
edad = 22
tiene_entrada = False

(edad >= 18) and (tiene_entrada)        # False
(edad >= 18) or (tiene_entrada)         # True
not (edad >= 18)                        # False

# ----------------------------
#   CORTO CIRCUITO (SHORT-CIRCUIT)
# ----------------------------
# Python no evalúa lo innecesario:
# - En 'and', si encuentra un False primero, se detiene.
# - En 'or', si encuentra un True primero, se detiene.

False and print("Nunca me ejecuto")    # No imprime nada
True  or  print("Tampoco me ejecuto")  # No imprime nada
