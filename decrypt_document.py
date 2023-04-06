def decrypt_document():
    key_file = input("Enter the key file name: ")
    encrypted_file = input("Enter the encrypted file name: ")
    output_file = input("Enter the output file name: ")

    with open(key_file, "r", encoding='utf-8') as keyfile, open(encrypted_file, "r", encoding='utf-8') as infile, open(output_file, "w", encoding='utf-8') as outfile:
        for key_line, encrypted_line in zip(keyfile, infile):
            key = key_line.strip()
            substitution = {key[i]: chr(ord('A') + i) for i in range(26)}
            decrypted_line = ''.join([substitution.get(char, char) for char in encrypted_line.upper()])
            outfile.write(decrypted_line)
