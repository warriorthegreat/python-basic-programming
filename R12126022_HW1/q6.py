num = input()
ansList = [] #儲存答案並sort
#轉list
numList = num.split(" ")
print(numList)

a = float(numList[0])
b = float(numList[1])
c = float(numList[2])

discriminant = (b ** 2)-(4 * a * c) #判別式
if discriminant >= 0 :
    root1 = (-b - (discriminant ** 0.5))/ (2 * a)
    ansList.append(root1)
    root2 = (-b + (discriminant ** 0.5))/ (2 * a)
    ansList.append(root2) #加入list

ansList.sort() #排序由小到大
ansList.reverse() #排序反轉 ＝ 大到小
print("{:.3f}".format(ansList[0])," ","{:.3f}".format(ansList[1]))