def find_dup(arr):
    see = set()
    duplicate = []
    for i in arr:
        if i in see:
            duplicate.append(i)
        else:
            see.add(i)
    return duplicate

my_arr = [10, 20, 30, 40, 50, 40, 50, 60, 70, 70, 80, 90, 100]
print(find_dup(my_arr))

my_arr_2 = []
print(find_dup(my_arr_2))

my_arr_3 = [1, 2, 3, 4, 5, 6]
print(my_arr_3)
