ti = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ui = [10.2, 8.3, 5.4, 4.1, 2.2, 0, -1.6, -3.9, -5.9, -7.8]

ti2 = [i * i for i in ti]

tu = [ti[i] * ui[i] for i in range(len(ti))]


k = -1636.0 / 825
b = 9905.5 / 825

yi_ = [k * ti[i] + b for i in range(len(ti))]

nev = [ui[i] - yi_[i] for i in range(len(ti))]
nev2 = [nev[i] ** 2 for i in range(len(ti))]

# for i in range(len(ti)):
#     print(ti[i], ui[i], ti2[i], tu[i], yi_[i], round(nev[i], 2), round(nev2[i], 4))

print(k * 12 + b)

# for x in range(1, 11):
#     print(k * x + b)
