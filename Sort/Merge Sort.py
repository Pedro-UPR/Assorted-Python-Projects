def sort_two_lists(l1, l2):
    new_list = []
    l1_ind, l2_ind = 0, 0
    while len(new_list) < len(l1) + len(l2):
        if l1_ind == len(l1):
            new_list.append(l2[l2_ind])
            l2_ind += 1
        elif l2_ind == len(l2):
            new_list.append(l1[l1_ind])
            l1_ind += 1
        else:
            l1_val = l1[l1_ind]
            l2_val = l2[l2_ind]
            if l1_val > l2_val:
                new_list.append(l1_val)
                l1_ind += 1
            else:
                new_list.append(l2_val)
                l2_ind += 1
    return new_list


def merge_sort(lst):
    # creates a list of sorted pairs
    temp_list = []
    for i in range(0, len(lst), 2):
        a = lst[i]
        if i == len(lst) - 1:
            temp_list.append([a])
        else:
            b = lst[1 + i]
            if a > b:
                temp_list.append([a, b])
            else:
                temp_list.append([b, a])
    # merges the elements
    while len(temp_list) > 1:
        temp_list_two = []
        for i in range(0, len(temp_list), 2):
            l1 = temp_list[i]
            if i == len(temp_list) - 1:
                temp_list_two.append(l1)
            else:
                l2 = temp_list[i + 1]
                new_list = sort_two_lists(l1, l2)
                temp_list_two.append(new_list)
        temp_list = temp_list_two


# explodes if given an odd list
# too many loops?

import random, time

lst = []
'''
for _ in range(1000000):
    lst.append(random.randint(0, 10000))'''
for x in range(1000000, 0, -1):
    lst.append(x)

t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
print(current_time)
merge_sort(lst)
t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
print(current_time)