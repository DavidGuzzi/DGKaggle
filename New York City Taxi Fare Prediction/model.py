#%%
import pandas as pd

df = pd.read_csv('train.csv', nrows=10000)

df_2 = df.groupby(['passenger_count'])['fare_amount'].mean()
# df_2.columns = ['passenger_count', 'number_of_obs']
# df_2_sum = df_2['number_of_obs'].sum()
# df_2['prop'] = df_2['number_of_obs'] / df_2_sum
# df_2

df_2

#%%
import pandas as pd

#Read train.csv
# df = pd.read_csv('train.csv').sample(frac=0.03, random_state=7)

#Get a sample, and save it
# sample = df.to_csv(r'C:\Users\HP\OneDrive\Escritorio\David Guzzi\Github\DGKaggle\New York City Taxi Fare Prediction\train_s.csv')

#Read train_s.csv and explore it

df = pd.read_csv('train_s.csv')
df.info()
