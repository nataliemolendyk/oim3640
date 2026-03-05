def uses_only(word, letters):
    """Does word use only the allowed letters?"""
    for letter in word:
        if letter not in letters:
            return False
    return True

def must_use(word, center):
    """Does word include the center letter?"""
    for letter in word:
        if letter == center:
            return True
    return False

def is_valid(word, letters, center):
    """Is the word valid?"""
    return uses_only(word, letters) and must_use(word, center) and len(word) >= 4

def open_words():
    """Load words from the data file."""
    with open('data/words.txt') as file:
        return [line.strip().lower() for line in file]
    
def find_words(word_list, letters, center):
    """Find all valid words in the word list."""
    valid_words = []
    for word in word_list:
        if is_valid(word, letters, center):
            valid_words.append(word)
    return valid_words

def main():
    """Load words, set up puzzle, print results."""
    letters = input("Enter the letters: ").lower()
    center = input("Enter the center letter: ").lower()
    word_list = open_words()

    valid_words = find_words(word_list, letters, center)
    for word in valid_words:
        print(word)

if __name__ == "__main__":
    main()         