num_list = [0, 1, 2, 3, 4, 5]


def combine(info_list):
    main_list = []
    for i in range(len(info_list) - 1):
        combine_list = []
        copy = info_list.copy()
        combine_list.append(copy.pop(0))
        combine_list.append(copy.pop(i))
        main_list.append(combine_list)
    return main_list

print(combine(num_list))