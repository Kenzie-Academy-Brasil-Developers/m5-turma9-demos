# Declaração Literal
my_set = {10, 1, 2, 2, 1}

print(my_set)
print(type(my_set))

# Declaração via builtin
my_set = set(range(2, 10))
my_set_2 = set(range(5, 15))
print(my_set)
print(my_set_2)

# União
set_sum = my_set | my_set_2
print(set_sum)
# Equivalente
set_sum = my_set.union(my_set_2)
print(set_sum)

# Transformando set em lista
sum_list = list(set_sum)
print(sum_list)

# Somando listas
my_lst = ['lista', 'nova']
print(sum_list + my_lst)
