frase = str(input("Escreva uma frase: ")).strip()

fraseformatada = frase.lower()

print(
    f"Na frase '{frase}' o 'A' apareceu {fraseformatada.count('a')} vez(es);\nApareceu pela primeira vez na posição {fraseformatada.find('a')+1};\nApareceu pela última vez na posição {fraseformatada.rfind('a')+1}."
)
