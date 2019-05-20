stairRNum=int(input())

#answer 1
for i in range(stairRNum):
    for j in range(stairRNum-i):
        print("*", end='')
    print("")

#answer 2
for i in range(stairRNum):
    print("*"*(stairRNum-i))

#answer 3
for i in range(stairRNum,0,-1):
    print("*"*i)

#answer 4
for i in reversed(range(StairRNum)):
    print("*"*i)