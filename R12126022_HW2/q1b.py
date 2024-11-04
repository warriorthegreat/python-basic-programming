sentence  =  input ()

#以空格切，變成list
senSplit = sentence.split(" ")

#反轉字串，從右側取值
revSentence = senSplit[::-1]

#反轉後用空格連接單字，join
result = " ".join(revSentence)

#輸出
print(result)

