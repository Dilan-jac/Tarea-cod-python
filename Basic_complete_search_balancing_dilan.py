N = int(input())
vacas = []

for _ in range(N):
    x, y = map(int, input().split())
    vacas.append((x, y))

respuesta = 10**9

for vaca1 in vacas:
    for vaca2 in vacas:
        cerca_x = vaca1[0]
        cerca_y = vaca2[1]

        superior_izq = 0
        superior_der = 0
        inferior_izq = 0
        inferior_der = 0

        for x, y in vacas:
            if x <= cerca_x and y > cerca_y:
                superior_izq += 1
            elif x > cerca_x and y > cerca_y:
                superior_der += 1
            elif x <= cerca_x and y <= cerca_y:
                inferior_izq += 1
            elif x > cerca_x and y <= cerca_y:
                inferior_der += 1

        maximo = max(superior_izq, superior_der, inferior_izq, inferior_der)

        if maximo < respuesta:
            respuesta = maximo

print(respuesta)

