import math

# Example
# Массив x
# x = [0.101, 0.106, 0.111, 0.116, 0.121, 0.126]
# # Массив y
# y = [1.26183, 1.27644, 1.29122, 1.30617, 1.32133, 1.3366]
# x_ = 0.1157
# h = 0.005

x = [0.150, 0.155, 0.160, 0.165, 0.170, 0.175]
# Массив y
y = [6.61659, 6.39989, 6.19658, 6.00551, 5.82558, 5.65583]
x_ = 0.1521
h = 0.005

n = len(x) - 1
t = round((x_ - x[0]) / h, 2)
t_i = [t - i for i in range(n + 1)]
P = 1
for _ in t_i:
    P *= _

C_i = []
for i in range(len(x)):
    C = ((-1) ** (n - i)) * math.factorial(i) * math.factorial(n - i)
    C_i.append(C)

f1 = []
f2 = []
for i in range(n + 1):
    f = (t_i[i]) * C_i[i]
    f1.append(f)

for i in range(n + 1):
    f = y[i] / f1[i]
    f2.append(f)

E = sum(f2)

f_x = P * E
print("  x   |   y   |   t  |   c   |   f1   |   f2   |  ")
for i in range(n + 1):
    print(x[i], y[i], t_i[i], C_i[i], f1[i], f2[i], sep=" | ")
print("P: ", P)
print("E: ", E)
print("f(x) ", f_x)
