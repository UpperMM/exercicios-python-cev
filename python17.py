from random import choice

aluno1 = str(input("Primeiro alumo: "))
aluno2 = str(input("Segundo aluno: "))
aluno3 = str(input("Terceiro aluno: "))
aluno4 = str(input("Quarto aluno: "))

alunos = [aluno1, aluno2, aluno3, aluno4]

sorteio = choice(alunos)

print(f"O sorteado foi {sorteio}.")
