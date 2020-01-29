data_list = ['foto', 'text', 'users', 'login', 'password']


def openfile(writeConfig):
    def openConfig(data):
        file = open("config.data", 'r+')
        writeConfig(file, data)
        file.close()
    return openConfig


@openfile
def writeConfig(file, line):
    if 'Configuration file! Do not modify!' not in file.read():
        file.write('\n''Configuration file! Do not modify!''\n')
    else:
        file.write("%s;\n" % line)


for data in data_list:
    writeConfig(data)
