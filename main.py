"""Takes a csv file, reads it, and creates graphs"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"""Loading and Preprocessing"""

csv = "https://raw.githubusercontent.com/fivethirtyeight/data/master/congress-demographics/data_aging_congress.csv"


def load_and_preprocess(csv):
    """loads the data"""
    general_df = pd.read_csv(csv)
    return general_df


general_df = load_and_preprocess(csv)

"""Summary Statistics"""


def get_summary_stats(general_df, col):
    """function that calls for the summary statistics for the variable age_years"""
    desc_stats = general_df[col].describe()
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


get_summary_stats(general_df, "age_years")

"""Building Visualization"""


def hist_cong_age(general_df, col):
    """builds a histogram for the ages of all Congressmembers"""
    plt.hist(general_df[col], bins=20, edgecolor="black")
    plt.title("Distribution of Ages in Congress", fontsize=16)
    plt.xlabel("Age", fontsize=14)
    plt.ylabel("Frequency", fontsize=14)
    plt.savefig("output/congressional_age.png")


hist_cong_age(general_df, "age_years")
