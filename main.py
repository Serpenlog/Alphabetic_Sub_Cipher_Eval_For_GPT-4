import sys
from capitalize import capitalize_text
from remove_empty_lines import remove_empty_lines
from replace_numbers import replace_numbers
from generate_permutations import generate_permutations
from encrypt_document import encrypt_document
from decrypt_document import decrypt_document
from count_lines import count_lines
from repeat_sentence import repeat_sentence
from create_jsonl import create_jsonl

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py [operation]")
        sys.exit(1)

    operation = sys.argv[1].lower()

    if operation == "capitalize":
        capitalize_text()
    elif operation == "remove_empty_lines":
        remove_empty_lines()
    elif operation == "replace_numbers":
        replace_numbers()
    elif operation == "generate_permutations":
        generate_permutations()
    elif operation == "encrypt_document":
        encrypt_document()
    elif operation == "decrypt_document":
        decrypt_document()
    elif operation == "count_lines":
        count_lines()
    elif operation == "repeat_sentence":
        repeat_sentence()
    elif operation == "create_jsonl":
        create_jsonl()
    else:
        print("Invalid operation")

if __name__ == "__main__":
    main()

