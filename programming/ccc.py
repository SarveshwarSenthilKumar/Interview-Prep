rows=int(input())
columns=int(input())
inputs=int(input())

gold=0

#https://dmoj.ca/submission/7601820
#CCC S2 2022

matrix=[]
# Initialize the matrix with "B"
for i in range(int(rows)):
    row=[]
    for x in range(int(columns)):
        row.append("B")
    matrix.append(row)

for i in range(int(inputs)):
    character, index = input().split()
    # Check if character is R for row
    if character=="R":
        # For each column
        for i in range(columns):
            # If the value at the index is B, change it to G and increase gold count
            if matrix[int(index)-1][i]=="B":
                matrix[int(index)-1][i]="G"
                gold+=1
            # If the value at the index is G, change it to B and decrease gold count
            else:
                matrix[int(index)-1][i]="B"
                gold-=1
    
    # Check if character is C for column
    elif character=="C":
        # For each row
        for i in range(rows):
            # If the value at the index is B, change it to G and increase gold count
            if matrix[i][int(index)-1]=="B":
                matrix[i][int(index)-1]="G"
                gold+=1
            # If the value at the index is G, change it to B and decrease gold count
            else:
                matrix[i][int(index)-1]="B"
                gold-=1

#Possible solution: use substring to change strings using multiplication of strings and slicing a single string variable as opposed to a multi dimensional array bringing down memory and time complexity

#Output the amount of gold
print(gold)