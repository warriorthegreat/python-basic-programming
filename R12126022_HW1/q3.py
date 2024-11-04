
#先判斷是否是質數，再度判斷是奇數與偶數
num = int(input())
prime = True
answerList = ["Prime", "Odd"]


#質數判斷 ： 質數定義包含1 & 自己=> 判斷重點是質數只考慮範圍2～自己前一個數，loop測試
#不考慮2 因為2本身因數就是12 在這情況下一定只有自己＆1。

for i in range(2, num) :
        if num % i  == 0 : 
            prime = False #只要檢測到一個餘數是0，就不是質數
            answerList[0] = "Not Prime"


#奇數（odd） 偶數 (even) 判斷
if num % 2 != 0 :
    odd= True
else : 
    odd = False
    answerList[1] = "Even"

#輸出
print(answerList[0] + "," + answerList[1])



