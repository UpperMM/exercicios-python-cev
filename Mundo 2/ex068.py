from random import randint

print("PAR OU ÍMPAR!")

vitorias = 0

while True:
    valor_maquina = randint(1, 10)
    valor = int(input("Diga um valor: "))
    total = valor + valor_maquina
    jogada = " "

    while jogada not in "PI":
        jogada = str(input("\nPar ou ímpar? [P/I] ")).strip().upper()[0]

    print(
        f"\nVocê jogou {valor} e o computador {valor_maquina}. O total de {total} é ",
        end="",
    )
    print("ímpar!" if total % 2 == 1 else "par!")

    if (valor + valor_maquina) % 2 == 1:
        if jogada == "P":
            print("\nVocê perdeu!")
            break
        else:
            print("\nVocê ganhou!")
    else:
        if jogada == "I":
            print("\nVocê perdeu!")
            break
        else:
            print("\nVocê ganhou!")

    vitorias += 1

    print("\nVamos jogar novamente!")

print(f"\nGAME OVER! Você ganhou {vitorias} vez[es]!")
