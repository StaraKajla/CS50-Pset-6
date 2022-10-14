import cs50
import re


def main():
    card = 0
    while card <= 0:
        card = cs50.get_int("Card number: ")
    #Check validity
    if check_validity(card) == True:
        print_brand(card)
    else:
        print("INVALID")


def check_validity(card):

    #check string of card number for 0-9 (only specific lengths)
    string_card = str(card)
    valid = re.findall("^[0-9]{13}$|^[0-9]{15,16}$", string_card)

    #if card has 13,15,16 digits: valid.regex will return list[numbers...] else empty list[]
    if (valid != [] and checksum(card) == True):
        return True
    else:
        return False


def checksum(card):
    #idx                         <--
    #4 0 0 3 6 0 0 0 0 0 0 0 0 0 1 4
    rev_card_no = str(card)[::-1]
    index = 0
    sum = 0
    for i in rev_card_no:
        if (index % 2 == 0):
            sum += int(i) % 10
        else:
            digit = 2 * (int(i) % 10)
            sum += digit // 10 + digit % 10
        index += 1
    return (sum % 10) == 0


def print_brand(card):
    if ((card >= 34e13 and card < 35e13) or (card >= 37e13 and card < 38e13)):
        print("AMEX")
    elif (card >= 51e14 and card <= 56e14):
        print("MASTERCARD")
    elif ((card >= 4e12 and card < 5e12) or (card >= 4e15 and card < 5e15)):
        print("VISA")
    else:
        print("INVALID")


if __name__ == "__main__":
    main()