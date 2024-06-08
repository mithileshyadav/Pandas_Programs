"""
Count Number  of Rows and Columns From a DataFrame
"""


import numpy as np
import pandas as pd

exam_data = {
    'name':['Satya','Kumari', 'pihu'],
    'age': [12,34,21],
}

df = pd.DataFrame(exam_data)
print("Number of Row: ", len(df))
print("Number of Columns: ", len(df.columns))
