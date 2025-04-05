def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

numero = 5 
resultado = factorial(numero) 
print(f"el factorial de {numero} es:{resultado}")