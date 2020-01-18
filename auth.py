def user_login():
        login = input('Login: ')
        password = input('Password: ')
        return login, password

login, password = user_login()

def user_update():
    try:
        users = open('Users.txt')
    except (OSError, IOError):
        users = open('Users.txt', 'w')
        users.write('1. Mark qwe123\n2. Ivan zxc123\n3. Oleg qwe123')
        users.close()
        users = open('Users.txt')


    content = []
    for line in users:
        if not line:
            continue
            number, name, *passw = line.split()
            content.append('{} {}'.format(name, ' '.join(passw)))
    content.append('{} {}'.format(login, password))
    users.close()

####

    for line in content:
        name, passw = line.split()
        if login == name and passw == password:
            print('OK')
            exit()
        elif login == name and passw != password:
            print('Not OK')
            exit()

user_update(user_login())
####

def get_key(line):
    return line[0].lower()

content.sort(key=get_key)
text = ''

for i, login in enumerate(content, start=1):
    text += '{}. {}\n'.format(i, login)


users = open('Users.txt', 'w')
users.write(text)
users.close()
