# ============================
#      MÉTODOS DE CADENA (str)
# ============================

# Las cadenas (strings) pertenecen a la clase str.
# Por eso se dice que "las cadenas van con mayúscula": str

# Los métodos se ejecutan sobre una variable de texto
# usando un punto (.) después de la variable.

texto = "manolito"
resultado = texto.upper()
print(resultado)   # MANOLITO


# ----------------------------
#          dir()
# ----------------------------
# Muestra todos los métodos y atributos disponibles
# para un objeto (en este caso, un string).

dir("hola")
# Devuelve una lista de métodos como: upper, lower, find, etc.


# ----------------------------
#          upper()
# ----------------------------
# Convierte todo el texto a mayúsculas.
texto = "hola"
texto.upper()   # "HOLA"

# ----------------------------
#            lower()
# ----------------------------
# Convierte todo el texto a minúsculas.

texto = "HoLa"
texto.lower()   # "hola"

# ----------------------------
#       capitalize()
# ----------------------------
# Convierte todo el texto a minúsculas
# y luego pone la primera letra en mayúscula.

texto = "hOLa"
texto.capitalize()   # "Hola"


# ----------------------------
#     RETORNAR UN VALOR
# ----------------------------
# Retornar significa que un método devuelve un resultado
# que puede ser guardado en una variable.

texto = "hola"
resultado = texto.upper()  # retorna "HOLA"
print(resultado)


# ----------------------------
#          find()
# ----------------------------
# Busca un valor dentro del string.
# Retorna la posición donde lo encuentra.
# Si NO lo encuentra, retorna -1.
# Los índices comienzan desde 0.
# El espacio también cuenta como carácter.

texto = "hola mundo"
texto.find("a")   # 3
texto.find("z")   # -1


# ----------------------------
#          index()
# ----------------------------
# Funciona igual que find(),
# pero si NO encuentra el valor lanza un error (excepción).

texto = "hola"
texto.index("o")  # 1
# texto.index("z") → ERROR (ValueError)


# ----------------------------
#        isnumeric()
# ----------------------------
# Verifica si el string está compuesto SOLO por números.
# Devuelve True o False.

"123".isnumeric()     # True
"12.3".isnumeric()    # False
"abc".isnumeric()     # False


# ----------------------------
#         isalpha()
# ----------------------------
# Verifica si el string está compuesto SOLO por letras.
# Devuelve True o False.
# No permite espacios ni números.

"hola".isalpha()      # True
"hola123".isalpha()   # False
"hola mundo".isalpha()# False


# ----------------------------
#     USO COMÚN DE is*
# ----------------------------
# Estos métodos se usan mucho para validar datos ingresados
# antes de convertirlos a int o float.

dato = "123"

if dato.isnumeric():
    numero = int(dato)

# ----------------------------
#           count()
# ----------------------------
# Cuenta cuántas veces aparece un valor dentro de un string.
# Si no encuentra coincidencias, retorna 0.

texto = "banana"
texto.count("a")   # 3
texto.count("z")   # 0


# ----------------------------
#            len()
# ----------------------------
# len NO es un método, es una función.
# Se usa como print().
# Cuenta la cantidad de caracteres del string.
# Los espacios también cuentan.

texto = "hola mundo"
len(texto)   # 10


# ----------------------------
#        endswith()
# ----------------------------
# Verifica si el string termina con un valor.
# Retorna True o False.

texto = "archivo.txt"
texto.endswith(".txt")   # True
texto.endswith(".pdf")   # False


# ----------------------------
#       startswith()
# ----------------------------
# Verifica si el string comienza con un valor.
# Retorna True o False.

texto = "python.py"
texto.startswith("py")   # True
texto.startswith("js")   # False


# ----------------------------
#          replace()
# ----------------------------
# Reemplaza una parte del string por otra.
# Solo reemplaza si encuentra coincidencias.
# Si no encuentra nada, retorna el string original.

variable = "gol"
variable_modificada = variable.replace("l", "rdo")
print(variable_modificada)   # "gordo"

# Ejemplo sin coincidencias:
texto = "hola"
texto.replace("z", "x")   # "hola"


# ----------------------------
#           split()
# ----------------------------
# Divide un string y genera una lista.
# Usa el valor pasado como separador.

texto = "Hola,que,tal,tu,dia"
texto_separado = texto.split(",")
print(texto_separado)
# ["Hola", "que", "tal", "tu", "dia"]

# ----------------------------
#            strip()
# ----------------------------
# Elimina espacios en blanco al inicio y al final del string.
# No elimina espacios internos.

texto = "   hola mundo   "
texto.strip()   # "hola mundo"
