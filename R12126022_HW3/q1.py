# C(n, k)，其中n,k為正整數。
# order is k and n，第一個輸入代表k，第二個輸入代表n
#必須保證 0 < k < n ，讓使用者一直輸入到正確為止。
#如果 k > n ，除了重新讓使用者輸入，也需要印出：“Error! k > n, please input again!”
#從n個元素中取出k個元素，k個元素的組合數量，就是排列組合。
#公式 ： n! /( k!(n-k)!)

def factorial(x):
    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))

nums = input("")
numList = nums.split() 
num_k = int(numList[0]) #k
num_n = int(numList[1]) #n

while True:
    if num_k < 0 or  num_n < 0 : #如果k n 都小於0 ，就不輸出任何提示讓user重打。都大於0則繼續判斷
        nums = input("")
        numList = nums.split() 
        num_k = int(numList[0]) #k
        num_n = int(numList[1]) #n  
    elif num_k == num_n :       #如果 k, n 相等，不輸出任何提示讓user重打。兩者為不同數字繼續判斷
        nums = input("")
        numList = nums.split() 
        num_k = int(numList[0]) #k
        num_n = int(numList[1]) #n  
    elif num_k > num_n :        # #如果 k > n ，輸出任何提示讓user重打。直到k < n 繼續判斷。
        print("Error! k > n, please input again!")
        nums = input("")
        numList = nums.split() 
        num_k = int(numList[0]) #k
        num_n = int(numList[1]) #n 
    else : 
        break   #至此n > k > 0, 計算階乘


#公式 ： n! /( k!(n-k)! )

numerator = factorial(num_n)
denominator = factorial(num_k)* factorial(num_n - num_k)

answer = int(numerator / denominator)

print(answer)
