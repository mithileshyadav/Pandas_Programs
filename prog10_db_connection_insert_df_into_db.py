import pandas as pd
import numpy as np
from sqlalchemy import create_engine
from urllib.parse import quote_plus

# Sample DataFrame
emp_data = {
    'name': ['Manu', 'Anjali', 'Sittu', 'Bittu', 'Abhinay', 'Kumar', 'Raju', 'Mithilesh', 'Ritesh', 'Rakesh'],
    'salary': [10000, 10000, 50000, 90000, 30000, 45000, 30000, 55000, 85000, 19000],
    'designation': ['Tester', 'Co-ordinator', 'Developer', 'Python Developer', 'Architecture', 'Manager', 'Sr. Python Developer', 'Sr. Python Developer', 'Manager', 'Sales'],
}


df = pd.DataFrame(emp_data)
print(df)
# Define the PostgreSQL database connection parameters
user = 'postgres'
password = 'pass@123'
host = 'localhost'
port = '5432'
database = 'test_database_mithilesh'

password = quote_plus(password)
# Create the connection string
connection_string1 = 'postgresql://'+user+':'+password+'@'+host+':'+port+'/'+database
# Create the SQLAlchemy engine

# engine = create_engine('postgresql://'+user+':'+password+'@'+host+':'+port+'/'+database)
engine = create_engine(connection_string1)

# Write the DataFrame to a SQL table
table_name = 'tbl_employee'
df.to_sql(table_name, engine, if_exists='replace', index=False)
print(f'DataFrame written to PostgreSQL table {table_name} successfully.')
