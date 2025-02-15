
def fibonacci_dict(par):
    my_dict = {}
    for key in range(par+1):
        for value in fibonacci_list:
            if key == 0:
                my_dict[key] = []
            if key > value:
                if my_dict.get(key, False) is False:
                    my_dict[key] = [value]
                else:
                    my_dict[key].append(value)

    return my_dict

fibonacci_list = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233]

print(fibonacci_dict(5))





