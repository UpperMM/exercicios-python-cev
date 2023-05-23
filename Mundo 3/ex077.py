# Exercício Python 077: Crie um programa que tenha uma tupla com várias
# palavras. Depois disso, você deve mostrar, para cada palavra, quais são
# as suas vogais.

palavras = (
    "casa",
    "gato",
    "música",
    "água",
    "ênfase",
    "óbvio",
    "pôr",
    "último",
    "fácil",
    "cuidar",
    "país",
    "sábado",
    "vídeo",
    "ótimo",
    "tórax",
    "pão",
    "último",
    "cômodo",
    "férias",
    "útil",
)

for palavra in palavras:
    print(f"\n{palavra.capitalize()} tem as vogais:", end=" ")

    for letra in palavra:
        if letra.lower() in "aeiouáàãâéèêíìîóòõôúùû":
            print(letra, end=" ")
