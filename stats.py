def count_words(text: str) -> int:
    """
    Function that counts the number of words in a given text

    Args:
        text: text to count words from

    Returns: number of words in the text

    """
    words = text.split()
    return len(words)


def count_characters(text: str) -> dict[str, int]:
    """
    Function that counts the number of characters in a given text
    and returns a dictionary with the charactes as keys and the number of occurences as values

    Args:
        text: text to count characters from

    Returns: dictionary with the characters as keys and the number of occurences as values

    """
    lowered_text = text.lower()
    characters = {}
    for char in lowered_text:
        if char.isalpha():
            if char in characters:
                characters[char] += 1
            else:
                characters[char] = 1

    return characters
