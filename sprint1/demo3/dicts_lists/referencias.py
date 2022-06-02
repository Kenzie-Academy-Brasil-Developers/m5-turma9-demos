def ref_int(number: int) -> None:
    number = 10
    print(f'dentro de ref_int -> {number}')


def ref_list(lst: list) -> None:
    # lista_1 = lst[:]
    lista_1 = lst.copy()
    lista_1[0] = 'Novo Elemento'

    print(f'dentro de ref_lst -> {lista_1}')


def ref_dict(d: dict) -> None:
    d['nova_chave'] = 'Novo Valor'
    print(f'dentro de ref_dict -> {d}')
