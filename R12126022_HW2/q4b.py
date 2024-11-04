num1 = input()
num2 = input()

num_List1 = num1.split(",")
num_List2 = num2.split(",")


def commonFunction(num1,num2):    
    outPutList = []
    for i in num_List1:
        for j in num_List2:
            if j == i : 
                outPutList.append(j)
    outPutList.sort()
    return outPutList

result = commonFunction(num_List1,num_List2)

answer = ",".join(result) 

if result == []:       
    print("N/A")
else :
    print(answer)

