import numpy as np
import pandas as pd
from scipy import stats
from scipy.stats import pearsonr
import matplotlib.pyplot as plt


if __name__ == "__main__":
        # Generate synthetic dataset
    np.random.seed(42)
    num_samples = 500
    originaldata = pd.DataFrame({
        "Category1": np.random.choice(["A", "B", "C", "D", "E"],
                                    num_samples, p=[0.2, 0.4, 0.2, 0.1, 0.1]),
        "Value1": np.random.normal(10, 2, num_samples),    
        "Value2": np.random.normal(20, 6, num_samples),  
    })
    originaldata.to_csv("originaldataset1.csv", sep=";")

    # Generate a similar dataset
    np.random.seed(42)
    num_samples = 500
    Aymendata = pd.DataFrame({
        "Category1": np.random.choice(["A", "B", "C", "D", "E"],
                                      num_samples, p=[0.4, 0.2, 0.1, 0.2, 0.1]),
        "Value1": np.random.normal(10, 2, num_samples),  
        "Value2": np.random.normal(20, 6, num_samples),  
    })
    Aymendata.to_csv("Aymendataset.csv", sep=";")


    x = Aymendata
    y = originaldata

    print("\nChi-square test for Category1:")
    aymenobserved = x[["Value1", "Value2"]]
    originalexpected = y[["Value1", "Value2"]]
    # chi2_stat, p_value_cat = chisquare(f_obs=observed, f_exp=expected)

    correlation_coefficient, p_value = pearsonr(aymenobserved, originalexpected)
    print(f"Corr coeff: {correlation_coefficient}, p-value: {p_value}")

    fig, ax = plt.subplots(2, 2, figsize=(10, 8))  # optional: set a better figure size

    # Top-left: Observed scatter
    ax[0, 0].scatter(aymenobserved["Value1"], aymenobserved["Value2"], label="Aymen Data")
    ax[0, 0].set_title("Aymen Data: Value1 vs Value2")
    ax[0, 0].set_xlabel("Value1")
    ax[0, 0].set_ylabel("Value2")
    ax[0, 0].legend()

    # Top-right: Expected scatter
    ax[0, 1].scatter(originalexpected["Value1"], originalexpected["Value2"], label="Original Data", color='orange')
    ax[0, 1].set_title("Original Data: Value1 vs Value2")
    ax[0, 1].set_xlabel("Value1")
    ax[0, 1].set_ylabel("Value2")
    ax[0, 1].legend()

    # Bottom-left: Observed full line plot
    ax[1, 0].plot(aymenobserved, label="Aymen Observed")
    ax[1, 0].set_title("Aymen Data Overview")
    ax[1, 0].legend()

    # Bottom-right: Expected full line plot
    ax[1, 1].plot(originalexpected, label="Original Data")
    ax[1, 1].set_title("Original Data Overview")
    ax[1, 1].legend()

    plt.tight_layout()
    plt.show()
