import requests

# Домашнее задание к лекции "Понятие класса"
# Задание 1
# Напишите функцию, которая возвращает название валюты (поле ‘Name’) с максимальным значением курса с помощью сервиса https://www.cbr-xml-daily.ru/daily_json.js

# def list_valutes():
#     r = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
#     response = r.json()
#     for _ in response['Valute']:
#         print(f"{_}")
# list_valutes()
# def request_name_money(name_valute):
#
#     r = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
#     response = r.json()
#     print(f"Actual-Date:{response['Date']}\n"
#           f"{response['Valute'][name_valute]['CharCode']}-{response['Valute'][name_valute]['Name']}\n"
#           f"{response['Valute'][name_valute]['Value']}")
#     # print(f"{r.json()}")
#     # return r.json()
# request_name_money("BGN")



# Задание 2
# Добавьте в класс Rate параметр diff (со значениями True или False), который в случае значения True в методах eur и usd будет возвращать не курс валюты,
# а изменение по сравнению в прошлым значением. Считайте, self.diff будет принимать значение True только при возврате значения курса.
# При отображении всей информации о валюте он не используется.


class Rate:
    def __init__(self, format='value'):
        self.format = format
        self.diff = False

    def exchange_rates(self):
        r = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
        return r.json()['Valute']

    def make_format(self, currency):
        response = self.exchange_rates()
        if currency in response:
            if self.format == 'full':
                print(f"{response[currency]}")
                return response[currency]

            if self.format == 'value' and self.diff is False:
                print(f"{response[currency]['Value']}")
                return response[currency]['Value']
            else:
                print(f"{round(response[currency]['Value'] - response[currency]['Previous'], 3)}")
                return round(response[currency]['Value'] - response[currency]['Previous'], 3)
        return 'Error'

    def eur(self):
        self.diff = True
        return self.make_format('EUR')
    def usd(self):
        self.diff = True
        return self.make_format('USD')
    def dkk(self):
        return self.make_format('DKK')



val = Rate('full')
val.make_format('AUD')
val.make_format('GBP')
val.dkk()
val.usd()
val = Rate()
val.dkk()
val.usd()




# Задание 3
# Напишите класс Designer, который учитывает количество международных премий. Подсказки в коде занятия в разделе “Домашнее задание задача 3”.




class Designer():
    def __init__(self, name, seniority, awards):
        self.name = name
        self.seniority = seniority + (awards * 2)
        self.grade = 0
        self.awards = awards

    def grade_up(self):
        self.grade += 1

    def check_if_it_is_time_for_upgrade(self):
        self.seniority += 1
        if self.seniority % (7 + self.grade) == 0:
            self.grade_up()
            self.seniority = 0
        return self.publish_grade()

    def publish_grade(self):
        print(f"Сотрудник-{self.name}     Специалитет: Освоенно:{self.seniority}  Необходимо:{7 + self.grade}     Прогресс-{self.grade}")

elena = Designer('Елена', seniority=0, awards=2)
for i in range(20):
    elena.check_if_it_is_time_for_upgrade()




