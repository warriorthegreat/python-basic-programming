"""
1.給一個txt. 用utf- 8 讀，txt檔案中未有n個學生，每個人都有三個科目。
2.學生的分數是整數而且不小於 0

資料格式
txt檔案的第一排 ：學生人數n ， 1 <= n <= 100  
第二排後 ： 學生編號 ＋ 科目一分數 ＋ 科目二分數 ＋ 科目三分數，每一個項目都用空格隔開ㄡ
例子：

4
1 70 73 62
2 63 90 92
3 73 68 60

要求：
讀txt計算每個學生總分，找到最高分的學生。

輸出：
最高分的學生編號, 總分
例子：
4, 254

提示 ：只有一組最高分的學生
"""

#測資只有1個

#輸入檔案名
fname  = input()
#讀取檔案
fRead  = open(fname, "r", encoding = "utf-8")
#不確定有多少行，但因為有學生所以猜測至少會有兩行（至少有一個學生人數 ＋ 學生）
fList = fRead.readlines()   #放進去list
fLen = len(fList) #list的長度，代表有多少個小list , -1就代表學生數。

#開始for loop計算分數，除了第一行跳過，設定range從1 開始（因為list中的第一個是0 ，第二的index才是1）
#第一層從 index 開始，第二層for loop 從index 0 開始。因為需要紀錄位於index 0 的學生編號，之後將index 1, 2, 3的str轉int加起來 (分數都是整數)
#把學生編號和總分傳進去一個list中，之後如果新的學生分數更高，就傳進去list中，然後舊的remove() 掉。新的留下來最後pop 拿出來。
#最後再想想要怎麼遵守 「學生編號, 總分」的格式。

scoreList = []
stuScore = []
stuNum = []

for i in range (0, fLen)  :  
    if i == 0 :        #第一個不用讀取    
        pass
    else : 
        num  = fList[i].split()
        scoreList.append(num)

#算分數

for a in range(0, fLen - 1):
    score = 0                               #個別學生總分數為0，每次換學生加總時重置。
    for j in range(0, 4):
        if j == 0 :                         #如果j = 0 ，加進學生編號list中。
            stuNum.append(scoreList[a][j])
        else :                              #如果j != 0 ，把對應的分數加起來
            subjNum = int(scoreList[a][j])
            score += subjNum                #總分 += 科目分數。
    stuScore.append(score)

#找出最高的分數以及對應編號：
beststuNum = stuScore.index(max(stuScore))+1
print(beststuNum, max(stuScore), sep = ",")

            
