import cs50


def main():
    cents = get_cents()

    quarters = calculate_quarters(cents)
    cents -= quarters * 25

    dimes = calculate_dimes(cents)
    cents -= dimes * 10

    nickels = calculate_nickels(cents)
    cents -= nickels * 5

    pennies = calculate_pennies(cents)
    cents -= pennies * 1

    total_coins = quarters + dimes + nickels + pennies

    print(total_coins)


def get_cents():
    amount = -1
    while amount < 0:
        amount = cs50.get_float("Cents: ")
    return amount * 100


def calculate_quarters(cents):
    return int(cents / 25)


def calculate_dimes(cents):
    return int(cents / 10)


def calculate_nickels(cents):
    return int(cents / 5)


def calculate_pennies(cents):
    return int(cents / 1)


if __name__ == "__main__":
    main()