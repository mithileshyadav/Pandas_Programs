"""
Write a Program  to get attempts is greate than 2 and Score Column is less than 56

"""
import pandas as pd

exam_data = {
    "name" : ["Shivangi", "Priya", "Satya", "Devi", "Kumari","Anu","manu", "Tanu", "Shivangi"],
    "socre": [100, 20, 12,17,40, 56,32,90, 91],
    "attempts": [1,67,32,12,9,2,7,5,2],
    "qualify": ["yes", "yes", "yes", "yes", "No", "No", "yes", "No","yes"],
}

df = pd.DataFrame(exam_data)
print(df)

gt_2 = df['attempts'] >2 
print("\n\n============= GET THE ATTEMPTS WHICH IS GREATE THAN 2 ===========\n\n")
print(df[gt_2])

print("\n\n============= GET THE SCORE IS LESS THAN 56 ===========\n\n")
lt_56 = df['socre'] < 56
print(df[lt_56])

print("\n\n============= GET THE NAME IS EQUAL TO Shivangi ===========\n\n")
name_eq = df['name'] == 'Shivangi'
print(df[name_eq])

print("\n\n============= GET THE NAME LEN <=4  ===========\n\n")
name_len_lte_4 = df['name'].str.len() <= 4
print(df[name_len_lte_4]) 
