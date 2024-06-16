import pandas as pd

exam_data = {
    "name" : ["Shivangi", "Priya", "Satya", "Devi", "Kumari","Anu","manu", "Tanu"],
    "socre": [100, 20, 12,17,40, 56,32,90],
    "attempts": [1,67,32,12,9,2,7,5],
    "qualify": ["yes", "yes", "yes", "yes", "No", "No", "yes", "No"],
}

df = pd.DataFrame(exam_data)
print(df)
# breakpoint()

# Syntax: df.iloc[row, column]

print(df.iloc[0:3, 0:4])




