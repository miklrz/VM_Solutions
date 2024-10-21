import math

x = []
for i in range(13):
    x.append(0.15 + 0.05 * i)
# Список значений из второго столбца
y = [
    0.860708,
    0.818731,
    0.778801,
    0.740818,
    0.704688,
    0.670320,
    0.637628,
    0.606531,
    0.576950,
    0.548812,
    0.522046,
    0.496585,
    0.4722367,
]

h = 0.05

x3 = 0.1430
x4 = 0.80

q3 = (x3 - x[0]) / h
q4 = (x4 - x[0]) / h

q = q4

yd1 = [y[i + 1] - y[i] for i in range(len(y) - 1)]
yd2 = [yd1[i + 1] - yd1[i] for i in range(len(y) - 2)]
yd3 = [yd2[i + 1] - yd2[i] for i in range(len(y) - 3)]

# for i in range(len(y)):
#     print(y[i], end=" ")
#     if i < len(y) - 1:
#         print(yd1[i], end=" ")
#     if i < len(y) - 2:
#         print(yd2[i], end=" ")
#     if i < len(y) - 3:
#         print(yd3[i], end=" ")

#     print("\n")

y_x = (
    y[0]
    + q * yd1[0]
    + ((q * (q - 1) / math.factorial(2)) * yd2[0])
    + (((q * (q - 1) * (q - 2)) * yd3[0]) / math.factorial(3))
)
print(y_x)
