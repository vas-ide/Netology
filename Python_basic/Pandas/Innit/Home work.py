# Домашнее задание к лекции "Библиотека Pandas"
# Преподаватель: Константин Башевой
# Домашнее задание
import pandas as pd
# Задание 1
# Скачайте с сайта https://grouplens.org/datasets/movielens/ датасет любого размера. Определите какому фильму было выставлено больше всего оценок 5.0.
#
# data_films = pd.read_html("https://grouplens.org/datasets/movielens/")
# Задание 2
# По данным файла power.csv посчитайте суммарное потребление стран Прибалтики (Латвия, Литва и Эстония) категорий 4, 12 и 21 за период с 2005 по 2010 года. Не учитывайте в расчетах отрицательные значения quantity.
data_country = pd.read_csv("power.csv")
# data_country_inf = data_country[ data_country['country'].str.contains('Es', case=False) ]['country'].unique()
filtered_data_country = data_country[(data_country['country'] == 'Lithuania') | (data_country['country'] == 'Latvia') | (data_country['country'] == 'Estonia')]
filtered_data_country_year = filtered_data_country[(filtered_data_country['year'] >= 2005)]
filtered_data_country_year_add = filtered_data_country_year[(filtered_data_country_year['year'] <= 2010)]
filtered_data_country_year_category = filtered_data_country_year_add[(filtered_data_country_year_add['category'] == 4) | (filtered_data_country_year_add['category'] == 12) | (filtered_data_country_year_add['category'] == 21)]
filtered_data_upd = filtered_data_country_year_category[(filtered_data_country_year_category["quantity"] > 0)]
print(filtered_data_upd["quantity"].sum())
print(len((filtered_data_upd)))
print(data_country['quantity'].sum())


#     with open("test.txt", "a", encoding="utf8") as code:
#         code.write(f"{filtered_data_country_year_category['quantity']}\n")


# Задание 3
# Выберите страницу любого сайта с табличными данными. Импортируйте таблицы в pandas dataframe.
# Примеры страниц (необязательно брать именно эти):
# https://fortrader.org/quotes
# https://www.finanz.ru/valyuty/v-realnom-vremeni



# df = pd.read_html("https://fortrader.org/quotes")
# print(df)
# df = pd.read_html("https://www.finanz.ru/valyuty/v-realnom-vremeni")
# print(df)