import matplotlib.pyplot as plt


x = [1, 2, 3, 4, 5, 6, 7]

y = [1, 2, 3, 4, 5, 6, 7]


plt.step(x, y, where='pre', color='blue', linewidth=2, label="Step Shape")

plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Staircase (Step) Line using Matplotlib")
plt.legend()
plt.grid(True)

plt.show()
