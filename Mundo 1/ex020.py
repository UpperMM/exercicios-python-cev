from random import shuffle

nome1 = str(input("Digite um nome: "))
nome2 = str(input("Digite mais um: "))
nome3 = str(input("... Mais um: "))
nome4 = str(input("E mais um: "))

pessoas = [nome1, nome2, nome3, nome4]
shuffle(pessoas)

print("A ordem é:")
print(pessoas)
