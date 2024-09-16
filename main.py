"""Takes a csv file, reads it, and creates graphs"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = "https://raw.githubusercontent.com/fivethirtyeight/data/master/congress-demographics/data_aging_congress.csv"
cg_age_df = pd.read_csv(dataset)
cg_age_df.head()


def get_summary_stats(dataset, col_of_intrst):
    desc_stats = dataset[col_of_intrst].describe()
    print(
        "The average age of a Congress member from during a particular congress between Jan 1947 and Feb 2014 is "
        + str(round(desc_stats["mean"], 3))
    )
    print(
        "The median age of a Congress member from during a particular congress between Jan 1947 and Feb 2014 is "
        + str(round(desc_stats["50%"], 3))
    )
    print(
        "Standard Deviation between the ages of Congress members is "
        + str(round(desc_stats["std"], 3))
    )

    return desc_stats


def sum_desc():
    """function that sets a new df variable equal to the summary stats"""
    cg_age_stats = cg_age_df.describe()
    print(cg_age_df)


sum_desc()


def build_chart():
    """builds a histogram out of the target columns"""
    plt.hist(cg_age_df["age_years"], bins=20, edgecolor="black")
    plt.title("Distribution of Ages in Congress", fontsize=16)
    plt.xlabel("Age", fontsize=14)
    plt.ylabel("Frequency", fontsize=14)


build_chart()
