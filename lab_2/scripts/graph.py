# import pandas as pd
# import matplotlib.pyplot as plt

# data = pd.read_csv("/Users/aloevartyom/Documents/dev/test/lab_2/data/results.csv")

# plt.plot(data["Number"], data["Base ms"], label="Base")
# plt.plot(data["Number"], data["Miller ms"], label="Miller")
# plt.xlabel("Number")
# plt.ylabel("Time (ms)")
# plt.legend()
# plt.title("Benchmark of prime number algs")
# plt.show()
import pandas as pd
import matplotlib.pyplot as plt

# Загрузка данных
data = pd.read_csv("/Users/aloevartyom/Documents/dev/test/lab_2/data/results.csv")

# Создание подграфиков
fig, ax = plt.subplots(2, 1, figsize=(10, 8))  # Два подграфика, размер 10x8

# График для Base
ax[0].plot(data["Number"], data["Base ms"], label="Base", color="blue", linestyle="-")
ax[0].set_title("Base Algorithm Benchmark")  # Заголовок для первого графика
ax[0].set_xlabel("Number")
ax[0].set_ylabel("Time (ms)")
ax[0].legend()  # Легенда
ax[0].grid(True)  # Сетка

# График для Miller
ax[1].plot(data["Number"], data["Miller ms"], label="Miller", color="red", linestyle="--")
ax[1].set_title("Miller-Rabin Algorithm Benchmark")  # Заголовок для второго графика
ax[1].set_xlabel("Number")
ax[1].set_ylabel("Time (ms)")
ax[1].legend()  # Легенда
ax[1].grid(True)  # Сетка

# Упорядочение макета
plt.tight_layout()  # Для корректного отображения графиков без наложений
plt.show()