# Operadores aritmeticos
# Suma, resta, multiplicación, division, exponente, cociente, modulo

numero1 = 10
numero2 = 30

resultado = numero1 + numero2

print(resultado)
print("El resultado es: ", resultado)

print("El resultado es {} y nada más")

print("El resultado es {} y nada más" .format(resultado, numero1))
print(f"El resultado es {resultado}")

print("El resultado es {1} y nada más {0}" .format(numero1, resultado))

# la resta
resultado = numero1 - numero2
print ("La resta es: ",resultado)

# la multiplicación
resultado = numero1 * numero2
print ("La multplicación es: ",resultado)

# la division
resultado = numero1 / numero2
# 0.3333333

print("{:.1f}" .format(resultado))
print(f"{resultado:.1f}")

# el modulo
resultado = numero1 % numero2
print ("El modulo es: ",resultado)

#el conciente
resultado = numero1 // numero2
print ("El cociente es: ",resultado)

# el exponente
resultado = numero1 ** numero2
print('El exponente es:', resultado)

texto = "Hola mi nombre es Eduardo"
# las variables de tipo STR tambien pueden ser accedidas mediante sus posiciones como si fuese una lista

