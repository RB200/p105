import math
import csv
with open('data.csv',newline='') as f:
    reader=csv.reader(f)
    file_data=list(reader)
data=file_data[0]

def getMean(data):
    x=len(data)
    total=0
    for i in data:
        total+=int(i)
    mean=total/x
    return mean

sq_list=[]
for num in data:
    b=int(num) - getMean(data)
    b= b**2
    sq_list.append(b)

sum=0
for i in sq_list:
    sum=sum+i
result=sum/(len(data)-1)
stdev=math.sqrt(result)
print(stdev)