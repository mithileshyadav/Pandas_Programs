import pandas as pd
import numpy as np
from sqlalchemy import create_engine
from urllib.parse import quote_plus

# Sample DataFrame
exam_data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
number = [100 + i for i in range(len(labels))]
df = pd.DataFrame(exam_data, index=number)
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
table_name = 'tbl_row_dataFrame_data'
df.to_sql(table_name, engine, if_exists='replace', index=False)
print(f'DataFrame written to PostgreSQL table {table_name} successfully.')
