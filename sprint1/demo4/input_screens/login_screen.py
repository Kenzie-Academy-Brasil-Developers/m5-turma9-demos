import os
from users.user_login import login_user


def login():
    while True:
        username = input('Digite seu username: ')
        password = input('Digite seu password: ')

        os.system('clear')

        found_user = login_user(username, password)

        if found_user:
            print('Bem Vindo')
            print(found_user)
            break

        print('credenciais inválidas\n')
