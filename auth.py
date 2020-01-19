def reg ():
    login = input('Login: ')
    password = input('Password: ')
    return login, password

def check (lg,pw,stroka):
    for stroka in content:
        name, passw = stroka.split()
        if lg == name and pw == passw:
            return True
            exit()
        elif lg == name and pw != passw:
            return False
            exit()

def get_key(line):
    return line[0].lower()

def sorting (spisok):
    spisok.sort(key=get_key)
    text = ''
    for i, log in enumerate(spisok, start=1):
        text += '{}. {}\n'.format(i, log)
    return text

s = reg()
login = s[0]
password = s[1]

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

if not (check(login, password,line)):
    content.append('{} {}'.format(login, password))

users.close()

ftext = sorting (content)

users = open('Users.txt', 'w')
users.write(ftext)
users.close()
