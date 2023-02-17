

import json
import traceback


def calc_money():
    analiz_sum = 0
    with open('real_data.txt', 'r') as file:
        for line in file:
            line_upd = line.split(" ")
            line_upd_add = line_upd[1].split("\t")
            innit_num = (line_upd_add[2][:-1])
            try:
                innit_num_add = innit_num.replace(",", ".")
                analiz_sum += float(innit_num_add)
            except:
                print(traceback.print_exc())
    print(analiz_sum)
calc_money()




from datetime import datetime
date_string = "May 25 2017 5:00AM"
date_datetime = datetime.strptime(date_string, "%b %d %Y %I:%M%p" )


print(type(date_datetime))
print(date_datetime.year)
print(date_datetime.hour)
print(date_datetime.weekday())
print(datetime.now())

