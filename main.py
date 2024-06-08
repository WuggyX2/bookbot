"""
Boot.dev book bot project
"""


def main():
    """Main function for this app"""
    with open("./books/frankenstein.txt", "r", encoding="UTF-8") as f:
        text = f.read()
        print(text)



main()
