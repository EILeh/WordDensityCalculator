"""
Word density calculator

Program is a word density calculator that reads a piece of text from the user
and then prints how many times each of the words appears in the text. The words
in the list are printed in alphabetic order and all the letters are in
lower-case. A string separated from other strings with empty characters is
considered a word (separated from the text using a split method).

Writer of the program: EILeh

"""

def main():

    text = {}
    is_input_not_empty = True

    print("Enter rows of text for word counting. Empty row to quit.")

    list_of_words = []

    while is_input_not_empty:
        user_input = input("")

        if user_input == "":
            is_input_not_empty = False

        list_of_words = user_input.split()

        # Goes through every word in the list_of_words.
        for word in list_of_words:
            # If word is not in dictionary text, this is the first time the
            # word appears.
            lowercase_word = word.lower()
            if lowercase_word not in text:
                # New key-value pair.
                text[lowercase_word] = 1

            # If word is in dictionary text, its' value is grown by one.
            else:
                text[lowercase_word] += 1

    # To get the word and how many times it appears in the input text,
    # the dictionary text is gone through in for loop where key is the word
    # and value is a number that contains how many times a word appear in the
    # text.
    for key, value in sorted(text.items()):
        print(f"{key} : {value} times")

if __name__ == "__main__":
    main()