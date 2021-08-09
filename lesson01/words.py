#!python words.py http://sixty-north.com/c/t.txt
"""Retrieve and print words from a URL.

Usage:
python3 words.py <URL>

"""
import sys

from urllib.request import urlopen

def fetch_words(url):
    """Fetch a list of words from a URL.

    Args:
        url:The URL of a UTF-8 text document.

    Returns:
        A list of strings containing the words from
        the document.
    """

    with urlopen(url) as story:
        story_words=[]
        for line in story:
            line_words=line.decode("utf-8").split(" ")
            for word in line_words:
                print(word)
                story_words.append(word)
    return story_words



def print_items(items):
    """Print item per line

    Args:
        items:An iterable series of printable items.
    """
    for item in items:
        print(item)


def main(url):
    """Print each word from a text document from at a URL.
    
    Args:
        url: The URL of a UTF-8 text document.
    """
    words=fetch_words(url) #"http://sixty-north.com/c/t.txt"
    print_items(words)


if __name__=="__main__":
    main(sys.argv[1]) # sys.argv[0] is the module filename
   