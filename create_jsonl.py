import json

def create_jsonl():
    key_file = input("Enter the key file name: ")
    encrypted_example_file = input("Enter the encrypted example file name: ")
    decrypted_example_file = input("Enter the decrypted example file name: ")
    encrypted_message_file = input("Enter the encrypted message file name: ")
    original_message_file = input("Enter the original message file name: ")
    output_file = input("Enter the output file name: ")

    with open(key_file, "r") as keyfile, open(encrypted_example_file, "r") as enc_ex_file, open(decrypted_example_file, "r") as dec_ex_file, open(encrypted_message_file, "r") as enc_msg_file, open(original_message_file, "r") as org_msg_file, open(output_file, "w") as outfile:
        for key_line, enc_ex_line, dec_ex_line, enc_msg_line, org_msg_line in zip(keyfile, enc_ex_file, dec_ex_file, enc_msg_file, org_msg_file):
            data = {
                "input": [
                    {
                        "role": "system",
                        "content": f"You are a helpful assistant. You will be given an encrypted mono-alphabetic substitution cipher to decrypt.\n\nThe key used to encrypt the message is '{key_line.strip()}', please respond with 'Decrypted message: ' followed by the decrypted message only."
                    },
                    {
                        "role": "user",
                        "content": f"Encrypted message: {enc_ex_line.strip()}",
                        "name": "example_user"
                    },
                    {
                        "role": "assistant",
                        "content": f"Decrypted message: {dec_ex_line.strip()}",
                        "name": "example_assistant"
                    },
                    {
                        "role": "user",
                        "content": f"Encrypted message: {enc_msg_line.strip()}"
                    }
                ],
                "ideal": org_msg_line.strip()
            }
            outfile.write(json.dumps(data) + "\n")
