import re


def return_nord(relation_list, end_list):
    main_added = False
    need_nord = []
    for end in end_list:
        p = re.compile("\d+$")
        pick = p.search(str(end)).group()
        sub_added = False
        for relation in relation_list:
            if relation[1] == str(pick):
                main_added = True
                sub_added = True
                need_nord.append(str(end) + "-" + str(relation[0]))
        if not sub_added:
            need_nord.append(end)
    if not main_added:
        return need_nord
    return return_nord(relation_list, need_nord)


T = int(input())
for i in range(T):
    build_num, rule_num = map(int, input().split())
    price = list(map(int, input().split()))
    num = []
    for j in range(rule_num):
        num.append(input().split())

    data = return_nord(num, [input()])
    print(price)
    print(data)