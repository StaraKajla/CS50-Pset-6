import cs50
import re


def main():

    text = cs50.get_string("Text: ")

    letters = count_letters(text)
    words = count_words(text)
    sentences = count_sentences(text)

    print("letters: ", letters)
    print("words: ", words)
    print("sentences: ", sentences)

    L = letters / words * 100
    S = sentences / words * 100

    # CLI Index
    CLI = (0.0588 * L) - (0.296 * S) - 15.8
    grade = round(CLI)

    if (grade < 1):
        print("Before Grade 1")
    elif (grade > 16):
        print("Grade 16+")
    else:
        print(f"Grade {grade}")


def count_letters(text):
    find_letters = re.findall("[a-zA-Z0-9]", text)
    return len(find_letters)


def count_words(text):
    find_word = re.findall("[\s]", text)
    return (len(find_word) + 1)


def count_sentences(text):
    find_sentence = re.findall("[!?.]", text)
    return len(find_sentence)


if __name__ == "__main__":
    main()