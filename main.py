"""
Boot.dev book bot project
"""
import sys
from stats import count_characters, count_words


def main():
    """Main function for this app"""

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    with open(book_path, "r", encoding="UTF-8") as f:
        text = f.read()
        word_count = count_words(text)
        character_count = count_characters(text)
        print_report(character_count=character_count, word_count=word_count, book_path=book_path)


def print_report(character_count: dict[str, int], word_count: int, book_path: str):
    """
    Function that prints a report message for the given dictionary of characters and
    their counts and the total word count.

    Args:
        character_count: dictionary containg characters and number of occurances
        word_count: total number of words in a document
    """

    dict_list = dict_to_dict_list(character_count)
    dict_list.sort(reverse=True, key=sort_on_count)

    print(f"""============ BOOKBOT ============
Analyzing book found at {book_path}...
----------- Word Count ----------
Found {word_count} total words
--------- Character Count -------""")

    for current_dict in dict_list:
        print(
            f"{current_dict["char"]}: {current_dict["count"]}"
        )

    print("============= END ===============")


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
