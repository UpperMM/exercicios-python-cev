reta1 = float(input("Digite um segmento: "))
reta2 = float(input("Mais um:"))
reta3 = float(input("e... mais um: "))

if reta3 + reta2 > reta1 and reta1 + reta3 > reta2 and reta1 + reta2 > reta3:
    print("É possível formar um triangulo.")
else:
    print("Não é possível formar um triângulo.")
