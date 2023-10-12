import pandas as pd


# Reading all the files from the data folder
df_0 = pd.read_csv("data/daily_sales_data_0.csv")
df_1 = pd.read_csv("data/daily_sales_data_1.csv")
df_2 = pd.read_csv("data/daily_sales_data_2.csv")

# Combining all the dataframes into single file
df = pd.concat([df_0,df_1,df_2],axis=0)

# Checking the shape of the dataset
print(df.shape)
# Keeping only product that is under study i.e. pink morsel
df = df[df['product']=='pink morsel']

# Checking the shape of the dataset
print(df.shape)

# Replace # from price
df['price'] = df['price'].apply(lambda x:x[1:])
df['price'] = df['price'].astype('float')

df['Sales'] = df['quantity'] * df['price']
# Keeping only columns for study
df = df[['Sales','date','region']]


print(df.head())