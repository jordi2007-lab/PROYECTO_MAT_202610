import random

def crear_matriz(m,n):
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
        print (*i)

    return matriz


matriz=crear_matriz(0,0)


def matriz_basica(matriz):
    mb = []
    for i in matriz:
        if i not in mb:
            mb.append(i)
    print("nueva")      
    for i in mb:
        print(*i)
    return mb


matrizbasica=matriz_basica(matriz)



