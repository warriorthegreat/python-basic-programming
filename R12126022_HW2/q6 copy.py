from datetime import datetime

date = input()
dateList = date.split(",")
d1Str = map(int,dateList[0])
d2Str = map(int,dateList[1])



date1 = datetime.strftime(d1Str, "%Y-%m-%d")
date2 = datetime.strftime(d2Str, "%Y-%m-%d")
days = (date1 - date2)
print(days)
    
