frase = str(input("Escreva uma frase: ")).strip()

fraseformatada = frase.lower()

print(
    f"Na frase '{frase}' o 'A' apareceu {fraseformatada.count('a')} vez(es);\nApareceu pela primeira vez na posição \033[32m{fraseformatada.find('a')+1}\033[m\nApareceu pela última vez na posição \033[31m{fraseformatada.rfind('a')+1}\033[m"
)
