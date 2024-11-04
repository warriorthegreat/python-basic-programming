from datetime import datetime

date = input()
dateList = date.split(",")
d1Str = dateList[0]
d2Str = dateList[1]

try :
    date1 = datetime.strptime(d1Str, "%Y-%m-%d")
    date2 = datetime.strptime(d2Str, "%Y-%m-%d")
    print(date1)
    days = abs((date1 - date2).days)
    print(days)
    
except : 
    print("Invalid")