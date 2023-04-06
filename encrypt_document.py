def encrypt_document():
    key_file = input("Enter the key file name: ")
    input_file = input("Enter the input file name: ")
    output_file = input("Enter the output file name: ")

    with open(key_file, "r") as keyfile, open(input_file, "r") as infile, open(output_file, "w") as outfile:
        for key_line, input_line in zip(keyfile, infile):
            key = key_line.strip()
            substitution = {chr(ord('a') + i): key[i] for i in range(26)}
            encrypted_line = ''.join([substitution.get(char, char) for char in input_line.lower()])
            outfile.write(encrypted_line)
