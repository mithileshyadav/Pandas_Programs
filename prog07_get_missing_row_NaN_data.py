"""
W.A.P of pandas to select the rows where the score is missing ie, i Nan.
"""

import pandas as pd
import numpy as np

exam_data = {
    "name" : ["Shivangi", "Priya", "Satya", "Devi", "Kumari","Anu","manu", "Tanu", "Shivangi"],
    "score": [100, np.nan, 12,17,np.nan, 56,32,90, np.nan],
    "attempts": [1,67,32,12,9,2,7,5,2],
    "qualify": ["yes", "yes", "yes", "yes", "No", "No", "yes", "No","yes"],
}

df = pd.DataFrame(exam_data)
print(df)


IsNull_value = df['score'].isnull()   # it Stre True where Nan 
print(df[IsNull_value])               # IT PRINT WHERE TRUE CONDITION
  
