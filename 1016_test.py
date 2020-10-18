i = 1
square_list = [4]
while ((2 * i) + 1) ** 2 <= 1000000000000:
    square_list.append(((2 * i) + 1) ** 2)
    i += 1
print(len(square_list))