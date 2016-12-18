from helpers import alphabet_position, rotate_character;

def encrypt(text, key):
    newString = "";

    keyPosition = 0;
    for letter in text:
        if letter.isalpha():
            newString += rotate_character(letter, alphabet_position(key[keyPosition]));
            keyPosition = (keyPosition + 1) % len(key);
        else:
            newString += letter;
            continue;

    return newString;



def main():
    message = input("Enter message to encrypt: ");
    key = input("Enter encryption key: ");
    print(encrypt(message, key));

if __name__ == '__main__':
    main();   
