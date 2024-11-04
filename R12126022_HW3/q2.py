#計算機
#要讀取文件獲取資料，計算後輸出至特定文件內。
#輸入格式 ： num1  operator  num2。可能是float 
#運算子 ：+, - ,*, / 。
#輸出 ： 可能是float 。
"""
輸入判斷和運算格式判斷 ： 
0. 輸入文件名與輸出文件名需要寫在同一行，以逗號分隔。
1. 沒有輸入的文件，螢幕的呈現是：File not found。

以下為格式判斷：
2. 運算子非 +, - ,*, /，輸出 Operator error。
3. 當運算子是 / ，但是除數 = 0 ，輸出 Cannot divide by zero
4. 輸入只有num1 num2 沒有運算子，輸出Operator lost
5. 輸入只有運算子 num2 沒有num1，輸出Number1 lost
6. 輸入只有num1 運算子 沒有num2，輸出Number2 lost。

"""
"""
輸出條件 ：
1. 輸出計算結果到文件
2. 如果輸出成功，顯示 Successfully
3. 不論有沒有error，都必須輸出Execution completed，在螢幕作為結尾。
4. 如果沒有找到輸出文件，則輸出File not found，輸出的文件內容則是空的。
"""
"""
先input輸入文件名，並且以list分隔。
try 儲存後把第一個文件名讀取，因為需要找到文件代表這文件一定存在，因此用read就可以。
except 如果沒有找到文件，就輸出File not found ＆ Execution completed，記得這邊要先生成文件再來關掉程式（沒有要求要輸入到對為止。）

else 如果有找到文件，開始判斷輸入格式是否正確，讀取後看格式能否拆成三份，如果可以拆成三份，代表沒有遺漏可以直接判斷格式是否有1, Operator error ＆ 2. Cannot divide by zero 。
如果拆不了三份代表有遺漏。
3. 如果第一格為op就是num1不見。
4. 如果第二格 = op ，代表num2不見。
5. 如果第二格不是op，代表op不見。

跑以上五個條件。沒有滿足就輸出對應錯誤，並且print : Execution completed
如果以上都滿足，就開始運算，把運算結果用write寫進文件中，無論如何都會輸出某文件，代表要創造一個儲存結果的新文件。
螢幕輸出 ：
Successfully
Execution completed

找到文件後讀取，開始判斷
如何將其儲存資料並進行運算？

"""

fname = input()
fname_list = fname.split(",") #用逗號切
try :
    fopen = open(fname_list[0], "r", encoding = "utf-8") #不確定檔案是否存在，不用with open .. 
except:
    print("File not found")
    print("Execution completed")
    fopen  = open(fname_list[1], "w", encoding = "utf-8") 
    exit()

else :
    num1List = []
    num2List = []
    opList = []
    opmap = [ "+", "-", "*", "/"]
    fstr = fopen.readline() #內容只有一行
    fstr_list = fstr.split() #依照算式中的空白分割成三等份。 如 （1 + 2 ）
    fstr_len = len(fstr_list) #看list是否內部有三個元素，確定元素有無遺漏

    if fstr_len < 3 :  #no 3 elements ，設定上最少會有2 elements
        if fstr_list[0] in opmap  :   #該是數字卻能找到operator，代表num1消失
            print("Number1 lost")
            print("Execution completed")
        elif fstr_list[1]  in opmap : 
            print("Number2 lost")
            print("Execution completed")
        elif fstr_list[1] not in opmap : 
            print("Operator lost")
            print("Execution completed")
    elif  fstr_len == 3 : #3 ele , 代表格式正常
        num1List.append(fstr_list[0])
        num2List.append(fstr_list[2])
        opList.append(fstr_list[1])    #這邊先分成三個列表，進行運算
        
        if opList[0]  not in opmap : #判斷運算子錯誤
            print("Operator error")
            print("Execution completed")
        else : 
        
        
            if opList[0] == "+" :
                answer = float(num1List[0]) + float(num2List[0])
            elif opList[0] == "-" : 
                 answer = float(num1List[0]) - float(num2List[0])
            elif opList[0] == "*" : 
                 answer = float(num1List[0]) * float(num2List[0])
            #try是否除數為0，如果不是就正常除，接續else繼續計算；是就接except輸出後終止程式。
            try : 
                if opList[0] == "/" :
                     answer = float(num1List[0]) / float(num2List[0])
            except : 
                print("Cannot divide by zero")
                print("Execution completed")
                
            else : 
                fout = open (fname_list[1], "wt" ,encoding= "utf-8")
                fout.write(str(answer))
                fout.close()
                print("Successfully")
                print("Execution completed")

