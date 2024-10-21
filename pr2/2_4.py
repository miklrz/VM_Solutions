import matplotlib.pyplot as plt
import matplotlib

matplotlib.use("Agg")

# Данные
x_values = [14, 15, 17, 19, 20, 21, 22, 24, 27, 32]
y_values = [70, 69.5, 68.5, 67.5, 66, 65, 64.5, 62.5, 60, 53.5]

# Построение графика
plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values, marker="o", color="b", label="y vs x")

# Настройки графика
plt.title("График зависимости y от x")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.legend()

# Показать график
plt.show()
