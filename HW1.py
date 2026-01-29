import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


#%% 1
np.random.seed(6401)
n = 1000

x = np.random.normal(loc=0, scale=1, size=n)
y = np.random.normal(loc=5, scale=np.sqrt(2), size=n)

print("First 5 observations of x (mean=0, variance=1):", x[:5])
print("\nFirst 5 observations of y (mean=5, variance=2):", y[:5])

#%% 2
def pearson_correlation(x, y):

    x_mean = x.mean()
    y_mean = y.mean()

    x_deviation = x - x_mean
    y_deviation = y - y_mean

    numerator = (x_deviation * y_deviation).sum()

    denominator = np.sqrt((x_deviation ** 2).sum()) * np.sqrt((y_deviation ** 2).sum())
    r = numerator / denominator

    return r

r = pearson_correlation(x, y)
print(f"\nCorrelation coefficient between x and y: r = {r:.6f}")

#%% 3
sample_mean_x = x.mean()
sample_mean_y = y.mean()

sample_variance_x = ((x - sample_mean_x) ** 2).sum() / (n - 1)
sample_variance_y = ((y - sample_mean_y) ** 2).sum() / (n - 1)

print(f"\na. The sample mean of random variable x is: {sample_mean_x:.6f}")
print(f"b. The sample mean of random variable y is: {sample_mean_y:.6f}")
print(f"c. The sample variance of random variable x is: {sample_variance_x:.6f}")
print(f"d. The sample variance of random variable y is: {sample_variance_y:.6f}")

#%% 4
plt.figure(figsize=(12, 6))

sample_index = np.arange(1, n + 1)

plt.plot(sample_index, x, label='x', color='blue', linewidth=0.8)
plt.plot(sample_index, y, label='y', color='red', linewidth=0.8)

plt.title('Line Plot of Random Variables X and Y', fontsize=14, fontweight='bold')

plt.xlabel('Sample Index', fontsize=12)
plt.ylabel('Value', fontsize=12)
plt.grid(True)
plt.legend(loc='upper right', fontsize=10)
plt.tight_layout()
plt.show()

#%% 5
plt.figure(figsize=(12, 6))
num_bins = 100

plt.hist(x, bins=num_bins, label='x', color='blue', alpha=0.7)
plt.hist(y, bins=num_bins, label='y', color='red', alpha=0.7)

plt.title('Histogram of Random Variables X and Y', fontsize=14, fontweight='bold')

plt.xlabel('Value', fontsize=12)
plt.ylabel('Frequency', fontsize=12)

plt.grid(True, linestyle='--', alpha=0.7)

plt.legend(loc='upper right', fontsize=10)

plt.tight_layout()

plt.show()

#%% 6
url = "https://raw.githubusercontent.com/rjafari979/Information-Visualization-Data-Analytics-Dataset-/main/tute1.csv"
df = pd.read_csv(url)

print("\nLast 5 observations of tute1.csv dataset:")
print(df.tail().to_string(index=True))

#%% 7
Sales = df['Sales']
AdBudget = df['AdBudget']
GDP = df['GDP']

corr_sales_adbudget = pearson_correlation(Sales, AdBudget)
corr_sales_gdp = pearson_correlation(Sales, GDP)
corr_adbudget_gdp = pearson_correlation(AdBudget, GDP)

print(f"\na. The sample Pearson's correlation coefficient between Sales & AdBudget is: {corr_sales_adbudget:.2f}")
print(f"b. The sample Pearson's correlation coefficient between Sales & GDP is: {corr_sales_gdp:.2f}")
print(f"c. The sample Pearson's correlation coefficient between AdBudget & GDP is: {corr_adbudget_gdp:.2f}")

#%% 8

plt.figure(figsize=(10, 6))
plt.scatter(AdBudget, Sales, alpha=0.7)
plt.xlabel('AdBudget')
plt.ylabel('Sales')
plt.title(f'Scatter Plot: Sales vs AdBudget')
plt.grid(True)
plt.tight_layout()
plt.show()

#%% 9

plt.figure(figsize=(10, 6))
plt.scatter(GDP, Sales, alpha=0.7, color='green')
plt.xlabel('GDP')
plt.ylabel('Sales')
plt.title(f'Scatter Plot: Sales vs GDP')
plt.grid(True)
plt.tight_layout()
plt.show()

#%% 10
plt.figure(figsize=(10, 6))
plt.scatter(AdBudget, GDP, alpha=0.7, color='red')
plt.xlabel('AdBudget')
plt.ylabel('GDP')
plt.title(f'Scatter Plot: GDP vs AdBudget')
plt.grid(True)
plt.tight_layout()
plt.show()

#%% 11
plt.figure(figsize=(12, 7))
time = df.index

plt.plot(time, Sales, label='Sales', marker='o', markersize=3)
plt.plot(time, AdBudget, label='AdBudget', marker='s', markersize=3)
plt.plot(time, GDP, label='GDP', marker='^', markersize=3)

plt.xlabel('Time')
plt.ylabel('Value')
plt.title('Line Plot of Sales, AdBudget, and GDP over Time')
plt.legend(loc='best')
plt.grid(True)
plt.tight_layout()
plt.show()

#%% 12
plt.figure(figsize=(12, 7))

plt.hist(Sales, bins=20, alpha=0.6, label='Sales', edgecolor='black')
plt.hist(AdBudget, bins=20, alpha=0.6, label='AdBudget', edgecolor='black')
plt.hist(GDP, bins=20, alpha=0.6, label='GDP', edgecolor='black')

plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram of Sales, AdBudget, and GDP')
plt.legend(loc='best')
plt.grid(True)
plt.tight_layout()
plt.show()