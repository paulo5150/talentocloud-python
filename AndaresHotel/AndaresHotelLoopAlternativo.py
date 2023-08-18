indice = 20

while True:
    if indice == 13:
        indice = indice - 1
        continue
    print("Andar ", str(indice))
    indice = indice - 1
    if indice == 0:
        break