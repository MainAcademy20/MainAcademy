import string
action = input("Do you want to encrypt or decrypt a message?: ")
if((action!="encrypt") and (action!="decrypt")):
    print("Invalid command. Try again using 'encrypt' or 'decrypt'")
    exit()
else:
    filename = input("Enter the name of a file: ")
    key = int(input("Please enter a key (number): ")) % 26
    if(action=="decrypt"):
        key = -key
with open(filename, "r") as f:
    code = str(f.read())
    print(code)
    alphabet = (string.ascii_lowercase + string.ascii_uppercase) * 2
    message = ""
for letter in code:
    position = alphabet.find(letter)
    new_position = position + key
    if letter in alphabet:
        message += alphabet[new_position]
    else:
        message += letter
print("Your message is:", message)
action2 = input("Do you want create a file with the message?(yes/no): ")
if(action2=="yes"):
    filename2 = input("Enter a name of the file: ")
    with open(filename2, 'w') as m:
        m.write(message)
elif(action2=="no"):
    exit()
elif(action2!="yes", "no"):
    print("Invalid command!")
    exit()