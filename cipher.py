import random

INPUT_ERROR = 'INPUT ERROR: Please reply with either "Y" or "N"'

def make_key_dict():
    """Creates a dictionary of every symbol on a US keyboard and randomly assigns a substitute with no duplicates"""
    def character_list():
        """Create and return a list of all characters possible to input in a traditional English keyboard"""
        return ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '`', '~', '{', '[', '}', ']', ':', ';', '"', "'", ",", '<', '.', '>', '?', '/', ' ']
    #Create dictionary key
    key_dict = {}
    #Create two lists of equal length, one standard and one randomly shuffled
    symbol_list_shuffled = character_list()
    symbol_list_shuffled = random.sample(symbol_list_shuffled, k = len(symbol_list_shuffled))
    symbol_list_og = character_list()
    #Randomly assign symbols to each character in the original list
    for _ in range(len(symbol_list_shuffled)):
        if symbol_list_og[_] not in key_dict:
            key_dict[symbol_list_og[_]] = symbol_list_shuffled[_]

    return key_dict
    
def encrypt_decrypt(text, cipher_key):
    """Encrypts or decrypts cleartext to an encrypted string or vice versa according to the given key"""
    text_cipher = ''
    for i in text:
        i = cipher_key[i]
        text_cipher = text_cipher + i
    return text_cipher

def print_key(key, message):
    """Prints the characters used and their corresponding substitute in alphabetical order"""
    message_list = set(sorted(message))
    for i in message_list:
        print(f'{key[i]} = {i}')

def dict_to_string(dictionary):
    """Converts a dictionary item to a series of strings"""
    dict_to_string = [ f'{key} : {dictionary[key]}' for key in dictionary ]
    return dict_to_string

def encrypt_mode():
    """The function that encrypts messages"""
    usr_message = input("Enter your message to be encrypted:")
    encryption_key_dict = make_key_dict()
    encrypted_message = encrypt_decrypt(usr_message, encryption_key_dict)
    print('Encrypted message:')
    print(encrypted_message)
    print()
    print('Relevant Key:')
    print_key(encryption_key_dict, usr_message)
    print()
    save_decrypt_txt = ''
    while save_decrypt_txt.lower() != 'y' and save_decrypt_txt.lower() != 'n':
        save_decrypt_txt = input("Save full cipher key as .txt file? (Y/N): ")
        print()
        if save_decrypt_txt.lower() == 'y':
            print('"cipher.txt" will be updated with your current cipher key.')
            cipher_name = input('Enter a name for this cipher: ')
            dict_string = dict_to_string(encryption_key_dict)
            with open('cipher.txt', 'w') as key_file:
                key_file.write(f'{cipher_name}\n')
                for dict_entry in dict_string:
                    key_file.write(f'{dict_entry}\n')

        elif save_decrypt_txt.lower() == 'n':
            print('"cipher.txt" will not be updated.')

        else:
            print(INPUT_ERROR)

def first_and_last(unsplit_line):
    """Takes the first and last characters of any string and returns them in a list of two items (i.e. '12345' would return [1,5]). Also removes \n at the end of lines. This is done to convert strings such as 'A :  \n' to a list like ['A', ' ']"""
    length = len(unsplit_line)
    first_last = [unsplit_line[0], unsplit_line[length-2]]
    return first_last

def decrypt_mode():
    """The function that decrypts messages"""
    key_present = ''
    while key_present.lower() != 'y' and key_present.lower() != 'n':
        key_present = input('Do you have the correct "cipher.txt" file for decoding this message saved in the same folder as this program? (Y/N): ')
        print()
        if key_present.lower() == 'y':
            key_dict = {}
            with open('cipher.txt', 'r') as cipher_key:
                next(cipher_key)
                for line in cipher_key:
                    line = first_and_last(line)
                    #Dictionary now in this format: encrypted : decrypted
                    key_dict[line[1]] = line[0]

            usr_message = input('Enter or paste the encrypted message: ')
            decrypted_message = encrypt_decrypt(usr_message, key_dict)
            print()
            print('Decrypted Message:')
            print(decrypted_message)
            print()

        elif key_present.lower() == 'n':
            print('Please move the correct "cipher.txt" file for this message to parent folder of this program.\nBe sure to delete or move any other "cipher.txt" files from the folder.\nThis program will now close.')

        else:
            print(INPUT_ERROR)

def main():
    print('*****Substitute Cipher Maker*****')
    encrypt_or_decrypt = ''
    while encrypt_or_decrypt.lower() != 'encrypt' and encrypt_or_decrypt.lower() != 'decrypt':
        encrypt_or_decrypt = input('Enter "ENCRYPT" to encrypt a message.\nEnter "DECRYPT" to decrypt a message.\n')
        if encrypt_or_decrypt.lower() == 'encrypt':
            encrypt_mode()
        elif encrypt_or_decrypt == 'decrypt':
            decrypt_mode()
        else:
            print('INPUT ERROR: Please reply with either "ENCRYPT" or "DECRYPT"')

    print('Thank you.')
    

if __name__ == '__main__':
    main()