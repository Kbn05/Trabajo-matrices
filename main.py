import numpy as np 

month = np.random.normal(18, 33, (5, 7))
print (month)

week1=month[0,:]
week2=month[1,:]
week3=month[2,:]
week4=month[3,:]
week5=month[4,:]

for i in week1:
    if i > i:
         print (i)

