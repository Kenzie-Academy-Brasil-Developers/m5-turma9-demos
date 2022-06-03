from .valid_users import USERS


def is_username_valid(username: str) -> bool:
    for user in USERS:
        if user['username'] == username:
            return False

    return True


def is_password_valid(password: str, special_chars='@!#%$') -> bool:
    # tem de ter entre 5 e 12 caracteres
    # if len(password) <= 4 or len(password) >= 13:
    #     return False
    if not 5 <= len(password) <= 12:
        return False

    # TODO:
    # Verificação se a string possui ao menos 1 caracters de `special_chars`
    # for/else

    return True


def login_user(username: str, password: str) -> dict | None:
    for user in USERS:
        if user['username'] == username and user['password'] == password:
            return user
