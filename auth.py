from Encrypt_String import read_from_file, write_to_file


def ask_credentials():
    input_login = input('Login: ')
    input_password = input('Password: ')
    return input_login, input_password


login, password = ask_credentials()


def read_credentials_from_file(file_name):
    content = []
    try:
        credentials = open(file_name)
    except (OSError, IOError):
        write_to_file(file_name, '1. Mark qwe123\n2. Ivan zxc123\n3. Oleg qwe123')
        credentials = open(file_name)
    for line in credentials:
        if not line:
            continue
        number, name, *passw = line.split()
        content.append('{} {}'.format(name, ' '.join(passw)))
    credentials.close()
    return content


def add_user(content):
    new_content = content
    new_content.append('{} {}'.format(login, password))
    return new_content


print(read_credentials_from_file('Users.txt'))


def write_credentials_to_file():
    write_to_file('Users.txt', text)
    pass


####

for line in content:
    name, passw = line.split()
    if login == name and passw == password:
        print('OK')
        exit()
    elif login == name and passw != password:
        print('Not OK')
        exit()

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
