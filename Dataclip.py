import pandas as pd


file_path = 'C:\\DeepLearning\\Covid Data.csv'
data = pd.read_csv(file_path)
print(data.loc[0, 'AGE'])