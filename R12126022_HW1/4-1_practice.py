def oddOrOther( x, y ):
    # 判斷 x 是奇數還是偶數
    if x % 2 != 0:
        x_result = "N"
    else:
        x_result = "Y"
    
    # 判斷 y 是奇數還是偶數
    if y % 2 != 0:
        y_result = "N"
    else:
        y_result = "Y"
    
    # 同時回傳 x 和 y 的結果
    return "{0}{1}".format(x_result, y_result) #這邊他會輸出tuple所以在此把他tuple的樣式弄掉

# 測試
print((oddOrOther(103, 29802))) 
print((oddOrOther(378, 872))) 
