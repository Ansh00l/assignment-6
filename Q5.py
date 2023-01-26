def sort_words(sequence):
    words = sequence.split("-")
    words.sort()
    return "-".join(words)

sequence = input("Enter a hyphen-separated sequence of words: ")
sorted_sequence = sort_words(sequence)
print("Sorted sequence:", sorted_sequence)
