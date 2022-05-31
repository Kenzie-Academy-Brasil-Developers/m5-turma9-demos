"""
    Comentário multinha
"""

x = "bom dia"  # aspas duplas
y = 'M5'  # aspas simples
z = """
Um texto
multinhas
qualquer"""  # string multinha
w = str(1)

print(x)  # \n
print(y)
print(z)
print(w)
print(x, y)
print(x + y)
print(type(x))

# Template strings (formatted string)
z = 5
template_str = f'Boa tarde M{z}'
print(template_str)
z = str(z)
print(type(z))

print(template_str[0])
# print(template_str[39283928])

# Imutáveis
# template_str[0] = 'Z'  # Error
template_str = f'Zoa tarde M{z}'
print(template_str)

# Slicing
str_len = len(template_str)
print(str_len)
print(template_str[str_len - 1])
print(template_str[-1])
print(template_str[-2])

print(template_str)
print(template_str[1:5])
print(template_str)

print(template_str[2:7:2])
print(template_str)

# Split
str_split = template_str.split()
print(str_split)
print(type(str_split))
