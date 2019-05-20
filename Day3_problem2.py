stairNum=int(input())

#answer 1
for i in range(stairNum):
    for j in range(i+1):
        print("*",end='')
    print("")

#answer 2
for i in range(stairNum):
    print("*"*(i+1))