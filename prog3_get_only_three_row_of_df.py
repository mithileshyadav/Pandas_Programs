import pandas as pd

exam_data = {
    "name" : ["Shivangi", "Priya", "Satya", "Devi", "Kumari","Anu","manu", "Tanu"],
    "socre": [100, 20, 12,17,40, 56,32,90],
    "attempts": [1,67,32,12,9,2,7,5],
    "qualify": ["yes", "yes", "yes", "yes", "No", "No", "yes", "No"],
}

df = pd.DataFrame(exam_data)
print(df)

# WE HAVE 3 WAY TO GET 3 ROW
# 1. head(3)  => get 3 row on the top. By default head() get 5 rows() from top
# 2. tail(4)  => get 4 row on the bottom. By default tail get 5 rows() from bottom
# 3. iloc[:3] => IntegerLocation From start to 3 get the row
# Syntax of iloc:
# =================
#  iloc[row, column]
#  ex. iloc[1:3, 0:3]   # MEANS  1 to 3 get rows, and 0 to 3 get column

print(df.head(3))
print(df.tail(2))

# In Between 3 to 6 rows so we go for iloc
print(df.iloc[3:6])




