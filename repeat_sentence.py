def repeat_sentence():
    n = int(input("Enter the number of repetitions: "))
    output_file = input("Enter the output file name: ")

    sentence = "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG"

    with open(output_file, "w") as outfile:
        for _ in range(n):
            outfile.write(sentence + "\n")
