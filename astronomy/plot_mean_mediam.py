import numpy as np
import matplotlib.pyplot as plt

# Generate sample data with some outliers
np.random.seed(42)  # For reproducibility
data = np.concatenate([
    np.random.normal(100, 10, 50),  # Normal distribution around 100
    np.random.normal(200, 5, 5)      # Few outliers around 200
])

# Calculate mean and median
mean_value = np.mean(data)
median_value = np.median(data)

# Create the plot
plt.figure(figsize=(12, 6))

# Plot histogram of the data
plt.hist(data, bins=20, alpha=0.6, color='skyblue', label='Data Distribution')

# Add vertical lines for mean and median
plt.axvline(mean_value, color='red', linestyle='dashed', linewidth=2, label=f'Mean: {mean_value:.2f}')
plt.axvline(median_value, color='green', linestyle='dashed', linewidth=2, label=f'Median: {median_value:.2f}')

# Customize the plot
plt.title('Distribution with Mean and Median Comparison', fontsize=14)
plt.xlabel('Values', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.legend(fontsize=10)
plt.grid(True, alpha=0.3)

# Show the plot
plt.tight_layout()
plt.show()

# Print the values
print(f"Mean: {mean_value:.2f}")
print(f"Median: {median_value:.2f}")
