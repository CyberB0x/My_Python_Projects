# Convert a string to an array
def string_to_array(arr):
    #Если строка пустая, возвращяем массив с одной пустой строкой
    if arr == "":
        return ['']

    #В противном случае разбиваем строку на слова
    return arr.split()

#Вызов функции
result_1 = string_to_array("Hello Python")
result_2 = string_to_array("I love Python code")
result_3 = string_to_array("")

#Проверка на равенство
print(result_1)
print(result_2)
print(result_3)

#Проверка на равенство с пустым массивом
print(result_3 == [''])