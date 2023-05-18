def analisar_nivel_energia(C, niveis_energia):
    for nivel in niveis_energia:
        if nivel <= 8000:
            print("Inseto!")
        else:
            print("Mais de 8000!")


C = int(input())

niveis_energia = []
for _ in range(C):
    nivel = int(input())
    niveis_energia.append(nivel)

analisar_nivel_energia(C, niveis_energia)
