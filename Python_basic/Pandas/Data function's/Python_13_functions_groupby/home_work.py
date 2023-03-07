# Домашнее задание к лекции "Функции и работа с данными"
# Преподаватель: Константин Башевой
# Домашнее задание
#
# Задание 1
import pandas as pd
import pathlib
wokr_path = pathlib.Path.cwd()

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)
pd.options.display.expand_frame_repr = False
# Напишите функцию, которая классифицирует фильмы из материалов занятия по следующим правилам:
# - оценка 2 и меньше - низкий рейтинг
# - оценка 4 и меньше - средний рейтинг
# - оценка 4.5 и 5 - высокий рейтинг
# df_1 = pd.read_csv("C:\\Users\\VAS-PC-IDE\\Documents\\CODE\\Python\\Netology\\Python_basic\\Pandas\\Data function's\\ml-latest-small\\movies.csv")
# df_2 = pd.read_csv("C:\\Users\\VAS-PC-IDE\\Documents\\CODE\\Python\\Netology\\Python_basic\\Pandas\\Data function's\\ml-latest-small\\ratings.csv")
# df_3 = pd.read_csv("C:\\Users\\VAS-PC-IDE\\Documents\\CODE\\Python\\Netology\\Python_basic\\Pandas\\Data function's\\ml-latest-small\\links.csv")
# df_4 = pd.read_csv("C:\\Users\\VAS-PC-IDE\\Documents\\CODE\\Python\\Netology\\Python_basic\\Pandas\\Data function's\\ml-latest-small\\tags.csv")
# # print(f'{df_1}\n{df_2}\n{df_3}\n{df_4}')
# # print(f'{len(df_1)}\n{len(df_2)}\n{len(df_3)}\n{len(df_4)}')
# # def classify(row):
# #     if row.rating in not type(float)
# df_23 = pd.merge(df_2, df_3, how="left")
# df = pd.merge(df_1, df_23, how="left")
# # print(df.head(10), len(df))
# df_upd = df[['title', 'movieId', 'userId', 'rating']]
# # print(df_upd.head(15), len(df_upd))
# df_add = df_upd.groupby('title').agg({'rating': 'mean'})
# print(df_add.head(15), len(df_add))
# def classification(row):
#     if row.rating <= 2:
#         return f"Low rating"
#     elif row.rating <= 4.4:
#         return f"Middle rating"
#     elif row.rating <= 5:
#         return f"Big rating"
#     else:
#         return f"Need additional analiz"
# df_add['calssif'] = df_add.apply(classification, axis=1)
# print(df_add.sort_values('rating', ascending=False).head(350), len(df_add))
# Результат классификации запишите в столбец class
# Задание 2
#
# Используем файл keywords.csv.
#
# Необходимо написать гео-классификатор, который каждой строке сможет выставить географическую принадлежность
# определенному региону. Т. е. если поисковый запрос содержит название города региона, то в столбце ‘region’ пишется
# название этого региона. Если поисковый запрос не содержит названия города, то ставим ‘undefined’.
#
# Правила распределения по регионам Центр, Северо-Запад и Дальний Восток:
#
# geo_data = {
# df = pd.read_csv('keywords.csv')
#
#
# def detect(row):
#     if "москва" in row.keyword or "тула" in row.keyword or "ярославль" in row.keyword:
#         return f"Центр"
#     elif 'петербург' in row.keyword or 'псков' in row.keyword or 'мурманск' in row.keyword:
#         return f"Северо-Запад"
#     elif 'владивосток' in row.keyword or 'сахалин' in row.keyword or 'хабаровск' in row.keyword:
#         return f"Дальний-Восток"
#     elif 'краснодар' in row.keyword or 'сочи' in row.keyword or 'астрахань' in row.keyword:
#         return f"Юг"
#     else:
#         return f"undefined"
# df['region'] = df.apply(detect, axis=1)
# print(df, len(df))
# 'Центр': ['москва', 'тула', 'ярославль'],
#
# 'Северо-Запад': ['петербург', 'псков', 'мурманск'],
#
# 'Дальний Восток': ['владивосток', 'сахалин', 'хабаровск']
# }
#
# Результат классификации запишите в отдельный столбец region.
#
# Задание 3 (бонусное)
# df = pd.read_html("https://grouplens.org/datasets/movielens")
# print(df) нет дата фрейма
df_1 = pd.read_csv("C:\\Users\\VAS-PC-IDE\\Documents\\CODE\\Python\\Netology\\Python_basic\\Pandas\\Data function's\\ml-latest-small\\movies.csv")
df_2 = pd.read_csv("C:\\Users\\VAS-PC-IDE\\Documents\\CODE\\Python\\Netology\\Python_basic\\Pandas\\Data function's\\ml-latest-small\\ratings.csv")
df = pd.merge(df_1, df_2, how="left")
# def detect(row):
#     date = range(1950, 2011)
#      if date in row.tiitle:
#          return date
# print(df.head(25))

# Есть мнение, что “раньше снимали настоящее кино, не то что сейчас”. Ваша задача проверить это утверждение, используя
# файлы с рейтингами фильмов из прошлого домашнего занятия (файл ratings.csv из базы
# https://grouplens.org/datasets/movielens). Т. е. проверить верно ли, что с ростом года выпуска фильма его средний
# рейтинг становится ниже.
#
# При этом мы не будем затрагивать субьективные факторы выставления этих рейтингов, а пройдемся по следующему алгоритму:
#
# В переменную years запишите список из всех годов с 1950 по 2010.
#
# Напишите функцию production_year, которая каждой строке из названия фильма выставляет год выпуска. Не все названия
# фильмов содержат год выпуска в одинаковом формате, поэтому используйте следующий алгоритм:
#
# для каждой строки пройдите по всем годам списка years
# если номер года присутствует в названии фильма, то функция возвращает этот год как год выпуска
# если ни один из номеров года списка years не встретился в названии фильма, то возвращается 1900 год
# Запишите год выпуска фильма по алгоритму пункта 2 в новый столбец ‘year’
#
# Посчитайте средний рейтинг всех фильмов для каждого значения столбца ‘year’ и отсортируйте результат по убыванию рейтинга