"""
Test goes here

"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from main import load_and_preprocess, get_summary_stats


example_csv = "https://raw.githubusercontent.com/fivethirtyeight/data/master/congress-age/congress-terms.csv"


def test_load_and_preprocess():
    """test that loading the csv will work"""
    general_df = load_and_preprocess(example_csv)
    assert general_df is not None
    assert general_df.shape == (29120, 13)


def test_get_summary_stats():
    test_desc_stats = get_summary_stats(pd.read_csv(example_csv), "age_years")
    assert desc_stats["mean"] == 44.043258
    assert desc_stats["min"] == 38.620123
    assert desc_stats["std"] == 5.860264


test_get_summary_stats()

if __name__ == "__main__":
    test_load_and_preprocess()
    get_summary_stats()
