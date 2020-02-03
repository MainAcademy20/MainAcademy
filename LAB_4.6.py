var = ["one", "two", "three", "four", "five"]
file1 = "config_data_file.txt"
def open_write_data_file(func):
    def open_write(data):
        f = open("config_data_file.txt", "r+")
        func(f, data)
        f.close()
    return open_write



@open_write_data_file
def write_config(file, string):
    if "Configuration file! Do not modify!" in file.read():
        message = file.write("{},\n".format(string))
    else:
        message = file.write("Configuration file! Do not modify!\n" + "{}\n".format(string))
    return message


write_config(var)









