metro = float(input("Digite um valor em metros: "))

print(
    f"\033[32m{metro/1000}km\n{metro/100}hm\n{metro/10}dam\n{metro}m\n{metro*10}dm\n{metro*100}cm\n{metro*1000}mm\033[m"
)
