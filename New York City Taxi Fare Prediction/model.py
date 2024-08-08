#%%
import pandas as pd

df = pd.read_csv('train.csv', nrows=10000)

df_2 = df.groupby(['passenger_count'])['fare_amount'].mean()
# df_2.columns = ['passenger_count', 'number_of_obs']
# df_2_sum = df_2['number_of_obs'].sum()
# df_2['prop'] = df_2['number_of_obs'] / df_2_sum
# df_2

df_2