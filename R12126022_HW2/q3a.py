numStr = input()

numStrList = numStr.split(",")  #轉list 

mappingList = [] #已經輸入過的數字放在這邊
outputList = [] #用來輸出的list

for i in numStrList : 
    if i not in mappingList :       #如果
        mappingList.append(i)
        outputList.append(i)
    else :
        pass

outputList.sort()       # 排序
result = ",".join(outputList)       #用逗號串接list內容
print(result)       # 輸出。

    

