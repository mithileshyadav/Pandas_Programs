"""
W.A.P  to select the 'Name' and 'Score' columns from the Dataframe.

"""

import pandas as pd
import numpy as np

# Sample DataFrame
exam_data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
}

df = pd.DataFrame(exam_data)
print(df)
print(df['name'])
print(df['score'])
print(df[['name','score']])
