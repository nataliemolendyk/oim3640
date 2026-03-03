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


def main():
    """Load words, set up puzzle, print results."""
    letters = input("Enter the letters: ")
    center = input("Enter the center letter: ")
    word_list = open_words('data/words.txt')

    valid_words = find_words(word_list, letters, center)
    for word in valid_words:
        print(word)
            