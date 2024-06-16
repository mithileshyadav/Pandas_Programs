"""
W.A pandas program to select the rows the socre is between 15, 90.
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
# print(df)
# breakpoint()
between_15to90 = df['score'].between(15,90)  # TRUE IF SCORE BETWEEN 15, 90
print(df[between_15to90])                    # print where True value 




