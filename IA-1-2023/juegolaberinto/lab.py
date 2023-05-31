import  random
filas=4
columnas=4
mapa=[]
paredes=8
espacios=filas*columnas-paredes
for i in range(0, filas):
    fila = []
    for j in range(0, columnas):
        fila.append(1)
    mapa.append(fila)
posicionfilaI=0
posicioncolumnaI=0
mapa[posicionfilaI][posicioncolumnaI] = 0
espaciogenerado=1
while espaciogenerado < espacios:
    direccion = random.randrange(3)
    if direccion == 0 and posicionfilaI > 0:
        posicionfilaI -= 1 #izquierda
    elif direccion == 1 and posicionfilaI < filas - 1:
        posicionfilaI += 1 #derecha
    elif direccion == 2 and posicioncolumnaI > 0:
        posicioncolumnaI -= 1 #arriba
    else:
        if posicioncolumnaI < columnas - 1:
            posicioncolumnaI += 1 #abajo
    if mapa[posicionfilaI][posicioncolumnaI] == 1:
        mapa[posicionfilaI][posicioncolumnaI] = 0
        espaciogenerado += 1
posicionfilaF=3
posicioncolumnaF=3
mapa[posicionfilaF][posicioncolumnaF]=2
for f in mapa:
 print(f)