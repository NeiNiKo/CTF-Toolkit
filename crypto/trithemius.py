# Standard alphabets
alphabets = {
    "en": "abcdefghijklmnopqrstuvwxyz",
    "uk": "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя"
}

# Trithemius cipher function
def trithemius(text, alphabet, mode, position_mode, language):
    result = ""
    letter_index = 0
    for position, char in enumerate(text):
        # Handle character case
        if language == "custom":
            search_char = char
        else:
            search_char = char.lower()
        # Check if character is in alphabet
        if search_char in alphabet:
            index = alphabet.index(search_char)
            # Select shift position
            if position_mode == "all":
                shift = position
            else:
                shift = letter_index
            # Set shift direction
            if mode == "decode":
                shift = -shift
            # Calculate shifted index
            index_offset = (index + shift) % len(alphabet)
            encrypted_char = alphabet[index_offset]
            # Preserve uppercase for standard alphabets
            if char.isupper() and language != "custom":
                encrypted_char = encrypted_char.upper()
            result += encrypted_char
            # Count processed alphabet characters
            letter_index += 1
        else:
            # Preserve characters outside the alphabet
            result += char
    return result

# Get input text
text = input("Enter text: ")

# Select alphabet
language = input("Choose alphabet (en/uk/custom): ").strip().lower()

if language == "custom":
    alphabet = input("Enter your alphabet: ")
elif language in alphabets:
    alphabet = alphabets[language]
else:
    print("Error: Unknown alphabet!")
    exit()

# Validate alphabet
if len(alphabet) < 2 or len(set(alphabet)) != len(alphabet):
    print("Error: Alphabet must contain at least 2 unique characters!")
    exit()

# Select operation
mode = input("Choose mode (encode/decode): ").strip().lower()
if mode not in ("encode", "decode"):
    print("Error: Invalid operation mode!")
    exit()

# Select position counting mode
position_mode = input("Count positions (all/alphabet): ").strip().lower()
if position_mode not in ("all", "alphabet"):
    print("Error: Invalid position mode!")
    exit()

# Execute selected operation
result = trithemius(text, alphabet, mode, position_mode, language)
print("\nResult:", result)
