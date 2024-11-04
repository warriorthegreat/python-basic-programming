numStr1 = input()
numStr2 = input()

numStr1_List = numStr1.split(",")
numStr2_List = numStr2.split(",")
outPut_List = []
for i in numStr1_List :         #取出numStr1_List元素
    if i in numStr2_List :      #如果numStr1_List元素有對應到numStr2_List
        outPut_List.append(i)   #把該數字放置到outPut_List

outPut_List.sort()              #list排序
result = ",".join(outPut_List) #整理列表，並且用","連接

if outPut_List == []:       #空列表 ＝ 沒有任何符合元素
    print("N/A")
else :
    print(result)
    