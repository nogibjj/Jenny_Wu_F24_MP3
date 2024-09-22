"""Takes a csv file, reads it, and creates graphs"""

import polars as pl
import matplotlib.pyplot as plt


def load_and_preprocess(csv):
    """loads the data"""
    general_df = pl.read_csv(csv)
    return general_df


"""Summary Statistics"""


def get_summary_stats(general_df, col):
    """function that calls for the summary statistics for the variable age_years"""
    desc_stats = general_df[col].describe()
    desc_df = pl.DataFrame(desc_stats)
    return desc_df


"""Building Visualization"""


def hist_cong_age(general_df, col):
    """builds a histogram for the ages of all Congressmembers"""

    plt.hist(general_df[col], bins=20, edgecolor="black")
    plt.title("Distribution of Ages in Congress", fontsize=16)
    plt.xlabel("Age", fontsize=14)
    plt.ylabel("Frequency", fontsize=14)
    plt.savefig("output/congressional_age.png")
    plt.show()


def main():
    """Calling the functions as defined with the specific dataset"""
    csv = "https://raw.githubusercontent.com/fivethirtyeight/data/master/congress-demographics/data_aging_congress.csv"

    general_df = load_and_preprocess(csv)
    s_stats = get_summary_stats(general_df, "age_years")
    hist_cong_age(general_df, "age_years")

    # print(general_df.head())
    print(s_stats)


if __name__ == "__main__":
    main()
