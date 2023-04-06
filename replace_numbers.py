def replace_numbers(input_file, output_file):
    import inflect
    p = inflect.engine()

    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        for line in infile:
            replaced_line = ' '.join([p.number_to_words(word) if word.isdigit() else word for word in line.split()])
            outfile.write(replaced_line + '\n')
