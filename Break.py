saifullahlist = ["saifullah", "chayan", 4, 5, 6, 7, 8, 9,10]

for x in range(len(saifullahlist)):
    if x == 4:
        break
    print(x)
    
for x in range(len(saifullahlist)):
    if x == 4:
        continue
    print(saifullahlist[x])