alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'];
#here is a comment
def alphabet_position(char):

    char = char.lower();

    for i in range(len(alphabet)):

        if char == alphabet[i]:
            return i;

def rotate_character(char, rot):

    if not char.isalpha():
        return char;

    newPosition = (alphabet_position(char) + rot) % len(alphabet);

    if char.isupper():
        return alphabet[newPosition].upper();
    elif char.islower():
        return alphabet[newPosition].lower();
