# input file - first_hundred_numbers.tsv 
""":r! cat first_hundred_numbers.tsv | head -n 10 """
75
85
44
63
27
83
90
67
77
69

import sys
import pandas as pd

def group_in_quantiles(data, num_quantiles):
    # Create a DataFrame from the input data
    df = pd.DataFrame(data, columns=['value'])
    
    # Use qcut to divide data into the specified number of quantiles
    df['quantile_label'], bins = pd.qcut(df['value'], q=num_quantiles, labels=[f'q{i+1}' for i in range(num_quantiles)], retbins=True)
    
    # Add the quantile interval as a new column
    df['quantile_interval'] = pd.cut(df['value'], bins=bins, include_lowest=True)
    
    # Print each row in the specified format
    for _, row in df.iterrows():
        print(f"{row['value']}\t{row['quantile_label']}\t{row['quantile_label']} {row['quantile_interval']}")

if __name__ == "__main__":
    # Read the number of quantiles from the command line
    num_quantiles = int(sys.argv[1])

    # Read input from stdin and convert it to a list of integers
    data = [int(line.strip()) for line in sys.stdin]

    # Call the function to group data into quantiles
    group_in_quantiles(data, num_quantiles)

""" Final Command - 
cat data/first_hundred_numbers.tsv | python group_in_quantiles.py 4 > numbers_quantiles.tsv
"""
