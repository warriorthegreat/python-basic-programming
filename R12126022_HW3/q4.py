nums = input()

num = nums.split() 
num1 = int(num[0])  #x
num2 = int(num[1])  #y
#x y 都會是正整數
#如果x是奇數，乘以五減三
#如果x是偶數，除以二加ㄧ
#紀錄每一次迴圈判斷的數字，如果迴圈判斷的數字aka location 等於 y 就停止。
#記得不要直接用Index 因為永遠會少1。
#輸出該location對應x值
numList = []
numList.append(num1)            #依照題意第一個是尚未經過處理的x
location = 1                    #location == 1

if num1 == 1 and num2 ==1 : 
    print(1)    
else:                               #一開始x就等於location ，一直算下去都是2,2,2,2,2,2....
    while location < num2 :         #這樣的判斷會從1開始，對x做第一次處理就是location == 2 ,第十一次處理location == 12

        if num1 % 2 != 0 :          
            num1 = (num1 * 5) -3
            location += 1
            numList.append(num1)
        else :
            num1 = (num1 / 2) + 1
            location += 1
            numList.append(num1)

    finNum = numList.pop()

    print("{:.0f}".format(finNum))


