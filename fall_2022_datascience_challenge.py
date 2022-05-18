"""
Note: Code was originally written in an Jupyter Notebook. 
Hence, the somewhat disjointed nature.
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Read dataset from given .csv file and create a box plot using the order amount
df = pd.read_csv('dataset.csv')
df.plot(y='order_amount', kind='box', title='Order Amount Outliers')

# Inter-qartile range, upper bound, and lower bound calculation
q3, q1 = np.percentile(df.order_amount, [75,25])

iqr = q3-q1

upper_bound = q3 + 1.5*iqr
lower_bound = q1 - 1.5*iqr

# Modal shoe price and removal of junk values
df['shoe_price'] = df['order_amount']/df['total_items']

i = 1
while i <= 100:
    shops = df[df['shop_id'] == i]
    mode = int(shops['shoe_price'].mode())
    drop_rows = df[(df['shop_id'] == i) & (df['shoe_price'] != mode)].index
    i+=1

df.drop(drop_rows, inplace=True)

# Average order valued of non-outlier dataset
aov_df = df[(df['order_amount'] >= lower_bound) & (df['order_amount'] <= upper_bound)]
aov = np.average(aov_df['order_amount'])