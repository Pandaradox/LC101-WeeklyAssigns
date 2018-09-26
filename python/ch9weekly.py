
# ##################################################Chapter 9 Weekly Assignment
# Function to scan a string for 'e' and return a percentage of the string that's 'e'

import string


def analyze_text(text):

    es = 0
    count = 0
    for char in text:
        if char in string.ascii_letters:
            count += 1
            if (char.lower() == 'e'):
                es += 1
    return("The text contains {length} alphabetic characters, of which {totalE} ({percentE}%) are 'e'.".format(length=count, totalE=es, percentE=((es / count) * 100)))


def main():
    text1 = "Eeeee"
    text2 = "Blueberries are tasteee!"
    text3 = "Wright's book, Gadsby, contains a total of 0 of that most common symbol ;)"
    # Tests 4-6: solutions using str.format should pass these
    text4 = "Eeeee"
    text5 = "Blueberries are tasteee!"
    text6 = "Wright's book, Gadsby, contains a total of 0 of that most common symbol ;)"
    print(analyze_text(text1))
    print(analyze_text(text2))
    print(analyze_text(text3))

    # answer1 = "The text contains 5 alphabetic characters, of which 5 (100.0%) are 'e'."
    # answer2 = "The text contains 21 alphabetic characters, of which 7 (33.3333333333%) are 'e'."
    # answer3 = "The text contains 55 alphabetic characters, of which 0 (0.0%) are 'e'."


if __name__ == "__main__":
    main()
