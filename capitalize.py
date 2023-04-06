def capitalize_text():
    input_file = input("Enter the input file name: ")
    output_file = input("Enter the output file name: ")

    with open(input_file, "r") as infile, open(output_file, "w") as outfile:
        for line in infile:
            outfile.write(line.upper())
