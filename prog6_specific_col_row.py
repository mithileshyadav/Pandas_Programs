"""
W.A.P  to select specified columns and rows from a given dataFrame.
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
print('\n==========================\n')
print(df.iloc[1:3, 1:3])
print('\n==========================\n')
print(df.iloc[[1,4,5], [1,3]])

# =================== iloc ======================
"""
iloc Syntax:
df.iloc[row_start:row_end, column_start: column_end]

iloc Syntax for Random Row and Random column:
df.iloc[[row1, row3, row5], [column1, column4]]
example:
df.iloc[[1,2,3,4,5], [1,3]]

"""