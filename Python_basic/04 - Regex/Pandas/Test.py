




import pandas as pd



# data = pd.read_excel("C:\Users\VAS-PC-IDE\Desktop\Приход и Траты.xlsx")


data_inf = pd.read_csv("power.csv")
data_inf.to_csv("data_inf.csv")
data_inf = pd.read_csv("power.csv").head(100)
data_inf.to_excel("data_inf.xls")
# print(data_inf.head())
# print(data_inf.tail())
# print(data_inf.head(20))
