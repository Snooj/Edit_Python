array_In=input("Input :")
array_Even=[] ; array_Odd=[]

for i in range(len(array_In)):
    if array_In[i]%2==0:
        array_Even.append(array_In[i])
    else:
        array_Odd.append(array_In[i])

print("Output :", array_Even.extend(array_Odd))