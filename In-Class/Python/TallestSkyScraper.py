def calc(buildings):
    for i in buildings:
        if 1 in i:
            print(len(buildings) - buildings.index(i))
            break
        

calc(
    [
    [0,1,0,0],
    [0,1,0,0],
    [0,1,1,0],
    [1,1,1,1,]
    ]
)