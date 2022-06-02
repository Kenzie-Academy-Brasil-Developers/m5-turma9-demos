def list_c(max_range: int):
    """
        Essa função criar uma lista de numeros de 1 até max_range
    """
    # numbers = list(range(1, max_range))
    # numbers = []

    # for number in range(1, max_range + 1):
    #     if number % 2 == 0:
    #         numbers.append('par')
    #     else:
    #         numbers.append('impar')

    # return numbers

    # Copia
    # return [number for number in range(1, max_range + 1)]

    # return [number * 2 for number in range(1, max_range + 1)]
    # return ['ok' for _ in range(1, max_range + 1)]
    # return [number for number in range(1, max_range + 1) if number % 2 == 0]
    return ["even" if number % 2 == 0 else "odd" for number in range(1, max_range + 1)]

    # map()
    # filter()
    # from functools import reduce
    # reduce()


def dict_c(d: dict):
    # new_d = {}

    # for key, value in d.items():
    #     if len(key) > 4:
    #         new_d[key] = value

    # return new_d
    lista = ['valor', 'casa', 'cachorro']
    # return {key: value for key, value in d.items() if len(key) > 4}
    # return {f'id_{index}': item for index, item in enumerate(lista)}
    return {index: item for index, item in enumerate(lista, 1)}
