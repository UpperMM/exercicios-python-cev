reta1 = float(input("Digite um segmento: "))
reta2 = float(input("Mais um: "))
reta3 = float(input("E mais um: "))

if reta3 + reta2 > reta1 and reta1 + reta3 > reta2 and reta1 + reta2 > reta3:
    print("\033[1;32mÉ possível formar um triangulo.\033[m")
else:
    print("\033[1;31mNão é possível formar um triângulo.\033[m")
