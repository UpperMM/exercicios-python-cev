# Exercício Python 045: Crie um programa que faça o computador jogar
# Jokenpô com você.

from random import choice

jogada = str(input("Pedra, papel ou tesoura? ")).upper().strip()
jogada_computador = choice(["PEDRA", "PAPEL", "TESOURA"])

if jogada == jogada_computador:
    resultado = "\033[1mEmpate!\033[m"
elif (
    jogada == "PAPEL"
    and jogada_computador == "TESOURA"
    or jogada == "TESOURA"
    and jogada_computador == "PEDRA"
    or jogada == "PEDRA"
    and jogada_computador == "PAPEL"
):
    resultado = "\033[31mPerdeu!\033[m"
elif (
    jogada == "TESOURA"
    and jogada_computador == "PAPEL"
    or jogada == "PEDRA"
    and jogada_computador == "TESOURA"
    or jogada == "PAPEL"
    and jogada_computador == "PEDRA"
):
    resultado = "\033[32mGanhou!\033[m"
else:
    print("\033[1;31mOpção inválida!")

if jogada in ["PEDRA", "PAPEL", "TESOURA"]:
    print(
        f"{resultado} Você jogou \033[1m{jogada}\033[m e o computador \033[1m{jogada_computador}!\033[m"
    )
