def limit_line_length(input_file, output_file, max_length=100):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            words = line.split()
            current_line = []
            current_length = 0

            for word in words:
                word_length = len(word)

                if current_length + word_length <= max_length:
                    current_line.append(word)
                    current_length += word_length + 1
                else:
                    outfile.write(' '.join(current_line) + '\n')
                    current_line = [word]
                    current_length = word_length + 1

            if current_line:
                outfile.write(' '.join(current_line) + '\n')

