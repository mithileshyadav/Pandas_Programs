"""
W.A pandas Program to select the rows where number
of attempts in the examination is less than 2 and score greater than 15
"""
import pandas as pd
import numpy as np

exam_data = {
    "name" : ["Shivangi", "Priya", "Satya", "Devi", "Kumari","Anu","manu", "Tanu", "Shivangi"],
    "score": [100, np.nan, 12,15,np.nan, 56,12,90, np.nan],
    "attempts": [1,67,32,12,9,2,7,5,2],
    "qualify": ["yes", "yes", "yes", "yes", "No", "No", "yes", "No","yes"],
}

df = pd.DataFrame(exam_data)
print(df)

print("\n\n========================= \n\n")
score_gte_15_and_attempts_gte_2 = (df['score'] >=2) & (df['attempts'] >=15)
print(df[score_gte_15_and_attempts_gte_2])




