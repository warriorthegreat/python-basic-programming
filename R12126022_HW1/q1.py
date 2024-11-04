numbers = input() #輸入身高（公尺），體重（公斤）
number = numbers.split() #變list

#對list內部值進行操作。
height = float(number[0]) 
weight = float(number[1])

bmi = weight / (height ** 2)

print("{:.2f}".format(bmi)) #用format改變顯示位數


