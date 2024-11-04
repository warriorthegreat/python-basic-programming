num = input() #要轉換成字串，才能切成list
numList = num.split()
num1 = int(numList[0])
num2 = int(numList[1])
if num1 < 0  or num1 > num2 : #防呆，以防輸入錯誤。
    print("錯誤，重新執行")
    num = input()
    numList =  num.split()      
    num1 = int(numList[0])
    num2 = int(numList[1])
else :
    pass

resultList = []

#範圍 ：2 - num  ，i 一開始2 
#數字沒辦法在條件裡進行迭代，所以一開始要有一個數字寫在外面。
#所以 每一個迴圈之後要加一， => i = 2,3,4.....
#每一個數字進行判斷

def isPrime(num):
    i = 2 
    if num < 2 : 
        return False           #如果 num < 2 不會是質數，跳下一個。
    
    while i < num :             #當i小於 num
        if num % i  == 0 :      #如果num除以i可以被整除代表不是質數，
            return False
        i += 1                  #+1換下一個數
    else :                      #其他的狀況都是質數，印出來。
        return True

while num1 <=  num2 :           #當num1 <= num 2 , 2 <= 33
    if isPrime(num1):
        resultList.append(str(num1))
    num1 +=1

if resultList == [] : 
    print(0)
else : 
    result = ",".join(resultList)
    print(result)


    











