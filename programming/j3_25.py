#https://dmoj.ca/problem/ccc25j3
#CCC J3 2025

n=int(input())

lower="abcdefghijklmnopqrstuvwxyz"

negative=False
currentNum=""
for i in range(n):
    barcode=input()
    newcode=""
    counter=0
    negative=False
    currentNum=""
    for letter in barcode:
        if not letter.isnumeric():
            if currentNum!="":
                if negative:
                    counter-=int(currentNum)
                    currentNum=""
                    negative=False
                else:
                    counter+=int(currentNum)
                    currentNum=""
        if letter not in lower:
            if letter.isnumeric():
                currentNum+=letter
            elif letter == "-":
                negative=True
            else:
                newcode+=letter
    if currentNum!="":
        if negative:
            counter-=int(currentNum)
        else:
            counter+=int(currentNum)
    print(newcode+str(counter))