escolha = soma = maior = menor = contador = 0

while escolha != "N":
    numero = int(input("Digite um número: "))
    if numero > maior:
        maior = numero
    if numero < menor or contador == 0:
        menor = numero
    contador += 1
    soma += numero
    escolha = str(input("Quer continuar? [S/N] ")).strip().upper()[0]

print(
    f"Você digitou {contador} números e a média foi {soma/contador}\nO maior valor foi {maior} e o menor foi {menor}."
)
