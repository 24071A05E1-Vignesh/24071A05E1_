#Read a CSV file using pandas and display the first 5 rows.
import pandas as pd
df = pd.read_csv('people_data.csv')
print(df.head())
