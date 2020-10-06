
"""Generate Markov text from text files."""
from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    contents = open(file_path)
    contents = contents.read()

    return contents
    #print(contents)


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """
    # your code goes here
    chains = {}

    list_of_words = text_string.split()

    list_of_words.append(None)

    for x in range(len(list_of_words) - 2):
        key = (list_of_words[x], list_of_words[x + 1])
        value = list_of_words[x + 2]
        #print(key)
        
        if key not in chains:
            chains[key] = []
            
        chains[key].append(value)
        
    print(chains)
    return chains

#  chains = {}
#     list_of_words = text_string.split()
#     print(list_of_words)
#     #list_of_words.append(None)
#     for x in range(len(list_of_words) - 2):
#         key = (list_of_words[x], list_of_words[x + 1])
#         value = list_of_words[x + 2]
# 
#         if key not in chains:
#             chains[key] = value
#         else key in chains:
#             newValue = chains[key]
#             newValue.append(value)
#             chains[key] = newValue
def make_text(chains):
    """Return text from chains."""

    key = choice(list(chains.keys()))
    words = [key[0], key[1]]
    word = choice(chains[key])

    while word is not None:
        key = (key[1], word)
        words.append(word)
        word = choice(chains[key])
    
    #print(words,word,key)

    # your code goes here

    return ' '.join(words)


input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
