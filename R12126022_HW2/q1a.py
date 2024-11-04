sentence  =  input ()

#以空格切，變成list
senSplit = sentence.split(" ")

#反轉字串 ＝空
revSentence = ""

#用一個迴圈把字串黏回去。
for i in senSplit :
    revSentence = i +" "+revSentence

#切掉多餘空格
output = str.strip(revSentence)

#輸出
print(output)


