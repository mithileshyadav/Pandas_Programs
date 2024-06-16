"""
Write a Panda program to calculate the sum of the examination attempts by the student.
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
# breakpoint()
sum_of_Score_column = df['score'].sum()
print("Sum of Score Columns: ",sum_of_Score_column)
sum_of_attempts = df['attempts'].sum()
print("Sum of Attempts Columns: ",sum_of_attempts)
