# This is part one of the Crypto Project: Initials
# User inputs a name, initials are returned

def get_initials(fullname): #I hate using underscores. This takes a string (a person's name) and returns their initials in uppercase

    initials = fullname[0]

    for i in range(len(fullname)):
        if fullname[i] == " ": #checks each character for a space
            initials += fullname[i + 1];

    return initials.upper(); #returns that string of capitalized initials

def main():
    name = input("Enter a name and I will tell you the initials: ")
    print("The initials of {} are {}!".format(name, get_initials(name)));

if __name__ == '__main__':
    main();
