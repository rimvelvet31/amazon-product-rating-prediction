import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def find_outliers(df, col):
    # Calculate first and third quartiles (25th and 75th percentiles)
    q1 = df[col].quantile(0.25)
    q3 = df[col].quantile(0.75)

    # Calculate IQR
    iqr = q3 - q1

    # Calculate lower and upper bounds
    upper = q3 + (1.5 * iqr)
    lower = q1 - (1.5 * iqr)

    # Log results
    print("Column:", col)
    print("Lower bound:", lower)
    print("Upper bound:", upper)

    # Identify outliers, which are the values outside the bounds
    return df[(df[col] < lower) | (df[col] > upper)]


def plot_univariate(df, col, type):
    if type == "num":
        fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(18, 6))

        fig.suptitle(f"Univariate Analysis of {col}")

        # Left plot
        sns.histplot(data=df, x=col, bins=10, ax=ax[0])
        ax[0].set_title(f"Histogram of {col}")

        # Right plot
        sns.boxplot(data=df, x=col, ax=ax[1])
        ax[1].set_title(f"Boxplot of {col}")

        plt.tight_layout()
        plt.show()
   
    elif type == "cat":
        # Sort categories by frequency (highest to lowest)
        order = df[col].value_counts().index

        # Countplots are ideal for visualizing the distribution of categorical variables
        sns.countplot(data=df, x=col, order=order)
        
        plt.title(f"Countplot of {col}")
        plt.xticks(rotation=90)
        plt.show()

    else:
        raise ValueError("Invalid args passed. Check if df and col names are correct, or if the type is valid ('num', 'cat').")
