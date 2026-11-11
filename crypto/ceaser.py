# Standard alphabets
alphabets = {
    "en": "abcdefghijklmnopqrstuvwxyz",
    "uk": "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя"
}

# Caesar cipher function
def caesar(text, alphabet, key, unknown_mode, language):
    result = ""
    for char in text:
        # Handle character case
        if language == "custom":
            search_char = char
        else:
            search_char = char.lower()

        # Chack if character is in alphabet
        if search_char in alphabet:
            index = alphabet.index(search_char)
            # Calculate shafted index
            index_offset = (index + key) % len(alphabet)
            encrypted_char = alphabet[index_offset]
            #Preserve uppercase for standard alphabets
            if char.isupper() and language != "custom":
                encrypted_char = encrypted_char.upper()
            result += encrypted_char
        else:
            # Preserve unknow characters if selected
            if unknown_mode == "keep":
                result += char
    return result

# Brute force function
def brute_force(text, alphabet, unknown_mode, language):
    for key in range(len(alphabet)):
        result = caesar(text, alphabet, -key, unknown_mode, language)
        print("Key: ", key, "| Result:", result)

# Get input from the user
text = input("Enter text: ")

# Select alphabet
language = input("Choose alphabet (en/uk/custom): ").strip().lower()
if language == "custom":
    alphabet = input("Enter your alphabet: ")
elif language in alphabets:
    alphabet = alphabets[language]
else:
    print("Error: Unknow alphabet")
    exit()

# Validate alphabet
if len(alphabet) < 2 or len(set(alphabet)) != len(alphabet):
    print("Error: Alphabet must be at least 2 unique characters")
    exit()

# Select operation
mode = input("Choose mode (encode/decode/brute): ").strip().lower()

# Validate operation
if mode not in ("encode", "decode", "brute"):
    print("Error: Invalid operation mode")
    exit()

# Choose hot ot handle characters outside the alphabet
unknown_mode = input("Unknow characters (keep/remove): ").strip().lower()
if unknown_mode not in ("keep", "remove"):
    print("Error: Invalid mode")
    exit()

# Execute selected operation
if mode == "brute":
    brute_force(text, alphabet, unknown_mode, language)
elif mode in ("encode", "decode"):
    #Get and validate shift key
    try:
        key = int(input("Enter shift key: "))
    except ValueError:
        print("Error: Shift key must be an integer")
        exit()
    #set direction on shift
    if mode == "encode":
        key = abs(key)
    elif mode == "decode":
        key = -abs(key)
    result = caesar(text, alphabet, key, unknown_mode, language)
    print ("\nResult: ", result)
