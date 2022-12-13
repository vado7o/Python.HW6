# Дан список интов, повторяющихся элементов в списке нет. Нужно преобразовать это множество в строку, сворачивая соседние по числовому ряду числа в диапазоны. 
# Примеры: [1,4,5,2,3,9,8,11,0] => "0-5,8-9,11" [1,4,3,2] => "1-4" [1,4] => "1,4"

# import os
# os.system('cls')

# list_int = [1,4,5,2,3,9,8,11,0]
# list_int.sort()
# output = ''
# fix = False

# output += '\"' + str(list_int[0])

# for ind in range(1, len(list_int)):    
#     if list_int[ind] - list_int[ind - 1] == 1:
#         fix = True
#         if ind == len(list_int) - 1:
#             output += '-' + str(list_int[ind])
#     else:
#         if fix == True:
#             output += '-' + str(list_int[ind - 1]) + ', ' + str(list_int[ind])
#             fix = False
#         else:
#             output += ',' + str(list_int[ind])
# output += '\"'

# print(f'Результат сворачивания в диапазоны для списка {list_int} = {output}\n')

# ********************************************************************************************************

# Дана строка (возможно, пустая), состоящая из букв A-Z написать функцию RLE, которая на выходе даст строку и сгенерирует ошибку, если
# на вход пришла невалидная строка

# import re
# import os
# os.system('cls')
# pattern = re.compile("([A-Z]+)")
# string = 'AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB'

# def zipping(string):
#     new_str = ''
#     count = 1

#     for i in range(1, len(string)):
#         if string[i] == string[i - 1]:
#             count += 1
#         else:
#             new_str = new_str + str(count) + string[i-1]
#             count = 1

#     new_str = new_str + str(count) + string[-1]
#     new_str = ''.join(filter(lambda x: x != '1', new_str))
#     return new_str

# if (string == '' or not bool(pattern.fullmatch(string))):
#     print('Неверно введена строка на вход!!!!\n')
# else:    
#     print(zipping(string))