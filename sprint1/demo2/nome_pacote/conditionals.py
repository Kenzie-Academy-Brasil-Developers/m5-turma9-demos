# print(__name__)


def cond_1(a: int, b: int) -> None:
    if a > b:
        print('a é maior que b')
    elif a == b:
        print('a é igual a b')
    else:
        print('b é maior que a')
    # !=


def cond_2(a: int, b: int) -> int:
    # Má prática
    # if a > b:
    #     return a
    # else:
    #     return b

    # Seguindo clean clode
    # if a > b:
    #     return a

    # return b

    return a if a > b else b
