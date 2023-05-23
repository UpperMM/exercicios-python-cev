""" Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Cuiabá (alteração necessária). """

brasileirao = (
    "Botafogo",
    "Palmeiras",
    "Fluminense",
    "Cruzeiro",
    "Athletico-PR",
    "Atlético-MG",
    "Santos",
    "Fortaleza",
    "Flamengo",
    "São Paulo",
    "Grêmio",
    "Internacional",
    "Bragantino",
    "Bahia",
    "Goiás",
    "Vasco",
    "Corinthians",
    "Cuiabá",
    "Coritiba",
    "América-MG",
)

print(
    f"""Os 5 primeiros times são: {brasileirao[:5]}

Os 4 últimos são: {brasileirao[-5:-1]}

Times em ordem alfabética: {sorted(brasileirao)}

O Cuiabá está na {brasileirao.index("Cuiabá")+1}ª posição"""
)
