


# def return_string(analiz_file, analized_file):
#     with open(analiz_file, 'r', encoding='utf8') as file:
#         for write_string in file:
#             analiz_lst = write_string.split(",")
#             if analiz_lst[-1] == "context\n":
#                 print(analiz_lst)
#                 with open(analized_file, 'a', encoding='utf8') as code:
#                     code.write(f"{write_string}")
#
# return_string("visit_log.csv", "visit_context.csv")


# import json
# dict_stat = {}
# def get_stat(file_name):
#     file_json = json.loads(file_name)
#     with open(file_json, 'r', encoding='utf8') as file:
#         for line in file:
#             print(line)
#
# get_stat('purchase_log.txt')


# import json
# def get_stat(file_name):
#     dict_stat = {}
#     with open(file_name, 'r', encoding='utf8') as file:
#         for line in file:
#             line_upd = json.loads(line)
#             if line_upd['category'] not in dict_stat:
#                 dict_stat[line_upd['category']] = 1
#             else:
#                 dict_stat[line_upd['category']] += 1
#     print(f"{dict_stat}")
# get_stat('purchase_log.txt')


import json
# def get_stat(file_name):
#     dict_stat = {}
#     with open(file_name, 'r', encoding='utf8') as file:
#         for line in file:
#             line_upd = json.loads(line)
#             dict_stat[line_upd['category']] = [line_upd['user_id']]
#             with open('get_stat.txt', 'a', encoding='utf8') as code:
#                 code.write(f"{{{line_upd['category']}: {line_upd['user_id']}}}\n")
#
#     print(f"{dict_stat}")
# get_stat('purchase_log.txt')


import json
purchases = {}
def get_stat(file_name):
    with open(file_name, 'r', encoding='utf8') as file:
        for num, line in enumerate(file):
            line_upd = json.loads(line)
            purchases[line_upd['user_id']] = line_upd['category']
            with open('get_stat.txt', 'a', encoding='utf8') as code:
                code.write(f"{line_upd['user_id']}: {line_upd['category']}\n")
get_stat('purchase_log.txt')


def get_analiz(file_name):
    with open('funnel.csv', 'a', encoding='utf8') as code:
        code.write(f"user_id,source, purchase\n")
    with open(file_name, 'r', encoding='utf8') as file:
        for line in file:
            line_upd = line[:-2].split(",")
            if line_upd[0] in purchases:
                with open('funnel.csv', 'a', encoding='utf8') as code:
                    code.write(f"{line_upd[0]},{str(line_upd[1])}, {purchases[line_upd[0]]}\n")
get_analiz('visit_log.csv')



