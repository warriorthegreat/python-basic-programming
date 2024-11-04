elements = input()
elements_list = elements.split(",")

#轉換成list 把值變成float #運算子保持原樣
operator = elements_list[0]
num1 = float(elements_list[1])
num2 = float(elements_list[2])

#放在前面，否則後面除的時候會直接float division by zero
if num2 == 0 :
    print("Error")

#感覺這樣做有點沒效率
elif operator == "+" :
    result = num1 + num2
    print("{:.2f}".format(result))
elif operator == "-" :
    result = num1 - num2
    print("{:.2f}".format(result))
elif operator == "*" :
    result = num1 * num2
    print("{:.2f}".format(result))
elif operator == "/" :
    result = num1 / num2
    print("{:.2f}".format(result))


