# Exercício Python 083: Crie um programa onde o usuário digite uma
# expressão qualquer que use parênteses. Seu aplicativo deverá analisar se
# a expressão passada está com os parênteses abertos e fechados na ordem correta.

pilha_parenteses = []

expressao = input("Digite a expressão: ")

for index in expressao:
    if index == "(":
        pilha_parenteses.append("(")
    elif index == ")":
        if len(pilha_parenteses) > 0:
            pilha_parenteses.pop()
        else:
            pilha_parenteses.append("erro")
            break

if len(pilha_parenteses) == 0:
    print("A expressão está certa!")
else:
    print("A expressão está errada!")
