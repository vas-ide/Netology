



# Задание 1
# Напишите функцию date_range, которая возвращает список дней между датами start_date и end_date. Даты должны вводиться в формате YYYY-MM-DD.

from datetime import datetime, timedelta

# def date_rage(start_date, end_date):
#     start_date_dt = datetime.strptime(start_date, '%Y-%m-%d')
#     end_date_dt = datetime.strptime(end_date, '%Y-%m-%d')
#     current_date = start_date_dt
#     lst_days = []
#     while current_date.strftime('%Y-%m-%d') <= end_date_dt.strftime('%Y-%m-%d'):
#         lst_days.append(current_date.strftime('%Y-%m-%d'))
#         current_date += timedelta(days=1)
#     print(lst_days)
#     return lst_days
# date_rage("2023-02-03", "2023-02-19")
# Задание 2
# Дополните функцию из первого задания проверкой на корректность дат. В случае неверного формата или если start_date > end_date должен возвращаться пустой список.


def date_rage(start_date, end_date):
    lst_days = []
    try:
        start_date_dt = datetime.strptime(start_date, '%Y-%m-%d')
        end_date_dt = datetime.strptime(end_date, '%Y-%m-%d')
        current_date = start_date_dt
    except:
        print(f"{lst_days}")
        return lst_days
    if current_date.strftime('%Y-%m-%d') > end_date_dt.strftime('%Y-%m-%d'):
        print(lst_days)
        return lst_days
    while current_date.strftime('%Y-%m-%d') <= end_date_dt.strftime('%Y-%m-%d'):
        lst_days.append(current_date.strftime('%Y-%m-%d'))
        current_date += timedelta(days=1)
    print(lst_days)
    return lst_days
date_rage("2023-02-03", "2023-02-19")
date_rage("2023-03-03", "2023-02-19")
date_rage("2023-02-03T23:10", "2023-02-19")



# Задание 3
# Дан поток дат в формате YYYY-MM-DD, в которых встречаются некорректные значения:
# stream = [‘2018-04-02’, ‘2018-02-29’, ‘2018-19-02’]
# Напишите функцию, которая проверяет эти даты на корректность. Т. е. для каждой даты возвращает True (дата корректна) или False (некорректная дата).

# def date_rage(lst_data):
#     for _, __ in enumerate(lst_data):
#         lst_data_upd = __.split("-")
#         print(lst_data_upd)
#         if int(lst_data_upd[1]) > 12 or int(lst_data_upd[1]) < 1:
#             print(f"{False}")
#         elif int(lst_data_upd[2]) > 31 or int(lst_data_upd[2]) < 1:
#             print(f"{False}")
#         else:
#             print(f"{True}")
def date_check(lst_data):
    lst_data_upd = lst_data.split("-")
    if int(lst_data_upd[1]) > 12 or int(lst_data_upd[1]) < 1:
        print(f"{False}")
        return False
    elif int(lst_data_upd[2]) > 31 or int(lst_data_upd[2]) < 1:
        print(f"{False}")
        return False
    else:
        print(f"{True}")
        return True
stream = ['2018-04-02', '2018-02-29', '2018-19-02']
for i in stream:
    print(i)
    date_check(i)



#
# Задание 4 (бонусное)
# Ваш коллега прислал код функции:
#
# DEFAULT_USER_COUNT = 3
#
# def delete_and_return_last_user(region, default_list=[‘A100’, ‘A101’, ‘A102’]):
# ""“
# Удаляет из списка default_list последнего пользователя
# и возвращает ID нового последнего пользователя.
# ”""
# element_to_delete = default_list[-1]
# default_list.remove(element_to_delete)
#
# return default_list[DEFAULT_USER_COUNT-2]
# При однократном вызове этой функции все работает корректно:
# delete_and_return_last_user(1)
# ‘A101’
#
# Однако, при повторном вызове получается ошибка IndexError: list index out of range.
#
# Задание:
#
# Что значит ошибка list index out of range?
# Почему при первом запуске функция работает корректно, а при втором - нет?