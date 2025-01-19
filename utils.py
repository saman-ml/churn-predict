import pandas as pd

df = pd.read_csv('data_preprop.csv')    
Contract_list = df.columns[18:21]
PaymentMethod_list = df.columns[21:25]
InternetService_list = df.columns[25:28]