def group_words_by_length():
    """Get words from user input until '*' is entered, then group by length"""
    grouped = {}

    print("Enter words (enter '*' to stop):")

    while True:
        word = input("Word: ").strip()

        # Stop condition with asterisk
        if word == '*':
            break

        # Only process non-empty words
        if word:
            length = len(word)
            grouped.setdefault(length, []).append(word)

    return grouped


# Run the program
result = group_words_by_length()

print("\nDictionary grouping words by length:")
print(result)

print("\nDetailed breakdown:")
for length, words in sorted(result.items()):
    print(f"Length {length}: {', '.join(words)}")