import os
from .login_screen import login

def welcome():
    # while True:
    #     name = input('Escreva seu nome: \n')
    #     age = input('Escreva sua idade: \n')

    #     print(type(name))
    #     print(type(age))

    #     if name == 'chrystian':
    #         print(f'Bem vindo {name} {age}!!')
    #         break

    #     print('nome inválido')
    os.system('clear')
    while True:
        # os.system('clear')

        print('1. Logar')
        print('2. Registrar')
        print('3. Sair')

        choice = input('Escolha uma opção: ')

        if choice == '1':
            os.system('clear')
            login()
            print('login bem sucedido')
            break
        elif choice == '2':
            os.system('clear')
            # TODO:
            # não pode username já cadastrado
            # senha tem de estar nos padroes da funcao is_password_valid
            print('register screen \n')
        elif choice == '3':
            os.system('clear')
            break
            # print('exit \n')
        else:
            os.system('clear')
            print('Escolha uma opção válida (1, 2, 3) \n')
