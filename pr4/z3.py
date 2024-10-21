import math
def y_func(x):  
    return math.tan(pow(x,2))/(pow(x,2) + 1)

def y_func_test(x):
    return math.sin(2*x-2.1)/(pow(x,2)+1)
# 3
# h = 0.1
# a = 0.2
# b = 1

#test
h = 0.05
a = 1.2
b = 1.6

x = []
y = []
for i in range(0,9):
    xi = a + h*i
    yi = y_func_test(xi)
    x.append(xi)
    y.append(yi)


I = h/3
_ = y[0]+y[8]

sum1=0
for i in range(1,8,2):
    sum1+=y[i]
_+=sum1*4

sum2 = 0
for i in range(2,7,2):
    sum2+=y[i]
_+=sum2*2

I*=_

yp1 = []
yp2 = []
yp3 = [] 
yp4 = []

for i in range(len(y)-1):
    yp1.append(y[i+1] - y[i])


for i in range(len(yp1)-1):
    yp2.append(yp1[i+1] - yp1[i])

for i in range(len(yp2)-1):
    yp3.append(yp2[i+1] - yp2[i])

for i in range(len(yp3)-1):
    yp4.append(yp3[i+1] - yp3[i])

# for i in range(len(y)):
#     print(y[i], end = " ")
#     if i < len(yp1) : print(yp1[i],end= " ")
#     if i < len(yp2) : print(yp2[i], end = " ")
#     if i < len(yp3) : print(yp3[i], end = " ")
#     if i < len(yp4) : print(yp4[i], end = " ")
#     print()


# print(y[0]+y[8],sum1,sum2,sep=" ")
# print(I)
