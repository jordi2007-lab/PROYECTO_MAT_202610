import random

while True:
    try:
        n=int(input("Ingresa el número de filas: "))
        if n<1:
            print("Valor inválido")
            continue
        break
    except ValueError:
        print("Dato inválido")

while True:
    try:
        m=int(input("Ingresa el número de columnas: "))
        if m<1:
            print("Valor inválido")
            continue
        break
    except ValueError:
        print("Dato inválido")

matriz=[]

for i in range (n):
    fila=[]
    for j in range(m):
        k=random.randint(0,1)
        fila.append(k)
    matriz.append(fila)

for i in matriz:
    print(i)