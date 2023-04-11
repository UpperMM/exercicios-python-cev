from math import sin, cos, tan, radians

angulo = float(input("Digite o ângulo que deseja: "))

seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print(
    f"O ângulo de {angulo} tem o SENO de \033[32m{seno:.2f}\033[m\nTem o COSSENO de \033[32m{cosseno:.2f}\033[m\nTem a tangente de \033[32m{tangente:.2f}\033[m"
)
