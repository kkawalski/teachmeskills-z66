def del_duplicates(l):
    res_list = []
    for item in l:
        if item not in res_list:
            res_list.append(item)
    return res_list

def join_list(l1, l2):
    l3 = [item for item in l1 if item in l2]
    return del_duplicates(l3)

def format_date(date):
    date_list = date.split('/')
    res_date = '-'.join([date_list[2], date_list[1], date_list[0]])
    return res_date

def reverse_list(l):
    return [l[i] for i in range(len(l) - 1, -1, -1)]
