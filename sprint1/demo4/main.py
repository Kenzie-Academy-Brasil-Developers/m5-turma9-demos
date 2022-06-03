from input_screens.main_screen import welcome
from users.user_login import is_password_valid


def main():
    # name = input('Escreva seu nome: ')
    # print('Escreva seu nome: ')
    # name = input()
    # name = input('Escreva seu nome: \n')
    # print(f'Bem vindo {name}!!')
    # welcome()

    password = '1' * 4
    print(is_password_valid(password))  # False

    password = '1' * 5
    print(is_password_valid(password))  # True

    password = '1' * 12
    print(is_password_valid(password))  # True

    password = '1' * 15
    print(is_password_valid(password))  # False


if __name__ == '__main__':
    main()
