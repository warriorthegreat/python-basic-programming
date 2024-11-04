import random

seed = int(float(input()))

list_num = []

    

write_txt = open("30numbers","wt", encoding = "utf-8")
for i in range (30) : 
    num = random.randint(-100, 100)
    write_txt.writelines(num)
write_txt.close()

read_txt = open("30numbers", "rt", encoding= "utf-8")
numread = read_txt.readlines
list_num.append(numread)