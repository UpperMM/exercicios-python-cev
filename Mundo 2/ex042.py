""" Exercício Python 042: Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
- EQUILÁTERO: todos os lados iguais
- ISÓSCELES: dois lados iguais, um diferente
- ESCALENO: todos os lados diferentes """

reta1 = float(input("Digite o 1º segmento: "))
reta2 = float(input("Digite o 2º segmento: "))
reta3 = float(input("Digite o 3º segmento: "))

if reta3 + reta2 > reta1 and reta1 + reta3 > reta2 and reta1 + reta2 > reta3:
    if reta1 == reta2 == reta3:
        triangulo = "EQUILÁTERO"
    elif reta1 == reta2 or reta1 == reta3 or reta2 == reta3:
        triangulo = "ISÓSCELES"
    else:
        triangulo = "ESCALENO"
    print(f"Os segmentos acima \033[32mPODEM FORMAR um triângulo {triangulo}!\033[m")
else:
    print(f"Os segmentos acima \033[31mNÃO PODEM FORMAR um triângulo!\033[m")
