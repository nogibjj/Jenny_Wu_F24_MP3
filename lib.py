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
    pl.Config(
        tbl_formatting="ASCII_MARKDOWN",
        tbl_hide_column_data_types=True,
        tbl_hide_dataframe_shape=True,
    )
    string_df = str(desc_df)

    summary_report = "This report displays the outputs from the main.py file, which include a table of generated summary statistics"

    with open("summary_stats.md", "w") as f:
        f.write("## Summary Statistics Report: \n")
        f.write(summary_report)
        f.write("#### Table of Summary Statistics \n")
        f.write(string_df)
        f.write("\n \n")
        f.write("![Congressional Age](outputs/congressional_age.png)\n")
    return desc_stats


"""Building Visualization"""


def hist_cong_age(general_df, col):
    """builds a histogram for the ages of all Congressmembers"""

    plt.hist(general_df[col], bins=20, edgecolor="black")
    plt.title("Distribution of Ages in Congress", fontsize=16)
    plt.xlabel("Age", fontsize=14)
    plt.ylabel("Frequency", fontsize=14)
    plt.savefig("output/congressional_age.png")
