ccc = True
while ccc == True:
    print(f"目前的 ccc 值: {ccc}")  # 用來檢查 ccc 的值是否改變
    try: 
        num = int(float(input("輸入數字: ")))  # 確保輸入是數字
    
    except:
        print("有錯誤，請輸入數字")
    
    else:
        print("沒有錯歐恭喜")
        ccc = False  # 正確輸入後跳出循環
        print(f"更改後的 ccc 值: {ccc}")  # 檢查 ccc 是否變為 True
        

print("程式結束")