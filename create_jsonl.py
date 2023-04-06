import json

def create_jsonl(key_file, encrypted_example_file, decrypted_example_file, encrypted_message_file, original_message_file, output_file):
    with open(key_file, "r", encoding='utf-8') as keyfile, open(encrypted_example_file, "r", encoding='utf-8') as enc_ex_file, open(decrypted_example_file, "r", encoding='utf-8') as dec_ex_file, open(encrypted_message_file, "r", encoding='utf-8') as enc_msg_file, open(original_message_file, "r", encoding='utf-8') as org_msg_file, open(output_file, "w", encoding='utf-8') as outfile:
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
                "ideal": f"Decrypted message: {org_msg_line.strip()}"
            }
            json_line = json.dumps(data, ensure_ascii=False) # ensure_ascii=False to prevent unicode escaping
            outfile.write(json_line + "\n")
