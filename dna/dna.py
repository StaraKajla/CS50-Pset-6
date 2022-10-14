import csv
import sys
from collections import Counter


def main():

    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        sys.exit("Usage: python dna.py data.csv sequence.txt")

    # data.csv
    data = sys.argv[1]
    # sequence.txt
    seq = sys.argv[2]

    # TODO: Read database file into a variable

    # DNA database
    dna_db = []
    with open(data) as file:
        reader = csv.DictReader(file)
        for row in reader:
            dna_db.append(row)

    # TODO: Read DNA sequence file into a variable
    dna_seq = ""
    with open(seq, 'r') as file:
        dna_seq = file.read()

    # TODO: Find longest match of each STR in DNA sequence

    #  Figure out DNA STR(Short Tandem Repeat) keys
    match_seq = {}
    # Find database keys and calculate maximum
    keys = dna_db[0].keys()
    for i in keys:
        match_seq[i] = str(longest_match(dna_seq, i))

    # TODO: Check database for matching profiles
    match = []
    for i in range(len(dna_db)):
        for j in keys:
            if j == 'name':
                continue
            elif (match_seq.get(j) in dna_db[i].get(j)):
                match.append(dna_db[i].get('name'))
            else:
                break

    result_dna = "No match"
    all_matches = Counter(match)
    for i in all_matches.keys():
        if (all_matches[i]) == len(keys) - 1:
            result_dna = i
            break

    print(result_dna)
    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


if __name__ == "__main__":
    main()
