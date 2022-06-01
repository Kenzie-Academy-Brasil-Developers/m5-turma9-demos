from funcoes import my_func
# Import absoluto
# from nome_pacote.conditionals import cond_1
# import nome_pacote
# from nome_pacote import conditionals
from nome_pacote import cond_1, cond_2, loop_1, loop_2, check_password

# print(__name__)


def main():
    # my_func(1, 2)
    # print(my_func(1, 2))
    # cond_1(5, 10)
    # nome_pacote.cond_2
    # conditionals.cond_2
    # cond_1('a', 'b')
    # print(cond_2(1, 2))

    # loop_1([1, 2, 3])
    # loop_1('python')
    # loop_1((1, 2, 3))
    # loop_1({1, 2, 3})
    # loop_1({'chave_1': 'valor_1', 'chave_2': 'valor_2'})
    # loop_2({'chave_1': 'valor_1', 'chave_2': 'valor_2'})

    # check_password('minha_senha')
    check_password(param_2='param_2', password='minha_senha')


if __name__ == '__main__':
    main()
