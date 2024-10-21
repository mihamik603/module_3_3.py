def print_params(a = 1, b = 'строка', c = True):
    print(f"a = {a}, b = {b}, c = {c}")


print_params()
print_params(2)
print_params(2, 'new_string')
print_params(2, 'new_string', False)
print_params(b = 25)
print_params(c = [1,2,3])

values_list = [4, 'another_string', False]
values_dict = {'a': 5, 'b': 'yet_another_string', 'c': None}

print_params(*values_list)
print_params(**values_dict)


values_list_2 = [6, 'hello']

print_params(*values_list_2, 42)