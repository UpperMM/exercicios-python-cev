from math import hypot

oposto = float(input("Digite o comprimento do cateto oposto: "))
adjacente = float(input("Digite o comprimento do cateto adjacente: "))

hipotenusa = hypot(oposto, adjacente)

print(f"A hipotenusa vai medir {hipotenusa:.2f}")
