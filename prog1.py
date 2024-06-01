"""
W.A.P to crate a dataFrame from a dictionary and display it. using only dictionary
Ex. {'Name': ["Satya", "Yadav"," Kuamr", ""], "RollNo": [1,2, None, None]}

"""
import pandas as pd
import numpy as np

d = {'Name': ["Satya", "Yadav"," Kuamr", ""], "RollNo": [1,2, None, None]}

df = pd.DataFrame(d)
print(df)







