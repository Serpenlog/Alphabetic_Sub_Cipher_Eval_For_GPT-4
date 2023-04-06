def capitalize_text(input_file, output_file):
    with open(input_file, "r", encoding='utf-8') as infile, open(output_file, "w", encoding='utf-8') as outfile:
        for line in infile:
            outfile.write(line.upper())
