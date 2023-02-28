
def optimal_numb(data, n):
    min_arg = 0
    max_arg = 0
    if n not in data:
        for _, __ in enumerate(data):
            if n < __:
                max_arg = __
                min_arg = data[_ - 1]
                break
        result_dic = {}
        result_dic[min_arg] = abs(min_arg - n)
        result_dic[max_arg] = abs(max_arg - n)
        keys_dd = list(result_dic.keys())
        values_dd = list(result_dic.values())
        if values_dd[0] == values_dd[1]:
            print(f"{keys_dd[0]}")
            return keys_dd[0]
        elif values_dd[0] > values_dd[1]:
            print(f"{keys_dd[1]}")
            return keys_dd[1]
        else:
            print(f"{keys_dd[0]}")
            result_dic[0]
    else:
        print(f"{n}")
        return f"{n}"
optimal_numb([1, 7, 17, 23, 27, 35, 65], 20)