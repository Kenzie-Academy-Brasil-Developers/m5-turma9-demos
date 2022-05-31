# Estrutura de dados chave/valor
# Chaves unicas
# Declaração literal
my_dict = {'chave': 'valor', 1: True}
print(my_dict)

my_dict = {'chave': 'valor', 1: True, 'chave': 'valor_2'}
print(my_dict)

x = 'valor'
x = 'valor_2'
print(x)

# Declaração via builtin
my_dict = dict(chave='Um Valor', chave_2='Outro Valor')
print(my_dict)

print(my_dict['chave'])
print(my_dict['chave_2'])

# Reatribuição
my_dict['chave'] = 'novo valor M5'
print(my_dict)
my_dict['nova_chave'] = 'novo valor M5'
print(my_dict)

# Erro ao acessar chave que não existe
# print(my_dict['chave_nao_existe'])

# Utilizando método get para acessar valor de dicionários
x = my_dict.get('chave_nao_existe', 'A chave não existe')
print(x)
