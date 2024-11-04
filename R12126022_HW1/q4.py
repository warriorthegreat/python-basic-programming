#Write a program that calculates the sum of the digits in and the length of a string entered by the user. 
#The first output is sum, and then the length of a string.

#Hint 1: only numbers and letters in a string
#Hint 2: if there are no numbers in a string, the sum is 0

string = input() 
length = len(string)
 # 計算字串長度

num = 0 # 數字預設為0，也預防沒有數字
numList = ["0","1","2","3","4","5","6","7","8","9"] 
markList = list(string) #轉list，包含所有字串的分割
for i in markList : #for 迴圈一個個挑出來
    if i in numList :
        num += int(i)  #0+是數字的值。 

print(num,",",length)
