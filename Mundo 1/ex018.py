from math import sin, cos, tan, radians

angulo = float(input("Digite o ângulo que deseja: "))

seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print(
    f"O ângulo de {angulo} tem o SENO de {seno:.2f}\nO ângulo de {angulo} tem o COSSENO de {cosseno:.2f}\nO ângulo de {angulo} tem a tangente de {tangente:.2f}"
)
