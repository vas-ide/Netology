
def return_string(analiz_file, analized_file):
    with open(analiz_file, 'r', encoding='utf8') as file_r:
        for write_string in file_r:
            analiz_string = write_string.split(",")
            print(analiz_string)
            # if analiz_string[-1] == "context":
                # with open(analized_file, 'a', encoding='utf8') as code:
                #     code.write(write_string)

return_string("visit_log.csv", "visit_context.csv")
