def print_params(a=1, b='строка', c=True):
    print(a, b, c)


# print_params() #выводится на печать, поскольку заданы параметры по умолчанию
# print_params(b=25) #выводится на печать с заменой именного аргумента b
# print_params(c=[1,2,3]) #выводится на печать с заменой именного аргумента c
# print_params(5,3) #выводится на печать с заменой первых двух элементов

values_list = ("Danil", [5, 5, 4, 5], 1997)
values_dict = {'a': 'себестоимость', 'b': 120.17, 'c': ['наценка', '250%', 420]}
values_list_2 = ("Danil", [5, 5, 4, 5])
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 42)
