def count_lines(input_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()
        return len(lines)
