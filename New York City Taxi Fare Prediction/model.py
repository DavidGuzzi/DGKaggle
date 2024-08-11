import pandas as pd

#Read train.csv
df = pd.read_csv('train.csv').sample(frac=0.03, random_state=7)

#Get a sample, and save it
sample = df.to_csv(r'C:\Users\HP\OneDrive\Escritorio\David Guzzi\Github\DGKaggle\New York City Taxi Fare Prediction\train_s.csv')