numStr = input()

numList = numStr.split(",") #字串以","分割成list

setNum = set(numList) #list 轉set 
answer = sorted(setNum)
result = ",".join(answer)
print(result)