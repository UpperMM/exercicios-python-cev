numero = int(input("Digite o número para exibir seu fatorial: "))

acumulador = numero - 1

print(f"Calculando {numero}! = {numero} x", end=" ")

while acumulador != 0:
    print(acumulador, end="")
    print(" x " if acumulador > 1 else " = ", end="")
    numero *= acumulador
    acumulador -= 1

print(numero, end="")

# utilizando o laço for
"""numero = int(input("Digite o número para exibir seu fatorial: "))

fatorial = 1

print(f"Calculando {numero}! = ", end="")

for i in range(numero, 0, -1):
    print(i, end="")
    print(" x " if i != 1 else " = ", end="")
    fatorial *= i

print(fatorial, end="")
"""
