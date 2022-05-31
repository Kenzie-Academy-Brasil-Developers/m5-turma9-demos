# Declaração Literal
my_lst = [1, 'String', False, 3.8, ['Outra', 'Lista']]
print(my_lst)
print(type(my_lst))

# Acessando elementos
print(my_lst[0])
print(my_lst[-1])

# Declaração via builtin
my_lst_2 = list('uma string')
print(my_lst_2)

my_lst_2 = list(range(2, 7, 2))
print(my_lst_2)

# Slicing
print(my_lst[:4])
print(my_lst[3:])

# Mutável
my_lst[0] = 'Novo Valor'
print(my_lst)

# Adicionando item
my_lst.append(-8000)
print(my_lst)
