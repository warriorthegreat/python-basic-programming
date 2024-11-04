passWord = input()

#判斷式
lenPassWord = len(passWord)
if lenPassWord < 6 : 
    print("Weak")
elif 6 <= lenPassWord <= 10 :
    print("Moderate")
elif lenPassWord > 10 :
    print("Strong")