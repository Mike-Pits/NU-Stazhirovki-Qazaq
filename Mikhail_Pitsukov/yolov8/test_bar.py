import matplotlib.pyplot as plt

# Sample data
metrics = ['Precision', 'Recall', 'mAP50', 'mAP50-95']
x = ['n_val', 'n_test','s_val', 's_test', 'm_val', 'm_test']

y1 = [0.974, 0.976, 0.986, 0.986, 0.969, 0.982]
y2 = [0.967, 0.963, 0.977, 0.973, 0.966, 0.949]
y3 = [0.985, 0.983, 0.99, 0.989, 0.982, 0.98]
y4 = [0.821, 0.832, 0.852, 0.856, 0.845, 0.853]

# Create a figure with four subplots
fig, axes = plt.subplots(2, 2, figsize=(10, 8))

# Plot the first subplot
x_pos = [0,0.75,3,4,6,7]
axes[0, 0].bar(x, y1)
axes[0, 0].set_yscale('log')
axes[0, 0].set_title(metrics[0])
axes[0, 0].set_xlabel('models size/split')
axes[0, 0].set_ylabel('%')
# axes[0, 0].plot(x, y1)

# Plot the second subplot
axes[0, 1].bar(x, y2)
axes[0, 1].set_yscale('log')
axes[0, 1].set_title(metrics[1])
axes[0, 1].set_xlabel('models size/split')
axes[0, 1].set_ylabel('%')

# Plot the third subplot
# Plot the second subplot
axes[1, 0].bar(x, y3)
axes[1, 0].set_yscale('log')
axes[1, 0].set_title(metrics[2])
axes[1, 0].set_xlabel('models size/split')
axes[1, 0].set_ylabel('%')

# Plot the fourth subplot
# Plot the second subplot
axes[1, 1].bar(x, y4)
axes[1, 1].set_yscale('log')
axes[1, 1].set_title(metrics[3])
axes[1, 1].set_xlabel('models size/split')
axes[1, 1].set_ylabel('%')


# Adjust the spacing between subplots
fig.tight_layout()

# Show the figure
plt.show()
