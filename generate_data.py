import os
from replace_numbers import replace_numbers
from remove_empty_lines import remove_empty_lines
from capitalize import capitalize_text
from generate_permutations import generate_permutations
from encrypt_document import encrypt_document
from repeat_sentence import repeat_sentence
from create_jsonl import create_jsonl
from count_lines import count_lines

def generate_data():
    init_file = input("Enter the initial file name: ")

    # Phase 1: Replace numbers
    phase1_file = "phase1.txt"
    replace_numbers(init_file, phase1_file)

    # Phase 2: Remove empty lines
    phase2_file = "phase2.txt"
    remove_empty_lines(phase1_file, phase2_file)

    # Phase 3: Capitalize
    input_file = "input.txt"
    capitalize_text(phase2_file, input_file)

    # Phase 4: Generate key file
    n = count_lines(input_file)
    key_file = "key.txt"
    generate_permutations(n, key_file)

    # Phase 5: Generate input examples
    input_ex_file = "input_ex.txt"
    repeat_sentence(n, input_ex_file)

    # Phase 6: Encrypt messages
    encrypted_msg_file = "encrypted_msg.txt"
    encrypt_document(key_file, input_file, encrypted_msg_file)

    # Phase 7: Encrypt input examples
    encrypted_ex_file = "encrypted_ex.txt"
    encrypt_document(key_file, input_ex_file, encrypted_ex_file)

    # Phase 8: Create JSONL
    data_file = "data.txt"
    create_jsonl(key_file, encrypted_ex_file, input_ex_file, encrypted_msg_file, input_file, data_file)

    # Call delete_files() function to clean up intermediate files
    delete_files("phase1.txt", "phase2.txt", "input.txt", "key.txt", "input_ex.txt", "encrypted_msg.txt", "encrypted_ex.txt")

def delete_files(*files):
    for file in files:
        try:
            os.remove(file)
        except FileNotFoundError:
            print(f"File {file} not found.")
