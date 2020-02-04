lst = ["one", "two", "tree", "fore", "five"]


def dc(func):
    def open_file(item):
        data_file = open("config.data", "r+")
        func(data_file, item)
        data_file.close()
        print(data_file, item, open_file)

    return open_file


@dc
def writeConfig(file, line):
    if "Configuration file! Do not modify!" in file.read():
        file.write("%s;\n" % (line))
    else:
        file.write("Configuration file! Do not modify!\n" + \
                   "%s;\n" % (line))


for item in lst:
    writeConfig(item)
