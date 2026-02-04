rows=int(input())
columns=int(input())
inputs=int(input())

gold=0

#https://dmoj.ca/submission/7601820
#CCC S2 2022

matrix=[]
for i in range(int(rows)):
    row=[]
    for x in range(int(columns)):
        row.append("B")
    matrix.append(row)

for i in range(int(inputs)):
    character, index = input().split()
    if character=="R":
        for i in range(columns):
            if matrix[int(index)-1][i]=="B":
                matrix[int(index)-1][i]="G"
                gold+=1
            else:
                matrix[int(index)-1][i]="B"
                gold-=1
    elif character=="C":
        for i in range(rows):
            if matrix[i][int(index)-1]=="B":
                matrix[i][int(index)-1]="G"
                gold+=1
            else:
                matrix[i][int(index)-1]="B"
                gold-=1

#Possible solution: use substring to change strings using multiplication of strings and slicing a single string variable as opposed to a multi dimensional array bringing down memory and time complexity

print(gold)