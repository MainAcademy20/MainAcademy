var = ["one", "two", "three", "four", "five"]
def open_write_data_file(func):
    def open_write(data):
        file = open("config_data_file.txt", "r+")
        func(file, data)
        file.close()
    return open_write



@open_write_data_file
def write_config(file, string):
    if "Configuration file! Do not modify!" in file.read():
        print("I`ll add in the file:\n", string)
        message = file.write("{}\n".format(string))
    else:
        message = file.write("Configuration file! Do not modify!\n" + "{}\n".format(string))
        print("I`ll add in the file:\n Configuration file! Do not modify!\n", string)
    file = open("config_data_file.txt", "r")
    for x in file:
        print(x)
    return message

write_config(var)









