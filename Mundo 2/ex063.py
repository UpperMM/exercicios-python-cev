termos = int(input("Quantos termos você quer mostrar? "))

numero_anterior = 1
fibonacci = 0

while termos != 0:
    print(fibonacci, end=" → ")
    fibonacci += numero_anterior
    numero_anterior = fibonacci - numero_anterior
    termos -= 1

print("FIM")
