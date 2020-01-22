def user_login():
    login = input('Login: ')
    password = input('Password: ')
    return login, password


login, password = user_login()


def read_write_file():
    try:
        users_content = open('Users.txt')
    except (OSError, IOError):
        users_content = open('Users.txt', 'w')
        users_content.write('1. Mark qwe123\n2. Ivan zxc123\n3. Oleg qwe123')
        users_content.close()


def format_line():
    lines = []
    with open('Users.txt', 'r+') as user:
        user = user.readlines()
    for line in user:
        number, name, *passw = line.split()
        lines.append('{} {}'.format(name, ' '.join(passw)))
    return lines


content = format_line()


def check_line():
    for line in content:
        name, passw = line.split()
        if name == login and password == passw:
            return print('ok')
        elif name == login and password != passw:
            return print('not ok')
    content.append('{} {}'.format(login, password))
    print('added')


check_line()


def get_key(line):
    return line[0].lower()


content.sort(key=get_key)


def format_text():
    text = ''
    for i, login in enumerate(content, start=1):
        text += '{}. {}\n'.format(i, login)
    return text


def write_text():
    users_content = open('Users.txt', 'w')
    users_content.write(format_text())
    users_content.close()


write_text()
