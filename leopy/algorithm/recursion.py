def recursion_sum(data_list):
    if data_list == []:
        return 0
    else:
        sum_1 = data_list.pop(0)
        return sum_1+recursion_sum(data_list)

def recursion_listCount(data_list):
    if data_list == []:
        return 0
    else:
        data_list.pop(0)
        return 1+recursion_listCount(data_list)

def recursion_max(data_list):
    maximum = data_list[0]
    if len(data_list)==1:
        return maximum
    else:
        data_list.pop(0)
        find_max = recursion_max(data_list)
        if maximum < find_max:
            maximum = find_max
    return maximum
