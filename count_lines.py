def count_lines(input_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        return len(lines)
