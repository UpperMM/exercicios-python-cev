print("LOJA")

soma_total = maior_10 = barato_preco = vezes = 0

while True:
    nome = str(input("\nDigite o nome do produto: "))
    preco = float(input("Preço: R$ "))

    soma_total += preco

    opcao = " "

    if vezes == 0 or preco < barato_preco:
        barato_preco = preco
        barato_nome = nome

    vezes += 1

    if preco > 1000:
        maior_10 += 1

    while opcao not in "SN":
        opcao = str(input("\nQuer continuar? [S/N] ")).strip().upper()[0]

    if opcao == "N":
        break

print(f"{'FIM DO PROGRAMA':-^45}")
print(
    f"O total da compra foi R$ {soma_total:.2f}\nTemos {maior_10} produto[s] que custa mais de R$ 1000.00\nO produto mais barato foi {barato_nome} que custa R$ {barato_preco:.2f}."
)
