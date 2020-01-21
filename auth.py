def user_login():
    login = input('Login: ')
    password = input('Password: ')
    return login, password


login, password = user_login()

try:
    users = open('Users.txt')
except (OSError, IOError):
    users = open('Users.txt', 'w')
    users.write('1. Mark qwe123\n2. Ivan zxc123\n3. Oleg qwe123')
    users.close()

with open('Users.txt', 'r+') as users:
    users = users.readlines()
content = []


def format_line():
    for line in users:
        number, name, *passw = line.split()
        content.append('{} {}'.format(name, ' '.join(passw)))


format_line()


def check_line():
    for line in content:
        name, passw = line.split()
        if name == login and password == passw:
            return print('ok')
        elif name == login and password != passw:
            return print('not ok')
    if name != login:
        content.append('{} {}'.format(login, password))
        print('added')


check_line()


def get_key(line):
    return line[0].lower()


content.sort(key=get_key)
text = ''


for i, login in enumerate(content, start=1):
    text += '{}. {}\n'.format(i, login)

users = open('Users.txt', 'w')
users.write(text)
users.close()
