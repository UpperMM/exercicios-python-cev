# Exercício Python 031: Desenvolva um programa que pergunte a distância de
# uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km
# para viagens de até 200Km e R$0,45 parta viagens mais longas.

km = float(input("Digite a distância da viagem em km: "))

if km <= 200:
    print(f"Para {km}km, o total a pagar é R${km*0.5:.2f}")
else:
    print(f"Para {km}km, o total a pagar é R${km*0.45:.2f}")
