row1=[' ',' ',' ']
row2=[' ',' ',' ']
row3=[' ',' ',' ']
map =[row1, row2, row3]
pos=input("where do you want to keep the treasure: ")
#23
hor=int(pos[0])
ver=int(pos[1])
selectedrow=map[ver-1]
selectedrow[hor-1]='X'
print(f"{row1}\n{row2}\n{row3}\n")

