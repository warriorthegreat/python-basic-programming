

# 4-1
import random

seed = int(input())
random.seed(seed)

print("Random data is as follows.")
# generate 30 data between -100 and 100
for i in range(30):
    tempnum = random.randint(-100, 100)
    print("No.",i+1,":", tempnum)


# In[ ]:


# 4-2
# open file for writing data
f = open("30numbers.txt", "w", encoding="utf-8")

f.write(str(111)+"\n")
print(111, file = f)

# close file
f.close()


# read file and save data to list
listnum = []
f = open("30numbers.txt",  "r",encoding="utf-8")
for line in f.readlines():
    listnum.append(int(line.strip()))
f.close()

"""
# print data in list
for item in listnum:
  print(item)
"""


# In[ ]:


# 4-3
# define function to compute mean
def calmean(l):
    return sum(l) / len(l)
    """
    # Other 2 ways
    sum = 0
    for i in range(len(l)):
        sum += l[i]
    return sum/len(l)

    sum = 0
    for i in l:
        sum += i
    return sum/len(l)
    """        

# define function to compute std
def calvariance(l, m):
    variance = sum([((x - m) ** 2) for x in l]) / len(l)
    res = variance ** 0.5
    return res
    """
    # Another way
    sum = 0
    for x in l:
        sum += (x - m) ** 2
    res = (sum / len(l)) ** 0.5
    
    return res
    """    

# calculate mean
meanvalue = calmean(listnum)
print("mean: ", meanvalue)
#print("mean: ", meanvalue, file=f)

# calculate std
std = calvariance(listnum, meanvalue)
print("std: ", std)
#print("std: ", std, file=f)


# In[ ]:


# 4-4
def compare(res, seed):
    if (res > seed):
        return True
    else:
        return False

# Compare std and seed
result = compare(std, seed)


# In[ ]:


# 4-5
f = open("30number.txt", "a", encoding="utf-8")

print("xxxxxx", file=f)

f.close()

