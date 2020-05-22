# Calculate the S2F of altcoins
# How to use:
# python3 s2f.py file.csv
# csv file must have the following columns: date (datetime-like), supply (total supply), reward (daily block reward)

import pandas as pd
import sys
from datetime import datetime

# Check that the user is providing a csv file
def check():
    if len(sys.argv) < 2:
        print("please provide a .csv file")
        return

# Load the csv into a dataframe
def load(csvfile):
    if ".csv" not in csvfile:
        print("not a csv file")
        return
    df = pd.read_csv(csvfile)
    df['date'] = pd.to_datetime(df['date'])
    return df

# Seperate out the different years
def separate_by_year(df, num_years):
    years = []
    curr = datetime.now().year
    for i in range(curr-num_years, curr+1):
        y_df = df[df['date'].dt.year == i]
        years.append(y_df)
    return years

# Calculate the s2f values for each year
def calculate_s2f_yearly(frames, df, correction_factor):
    values = []
    for frame in frames:
       s2f = (frame['supply'].max()-correction_factor) / (frame['reward'].sum())
       values.append((frame['date'].min().year, s2f))
    print(values)
    return values

calculate_s2f_yearly(separate_by_year(load(sys.argv[1]), 4), load(sys.argv[1]), 7.2e7)





