import inflect

def replace_numbers():
    input_file = input("Enter the input file name: ")
    output_file = input("Enter the output file name: ")
    p = inflect.engine()

    with open(input_file, "r") as infile, open(output_file, "w") as outfile:
        for line in infile:
            words = line.split()
            new_line = []
            for word in words:
                if word.isdigit():
                    word = p.number_to_words(word)
                new_line.append(word)
            outfile.write(" ".join(new_line) + "\n")
