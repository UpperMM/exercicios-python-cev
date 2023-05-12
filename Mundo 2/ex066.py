contador = soma = 0

while True:
    numero = int(input("Digite um número [999 para parar]: "))
    if numero == 999:
        break
    contador += 1
    soma += numero

print(f"Foram digitados {contador} números e a soma entre eles foi {soma}.")
