import numpy as np
import pandas as pd
import seaborn as sns
from scipy import stats
import matplotlib.pyplot as plt



if __name__ == "__main__":
    # Generate synthetic dataset
    np.random.seed(42)
    num_samples = 500
    df = pd.DataFrame({
        "Category1": np.random.choice(["A", "B", "C", "D", "E"],
                                      num_samples, p=[0.2, 0.4, 0.2, 0.1, 0.1]),
        "Value1": np.random.normal(10, 2, num_samples),  
        "Value2": np.random.normal(20, 6, num_samples),  
    })
    df.to_csv("original.csv", sep=";")
  
    print("\nCategorical Variable Distribution (Category1):")
    category_counts = df['Category1'].value_counts(normalize=True)  
    print(category_counts)

    plt.figure(figsize=(8, 6))
    sns.countplot(x='Category1', data=df)
    plt.title('Distribution of Alphabets')
    plt.show()  

    print("\nSummary Statistics for Value1 and Value2:") 
    print(df[['Value1', 'Value2']].describe())

# Create a figure and axes for two subplots (side-by-side)
plt.figure(figsize=(14, 6))

#Value1
plt.subplot(1, 2, 1)
sns.histplot(df['Value1'], kde=True, color='blue', bins=30, stat='density')
plt.title('Distribution of Value1')
plt.xlabel('Value1')
plt.ylabel('Density')

#Value2
plt.subplot(1, 2, 2)
sns.histplot(df['Value2'], kde=True, color='green', bins=30, stat='density')
plt.title('Distribution of Value2')
plt.xlabel('Value2')
plt.ylabel('Density')

plt.tight_layout()
plt.show()

