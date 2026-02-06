#https://dmoj.ca/problem/ccc02s2
#CCC S2 2002

numerator=int(input())
denominator=int(input())

whole=int(numerator/denominator)
remainder=numerator%denominator

bestdenom=denominator

if remainder==0:
    print(whole)
else:
    for i in range(1, remainder+1):
        if denominator%i==0 and numerator%i==0:
            bestdenom=i
    print(whole, str(int(remainder//bestdenom)) + "/" + str(int(denominator//bestdenom)))