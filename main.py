"""
Boot.dev book bot project
"""


def main():
    """Main function for this app"""
    with open("./books/frankenstein.txt", "r", encoding="UTF-8") as f:
        text = f.read()
        word_count = count_words(text)
        character_count = count_characters(text)
        print_report(character_count=character_count, word_count=word_count)


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


def print_report(character_count: dict[str, int], word_count: int):
    """
    Function that prints a report message for the given dictionary of characters and
    their counts and the total word count.

    Args:
        character_count: dictionary containg characters and number of occurances
        word_count: total number of words in a document
    """

    dict_list = dict_to_dict_list(character_count)
    dict_list.sort(reverse=True, key=sort_on_count)

    print("--- Begin report of books/frankenstein.txt --- \n")
    print(f"{word_count} words found in the document\n")

    for current_dict in dict_list:
        print(
            f"The '{current_dict["char"]}' character was found {current_dict["count"]} times"
        )

    print("--- End report ---")


def dict_to_dict_list(data: dict[str, int]) -> list[dict[str, str | int]]:
    """
    Helper function that transforms a given dictionary to a list of dictionaries that have
    a char and a count propertry

    Args:
        data: dictionary to be transformed

    Returns: a list of dictionaries

    """
    return_data = []

    for key, value in data.items():
        return_data.append({"char": key, "count": value})

    return return_data


def sort_on_count(data: dict[str, str | int]):
    """
    Helper function that can be given as an argument for the key param in the sort function
    list of dictionaries being sorted have to have a "count" property

    Args:
        data: dictionary used being sorted.

    Returns:

    """
    return data["count"]


main()
