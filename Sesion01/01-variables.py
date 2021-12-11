# variable numerica
numero = 10
numero2 = 10.5

numero = "Febrero"

# variables de texto o string
nombre = "Eduardo"
apellido = "Ramiro"

html = """<html>
<p>
</p>"""

print("Hola :)")

print(type(nombre))
# str = string
# int = integer
# float = float
print(type(numero))
print(type(numero2))
# bool = boolean

soltero = True
calor = False
print(type(soltero))

# Variables que tienen vario Valores
# Arreglos > Listas List
edades = [10, 12 , 40, 60, 'Eduardo', 14.5, False, [1, 2]]

# JSON (JavaScript Object Notation) | Diccionario
# Nota : Si un llave se repite su valor sera modificado y se perdera el anterior valor
curso = {
    'nombre': 'Backend',
    'nombre': 'Frontend',
    'dificultad': 'Dificil',
}

print(curso['dificultad'])