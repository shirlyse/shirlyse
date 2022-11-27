import pandas as pd
# dataframe Name and Age columns
#df = pd.DataFrame({'Name': ['A', 'B', 'C', 'D'],
 #                  'Age': [10, 0, 30, 50]})
df = pd.DataFrame({})
df['flight'] = ''
#df.assign(flight='')
df['flight2'] = ''
print(df)

# Convert the dataframe to an XlsxWriter Excel object.
#df.to_excel(writer, sheet_name='Sheet1', index=False)
#writer.close()
#reader = pd.read_excel(r'demo.xlsx')
#print(reader)