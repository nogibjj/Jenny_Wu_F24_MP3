"""Takes a csv file, reads it, and creates graphs"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def load_and_preprocess(csv):
    """loads the data"""
    general_df = pd.read_csv(csv)
    return general_df


dataset = "https://raw.githubusercontent.com/fivethirtyeight/data/master/congress-demographics/data_aging_congress.csv"
cg_age_df = pd.read_csv(dataset)
cg_age_df.head()


def get_summary_stats():
    """function that calls for the summary statistics"""
    desc_stats = cg_age_df["age_years"].describe()
    print(
        """The average age of a Congress member from during a particular congress between 
        Jan 1947 and Feb 2014 is """
        + str(round(desc_stats["mean"], 3))
    )
    print(
        """The median age of a Congress member from during a particular congress between 
        Jan 1947 and Feb 2014 is """
        + str(round(desc_stats["50%"], 3))
    )
    print(
        "Standard Deviation between the ages of Congress members is "
        + str(round(desc_stats["std"], 3))
    )

    return desc_stats


get_summary_stats()


def build_chart():
    """builds a histogram out of the target columns"""
    plt.hist(cg_age_df["age_years"], bins=20, edgecolor="black")
    plt.title("Distribution of Ages in Congress", fontsize=16)
    plt.xlabel("Age", fontsize=14)
    plt.ylabel("Frequency", fontsize=14)


build_chart()
