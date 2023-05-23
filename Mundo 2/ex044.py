""" Exercício Python 044: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço formal
- 3x ou mais no cartão: 20% de juros """

preco = float(input("Preço das compras: R$ "))
opcao = int(
    input(
        "FORMAS DE PAGAMENTO\n[ 1 ] à vista no dinheiro/cheque\n[ 2 ] à vista no cartão\n[ 3 ] 2x no cartão\n[ 4 ] 3x ou mais no cartão\n qual é a opção? "
    )
)

if opcao == 1:
    novopreco = preco * 0.9
elif opcao == 2:
    novopreco = preco * 0.95
elif opcao == 3:
    novopreco = preco
    print(
        f"Sua compra será parcelada em \033[1m2x\033[m de R$ \033[32m{preco/2:.2f} SEM JUROS\033[m."
    )
elif opcao == 4:
    parcelas = int(input("Quantas parcelas? "))
    novopreco = preco * 1.2
    print(
        f"Sua compra será parcelada em \033[1m{parcelas}x\033[m de \033[31mR$ {novopreco/parcelas:.2f} COM JUROS\033[m."
    )
else:
    novopreco = preco
    print("\033[1;31mOpção inválida. Tente novamente.\033[m")

if opcao in [1, 2, 3, 4]:
    print(
        f"Sua compra de \033[1mR$ {preco:.2f}\033[m vai custar \033[1mR$ {novopreco:.2f}\033[m no final."
    )
