def repeat_sentence(n, output_file):
    sentence = "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG"
    with open(output_file, "w", encoding='utf-8') as outfile:
        for _ in range(n):
            outfile.write(sentence + "\n")
