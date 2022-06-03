from users.user_login import is_username_valid, is_password_valid, login_user


def test_is_username_valid_success():
    username = 'chrystian2'

    result = is_username_valid(username=username)
    expected = True

    # is
    assert result is expected, 'Usuário deveria ter sido validado'


def test_is_username_valid_fail():
    username = 'chrystian'

    result = is_username_valid(username=username)
    expected = False

    # is
    assert result is expected


def test_is_password_valid_success():
    password = 'senh@'

    result = is_password_valid(password=password)
    expected = True

    assert result is expected, 'Senha deveria ter sido validada'


def test_is_password_valid_less_chars():
    password = '1'

    result = is_password_valid(password=password)
    expected = False

    assert result is expected, 'Senha deveria ter sido validada'


def test_is_password_valid_more_chars():
    password = '1' * 13

    result = is_password_valid(password=password)
    expected = False

    assert result is expected, 'Senha deveria ter sido validada'


def test_login_success():
    username = 'chrystian'
    password = 'senh@'

    result = login_user(username=username, password=password)
    expected = {'username': 'chrystian', 'password': 'senh@', 'job': 'Instrutor'}

    assert type(result) is dict, 'Verifique se o retorno de `login_user` quando sucesso é um dict'
    assert result == expected


def test_login_fail():
    username = 'chrystian'
    password = 'senh@aaa'

    result = login_user(username=username, password=password)
    expected = None

    assert result is expected
