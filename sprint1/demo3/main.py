from dicts_lists.referencias import ref_int, ref_list, ref_dict
from dicts_lists.packing_unpacking import func_args, func_kwargs
from dicts_lists.comprehension import list_c, dict_c


def main():
    # n = 5
    # print(f'antes de chamar ref_int -> {n}')
    # ref_int(n)
    # print(f'depois de chamar ref_int -> {n}')

    # lista = [1, 2, 3, 4]
    # print(f'antes de chamar ref_list -> {lista}')
    # ref_list(lista)
    # print(f'depois de chamar ref_list -> {lista}')

    # d = {'name': 'chrystian'}
    # print(f'antes de chamar ref_dict -> {d}')
    # ref_dict(d)
    # print(f'depois de chamar ref_dict -> {d}')

    # print(func_args(1, 2, 5, 5, 10))
    # lista = [1, 2, 3]
    # print(func_args(*lista))
    # print(func_args(*[1, 2, 3]))

    # func_kwargs(name='chrystian', module='M5', age='29')
    # func_kwargs(**{'name': 'chrystian', 'module': 'M5'})
    # d = {'name': 'chrystian', 'module': 'M5'}
    # func_kwargs(**d)
    # print(d)
    # print(list_c(10))

    d = {'name': 'chrystian', 'module': 'M5', 'age': 10}
    # print(d)
    print(dict_c(d))


if __name__ == '__main__':
    main()
