import lib 

def main():
    """Calling the functions as defined with the specific dataset"""
    csv = "https://raw.githubusercontent.com/fivethirtyeight/data/master/congress-demographics/data_aging_congress.csv"

    general_df = lib.load_and_preprocess(csv)
    s_stats = lib.get_summary_stats(general_df, "age_years")
    lib.hist_cong_age(general_df, "age_years")

    # print(general_df.head())
    print(s_stats)


if __name__ == "__main__":
    main()
