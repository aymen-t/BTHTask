# BTHTask for the Ph.D. Position in GenAI

### Task Details:
We were provided with a Python script that generates a synthetic dataset with three variables:
1. Category1: A categorical variable with values ["A", "B", "C", "D", "E"].
2. Value1: A continuous variable generated from a normal distribution with a mean of 10 and a standard deviation of 2.
3. Value2: A continuous variable generated from a normal distribution with a mean of 20 and a standard deviation of 6.
### Features:
- Generates a **DataFrame** with 500 samples.
- Category1 follows a specified categorical distribution.
- Value1 and Value2 are continuous variables following normal distributions.
- Saves the generated data to a CSV file (`dataset.csv`).

### Assumption and Reasoning:
We are assuming that the original data generation code was not available in a real-world scenario, I approached the problem by reverse-engineering the characteristics of the dataset through exploratory data analysis (EDA).
- The code file titled "Original Dataset.py" contains the generation and statistical analysis of the dataset.
- After performing analysis, we got frequencies of the categories found in "Distribution of Categories.png".
- I used the following to inspect central tendencies and variability: "df[['Value1', 'Value2']].describe()", This gave me mean and standard deviation values, it also provided evidence of normal distribution. To confirm the distribution type, I plotted histograms with KDE curves. Below is the output:
-              Value1      Value2
      count  500.000000  500.000000
      mean    10.015240   20.436278
      std      2.014124    5.972594

- These were approximate values (mean and standard deviation), I did not reuse them but kept them in mind to create similar but altered distributions. 

### Generate Similar Dataset:
- The next task is to generate a similar dataset. I created a new dataset with:
- A different but realistic probability distribution for Category1: [0.4, 0.2, 0.1, 0.2, 0.1]
- The same sample size (500 rows) for comparability.
- I compared the original and synthetic datasets using both statistical metrics  i.e Pearson correlatio and visual plots.
- For Visualization, I used, Scatter plots for Value1 vs Value2 from both datasets and Line plots to inspect the overall pattern across rows
- The mean and standard deviation my generated data are given below
-              Value1      Value2
      count  500.000000  500.000000
      mean    11.022860   19.363565
      std      3.021186    4.977162
  - "Comparing Datasets.png" shows the distributions of both datasets and also provide a visual comparison between both. 

### Requirements:
- **pandas**
- **numpy**
- **seaborn**
- **matplotlib**
- **scipy**

You can install the required dependencies by running:

```bash
pip install pandas numpy seaborn matplotlib scipy
