import matplotlib.pyplot as plt

# Список метрик
metrics = ['Precision', 'Recall', 'mAP50', 'mAP50-95']

# Список моделей/выборок
x = ['n_val', 'n_test','s_val', 's_test', 'm_val', 'm_test']

# Списки величин метрик по каждой модели/выборке
y1 = [0.974, 0.976, 0.986, 0.986, 0.969, 0.982] # Precision
y2 = [0.967, 0.963, 0.977, 0.973, 0.966, 0.949] # Recall
y3 = [0.985, 0.983, 0.99, 0.989, 0.982, 0.98] # mAP50
y4 = [0.821, 0.832, 0.852, 0.856, 0.845, 0.853] # mAP50-95

# Создаём "канвас" для четырех графиков
fig, axes = plt.subplots(2, 2, figsize=(10, 8))

axes[0, 0].bar(x, y1)
axes[0, 0].set_yscale('log')
axes[0, 0].set_title(metrics[0])
axes[0, 0].set_ylabel('%')

axes[0, 1].bar(x, y2)
axes[0, 1].set_yscale('log')
axes[0, 1].set_title(metrics[1])
axes[0, 1].set_ylabel('%')


axes[1, 0].bar(x, y3)
axes[1, 0].set_yscale('log')
axes[1, 0].set_title(metrics[2])
axes[1, 0].set_ylabel('%')

# Plot the fourth subplot
# Plot the second subplot
axes[1, 1].bar(x, y4)
axes[1, 1].set_yscale('log')
axes[1, 1].set_title(metrics[3])
axes[1, 1].set_ylabel('%')

fig.tight_layout()

plt.show()
