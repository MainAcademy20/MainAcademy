login = input('Login: ')
password = input('Password: ')


def open_file():
    return open('Users.txt')


def open_file_w():
    return open('Users.txt', 'w')


try:
    users = open_file()
except (OSError, IOError):
    users = open_file_w()
    users.write('1. Mark qwe123\n2. Ivan zxc123\n3. Oleg qwe123')
    users.close()
    users = open_file()


def content_add(log, pas):
    return content.append('{} {}'.format(log, pas))


content = []
for line in users:
    if not line:
        continue
    number, name, *passw = line.split()
    content_add(name, ' '.join(passw))
content_add(login, password)
users.close()

####

for line in content:
    name, passw = line.split()
    if login == name and passw == password:
        print('OK')

    elif login == name and passw != password:
        print('Not OK')


def get_key(line):
    return line[0].lower()


content.sort(key=get_key)
text = ''

for i, login in enumerate(content, start=1):
    text += '{}. {}\n'.format(i, login)


users = open_file_w()
users.write(text)
users.close()
