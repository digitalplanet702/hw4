#1
for i in range(10, 21, 1):
    print(i, end= " ");
#2
for i in range(10, 21, 2):
    print(i, end= " ");
#3
gap: int = int (input("please enter the gap:"))

for i in range(10, 21, gap):
    print(i, end= " ");

#4
startpoint: int = int (input("please enter the start point:"))
endpoint: int = int (input("please enter the end point:"))
gap: int = int (input("please enter the gap:"))

for i in range(startpoint, endpoint, gap):
    print(i, end= " ");