import pandas as pd

df = pd.read_csv('data_preprop.csv')

Contract_list = df.columns[17:20]
PaymentMethod_list = df.columns[20:24]
InternetService_list = df.columns[24:]