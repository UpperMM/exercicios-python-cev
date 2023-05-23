""" Exercício Python 063: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.

Ex: 0 - 1 - 1 - 2 - 3 - 5 - 8 """

termos = int(input("Quantos termos você quer mostrar? "))

numero_anterior = 1
fibonacci = 0

while termos != 0:
    print(fibonacci, end=" → ")
    fibonacci += numero_anterior
    numero_anterior = fibonacci - numero_anterior
    termos -= 1

print("FIM")
