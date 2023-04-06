km = float(input("Digite a distância da viagem em km: "))

if km <= 200:
    print(f"Para {km}km, o total a pagar é R${km*0.5:.2f}")
else:
    print(f"Para {km}km, o total a pagar é R${km*0.45:.2f}")
