def count_lines():
    input_file = input("Enter the input file name: ")

    with open(input_file, "r") as infile:
        line_count = sum(1 for line in infile)
        print(f"The file has {line_count} lines.")
