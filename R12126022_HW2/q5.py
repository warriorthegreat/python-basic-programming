binaryStr = input()

#slice成list => 1,1,0,1
#正取 => 2**3 + 2**2 + 0**1 + 2**0 
#判斷有多少個位元 ： 
elements = list(binaryStr)
binaryLen = len(elements) 
result = 0 

 
for i in elements :
    binaryLen -= 1         #4-1 = 3, ....1-1 = 0
    biNum = int(i) * 2 ** (binaryLen)       # 1 * 2 ** 3
    result += biNum     # result = result + 2**3 
    

print(result)



