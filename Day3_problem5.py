# answer 1 ( wrong )
givenlist = [15,11,7,2]
target = 9
 
for i in range(len(givenlist)):
    for j in range(len(givenlist)):
        if givenlist[i]+givenlist[j-i]==target:
            print("return ",givenlist[i],givenlist[j])
