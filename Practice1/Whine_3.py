def weird_sort(lst):
    lst.sort()
    length_list = len(lst)
    temp_list = []

    x = 0
    y = length_list - 1
    i = 0

    while x <= y:
        if i % 2 == 0:
            temp_list.append(lst[y])
            y -= 1
        else:
            temp_list.append(lst[x])
            x += 1
        i += 1

    print(temp_list, end=" ")

user_input = [10, 20, 30, 40, 50, 60]
weird_sort(user_input)