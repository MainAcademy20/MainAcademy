var = ["one", "two", "three", "four", "five"]
def open_write_data_file(func):
    def open_write(data):
        f = open(input("Enter the name of a file: "), "r+")
        func(data, f)
        print("Data file is: ", f)
        f.close()
    return open_write



@open_write_data_file
def write_config(file, string):
    if "Configuration file! Do not modify!" in file.read():
        message = file.write("{},\n".format(string))
        print(message)
    else:
        message = file.write("Configuration file! Do not modify!\n" + "{}\n".format(string))
        print(message)

for data in var:
    write_config(data)









