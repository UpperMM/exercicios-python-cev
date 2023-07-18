# Exercício Python 080: Crie um programa onde o usuário possa digitar
# cinco valores numéricos e cadastre-os em uma lista, já na posição
# correta de inserção (sem usar o sort()). No final, mostre a lista
# ordenada na tela.

lista = []

for repeticao in range(0, 5):
    valor = int(input("Digite um valor para ser adicionado à lista: "))

    if repeticao == 0 or valor >= lista[-1]:
        lista.append(valor)
        print("Valor adicionado ao final da lista!")

    else:
        for posicao, elemento in enumerate(lista):
            if valor < elemento:
                lista.insert(posicao, valor)
                print(f"Valor adicionado na posição {posicao}")
                break

print("\nLista ordenada:", lista)
