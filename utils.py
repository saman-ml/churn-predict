import pandas as pd

df = pd.read_csv('IT_customer_churn.csv')

InternetService_list = df['InternetService'].unique()
Contract_list = df['Contract'].unique()
PaymentMethod_list = df['PaymentMethod'].unique()
