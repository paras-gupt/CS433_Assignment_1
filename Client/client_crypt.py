# Encryption methods

def substitute(data):
    # Default offset is set to 2
    offset = 2
    # Only for Aplha Numeric characters
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    lowercase_aplhabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    uppercase_aplhabets = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    str = ""

    for letter in data:
        if letter in numbers:
            idx = numbers.index(letter)        
            str = str + numbers[(idx + offset)%10]
        elif letter in lowercase_aplhabets:
            idx = lowercase_aplhabets.index(letter)        
            str = str + lowercase_aplhabets[(idx + offset)%26]
        elif letter in uppercase_aplhabets:
            idx = uppercase_aplhabets.index(letter)        
            str = str + uppercase_aplhabets[(idx + offset)%26]
        else:
            str = str + letter

    return str

def transpose(data):
    str = ""
    sentences = data.split('\n')
    for i in range(len(sentences)):
        words = sentences[i].split()
        for j in range(len(words)):
            str = str + words[j][::-1]
            if(j != len(words)-1):
                str += ' '
        if(i!=len(sentences)-1):
            str = str + '\n'

    return str

def encrypt(mode, data):
    if (int(mode) == 1):
        return data
    elif (int(mode) == 2):
        return substitute(data)
    elif (int(mode) == 3):
        return transpose(data)

def encryption_mode():
    # Default encryption is set to plain text
    mode = 1
    print('''The following encryption modes are available:
            1 - Plain Text
            2 - Substitute
            3 - Transpose
        ''')
    mode = input('Enter encryption mode: ')

    while(not (int(mode) == 1 or int(mode) == 2 or int(mode) == 3)):
        mode = input('\nInvalid Encryption Mode. Enter encryption mode again: ')

    return mode

# Decryption methods

def de_substitute(data):
    # Default offset is set to 2
    offset = 2
    # Only for Aplha Numeric characters
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    lowercase_aplhabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    uppercase_aplhabets = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    str = ""
    for letter in data:
        if letter in numbers:
            idx = numbers.index(letter)        
            str = str + numbers[(idx - offset)%10]
        elif letter in lowercase_aplhabets:
            idx = lowercase_aplhabets.index(letter)        
            str = str + lowercase_aplhabets[(idx - offset)%26]
        elif letter in uppercase_aplhabets:
            idx = uppercase_aplhabets.index(letter)        
            str = str + uppercase_aplhabets[(idx - offset)%26]
        else:
            str = str + letter

    return str

def de_transpose(data):
    str = ""
    sentences = data.split('\n')
    for i in range(len(sentences)):
        words = sentences[i].split()
        for j in range(len(words)):
            str = str + words[j][::-1]
            if(j != len(words)-1):
                str += ' '
        if(i!=len(sentences)-1):
            str = str + '\n'

    return str

def decrypt(mode, data):
    if (int(mode) == int(1)):
        return data
    elif (int(mode) == int(2)):
        return de_substitute(data)
    elif (int(mode) == int(3)):
        return de_transpose(data)
