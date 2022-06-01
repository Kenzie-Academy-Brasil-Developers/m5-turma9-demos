from typing import Iterable


def loop_1(iterable: Iterable) -> None:
    # for (i=0;i<10;i++)
    #     array[i]
    for item in iterable:
        if type(item) is not int:
            print(f'{item} não é um int')
            break
        # print(item)
    else:
        print('o loop foi rodado até o fim')
    
    print('fim da funcao')


def loop_2(d: dict) -> None:
    # for key, value in d.items():
    #     print(key)
    #     print(value)

    # for value in d.values():
    #     print(value)

    for key in d.keys():
        print(key)

    # Equivalentes
    for key in d:
        print(key)


def check_password(password: str, param_2: str, special_char: str = '@!#$%&') -> str:
    print(password)
    print(param_2)
    print(special_char)

    return ''
