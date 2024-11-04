num = input()
numList =  num.split()      #list
num1 = int(numList[0])
num2 = int(numList[1])

if num1 < 0 or num1 > num2 : #防呆，以防輸入錯誤
    print("錯誤，重新執行")
    num = input()
    numList =  num.split()      
    num1 = int(numList[0])
    num2 = int(numList[1])
else :
    pass

def isPrime(num):
    if num < 2 :
        return False        #非質數
    for i in range(2,num):
        if num % i == 0 :
            return False    #非質數
    return True             #是質數


outPutList = [ ]
for i in range (num1,num2+1) : # i = 2,3, ... num 
    if isPrime(i) == True:          #如果是質數
        outPutList.append(str(i))   #轉換成字串加進輸出列表
    else :
        continue                    #非質數就啥都不做。

if outPutList ==  [] : 
    print(0)
else:
    result = ",".join(outPutList)
    print(result)