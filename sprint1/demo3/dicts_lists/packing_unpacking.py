def func_args(*args: tuple) -> None:
    total = 0
    # lst = list(args)
    print(type(args))
    print(args)

    for number in args:
        total += number

    return total


def func_kwargs(**kwargs: dict) -> None:
    print(type(kwargs))
    # print(kwargs)
    kwargs['nova_chave'] = 'novo valor'
    # print(kwargs)

    for k, v in kwargs.items():
        print(k, v)

    return kwargs
