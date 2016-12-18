from sys import argv, exit;
from helpers import alphabet_position, rotate_character;

def user_input_is_valid(cl_args):
    if cl_args[-1].isdigit():
        return True;
    if not cl_args[-1].isdigit():
        return False;


def encrypt(text, rot):
    newString = "";


    for character in text:
        newString += rotate_character(character, rot);

    return newString;


def main():
    if user_input_is_valid(argv):
        text = input("Enter a message to be encrypted: ");
        print(encrypt(text, int(argv[-1])));
    else:
        print("usage: python caesar.py n, where n is rotation amount as a whole number");
        exit();

if __name__ == '__main__':
    main()
