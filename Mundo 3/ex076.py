# Exercício Python 076: Crie um programa que tenha uma tupla única com
# nomes de produtos e seus respectivos preços, na sequência. No final,
# mostre uma listagem de preços, organizando os dados em forma tabular.

produtos = (
    "Lápis",
    1.75,
    "Borracha",
    2.00,
    "Caderno",
    15.90,
    "Estojo",
    25.00,
    "Transferidor",
    4.20,
    "Compasso",
    9.99,
    "Mochila",
    120.32,
    "Canetas",
    20.30,
    "Livro",
    34.90,
)

print("-" * 29 + f"\n{'Listagem de preços':^29}\n" + "-" * 29)

for posicao in range(0, len(produtos), 2):
    print(f"{produtos[posicao]:.<20}R$ {produtos[posicao+1]:>6.2f}")

print("-" * 29)
