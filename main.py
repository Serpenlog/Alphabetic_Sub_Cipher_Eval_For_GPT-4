import sys
from capitalize import capitalize_text
from remove_empty_lines import remove_empty_lines
from replace_numbers import replace_numbers
from generate_permutations import generate_permutations
from encrypt_document import encrypt_document
from count_lines import count_lines
from decrypt_document import decrypt_document
from repeat_sentence import repeat_sentence
from create_jsonl import create_jsonl
from generate_data import generate_data
from limit_line_length import limit_line_length

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
    elif operation == "count_lines":
        input_file = sys.argv[2]
        print(count_lines(input_file))
    elif operation == "decrypt_document":
        decrypt_document()
    elif operation == "repeat_sentence":
        n = int(sys.argv[2])
        output_file = sys.argv[3]
        repeat_sentence(n, output_file)
    elif operation == "create_jsonl":
        create_jsonl()
    elif operation == "generate_data":
        generate_data()
    elif operation == "limit_line_length":
        input_file = sys.argv[2]
        output_file = sys.argv[3]
        limit_line_length(input_file, output_file)
    else:
        print("Invalid operation")

if __name__ == "__main__":
    main()

