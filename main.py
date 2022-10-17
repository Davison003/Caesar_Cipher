import art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1','2', '3','4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', ' ']


def caesar(text, shift, direction):
    final_text = ""
    if shift > 26:
        shift %= 26
    
    if direction == 'decode':
        shift *= -1

    for position in range(len(text)):
        if (text[position] in numbers) or (text[position] in symbols):
            final_text += text[position]
            continue
        index_letter = alphabet.index(text[position], 26)
        final_text += alphabet[index_letter + shift]

    print(f"The {direction}d text will be: {final_text}")


print(art.logo)

testing = True
while(testing):
    
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(text, shift, direction)
    
    quit = input("Leave? Yes/No\n").lower()
    if(quit == 'yes'):
        testing = False
    else:
        continue

