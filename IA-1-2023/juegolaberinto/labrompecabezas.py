inicio=[1, 2, 3, 4]
final=[1, 2, 3, 4]
resuelto=False
revisados=[]
frontera=[]
while not resuelto:
    visitados=inicio.pop()
    if inicio == visitados:
        print("resultado encontrado:" +final)
        resuelto= True
    else:
        estado1 = [inicio[2], inicio[1], inicio[3], inicio[0]]
        estado2 = [inicio[0], inicio[2], inicio[1], inicio[3]]
        estado3 = [inicio[0], inicio[1], inicio[3], inicio[2]]
        print(estado1)
