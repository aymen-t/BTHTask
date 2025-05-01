# BTHTask
Original Dataset
# Synthetic Dataset Generation and Analysis

This Python script generates a synthetic dataset with three variables:
1. **Category1**: A categorical variable with values ["A", "B", "C", "D", "E"].
2. **Value1**: A continuous variable generated from a normal distribution with a mean of 10 and a standard deviation of 2.
3. **Value2**: A continuous variable generated from a normal distribution with a mean of 20 and a standard deviation of 6.

### Features:
- Generates a **DataFrame** with 500 samples.
- **Category1** follows a specified categorical distribution.
- **Value1** and **Value2** are continuous variables following normal distributions.
- Saves the generated data to a CSV file (`original.csv`).

We are then assuming that we only have the dataset csv file and now want to understand how dataset was generated. 
- Provides **descriptive statistics** for `Value1` and `Value2`.
- Visualizes the distribution of `Category1` (categorical) and the distributions of `Value1` and `Value2` (continuous) using histograms and Kernel Density Estimation (KDE).
- This made us understand how dataset was generated.
- The next task is to generate a similar dataset.

### Requirements:
- **pandas**
- **numpy**
- **seaborn**
- **matplotlib**
- **scipy**

You can install the required dependencies by running:

```bash
pip install pandas numpy seaborn matplotlib scipy
