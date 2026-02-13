#https://dmoj.ca/problem/ccc14s1
#CCC S1 2014

friends=int(input())
rounds=int(input())

invitees=[]

for i in range(1, friends+1):
    invitees.append(i)

for i in range(rounds):
    r=int(input())
    newInvitees=[]
    for j in range(len(invitees)):
        if (j+1)%r!=0:
            newInvitees.append(invitees[j])
    invitees=newInvitees

for i in invitees:
    print(i)