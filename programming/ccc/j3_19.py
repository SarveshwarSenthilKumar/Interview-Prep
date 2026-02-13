#https://dmoj.ca/problem/ccc19j3
#CCC J3 2019

n=int(input())

for i in range(n):
    number=0
    line=input()
    updatedLine=""
    currentChar=""
    for char in line:
        if char == currentChar:
            currentChar=char
            number+=1
        else:
            if currentChar!="":
                updatedLine+=str(number)+" "+currentChar+" "
            currentChar=char
            number=1
    updatedLine+=str(number)+" "+currentChar+" "
    print(updatedLine[:-1])