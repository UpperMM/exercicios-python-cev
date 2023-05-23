""" Exercício Python 043: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
- IMC abaixo de 18,5: Abaixo do Peso
- Entre 18,5 e 25: Peso Ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida """

peso = float(input("Qual é seu peso? (Kg) "))
altura = float(input("Qual é a sua altura? (M) "))

imc = peso / (altura ** 2)

if imc < 18.5:
    status = "\033[31mabaixo do peso!"
elif imc < 25:
    status = "na\033[32m faixa de peso normal. Parabéns!!"
elif imc < 30:
    status = "em \033[31msobrepeso.!"
elif imc < 40:
    status = "em \033[31mobesidade!!"
else:
    status = "em \033[31mobesidade mórbida. Cuidado!"

print(f"O IMC dessa pessoa é de {imc:.1f}\n Você está {status}")
