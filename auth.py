from Encrypt_String import read_from_file, write_to_file


def ask_credentials():
    input_login = input('Login: ')
    input_password = input('Password: ')
    return input_login, input_password


def read_content_from_file(file_name):
    file_content = []
    try:
        credentials = open(file_name)
    except (OSError, IOError):
        write_to_file(file_name, '1. Mark qwe123\n2. Ivan zxc123\n3. Oleg qwe123')
        credentials = open(file_name)
    for line in credentials:
        if not line:
            continue
        number, name, *passw = line.split()
        file_content.append('{} {}'.format(name, ' '.join(passw)))
    credentials.close()
    return file_content


def convert_array_to_string(input_content):
    text = ''
    for i, input_credentials in enumerate(input_content, start=1):
        text += '{}. {}\n'.format(i, input_credentials)
    return text


def check_access(input_content, input_login, input_password):
    for line in input_content:
        name, passw = line.split()
        if input_login == name and passw == input_password:
            print(input_content)
            print('Access Granted')
            exit()
        elif input_login == name and passw != input_password:
            print('Access Denied')
            exit()
    register_new_user(content, login, password)


def register_new_user(input_content, input_login, input_password):
    new_content = input_content.copy()
    print(new_content)
    choice = input('Do you want to register?\n')
    if choice:
        if input_login != input_password:
            new_content.append('{} {}'.format(input_login, input_password))
        else:
            print('A password must be different than your login')
    else:
        exit()
    new_content.sort(key=lambda line: line[0].lower())
    write_to_file('Users.txt', convert_array_to_string(new_content))


login, password = ask_credentials()
content = read_content_from_file('Users.txt')
check_access(content, login, password)
