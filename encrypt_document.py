def encrypt_document(key_file, input_file, output_file):
    with open(key_file, "r") as keyfile, open(input_file, "r") as infile, open(output_file, "w") as outfile:
        for key_line, input_line in zip(keyfile, infile):
            key = key_line.strip()
            substitution = {chr(ord('A') + i): key[i] for i in range(26)}

            encrypted_line = ''.join([substitution.get(char, char) for char in input_line])
            outfile.write(encrypted_line)
