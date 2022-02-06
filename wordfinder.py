"""Word Finder: finds random words from a dictionary."""

import random

class WordFinder:
    """finds random words from a document of words. words must be separated by a new line"""
    def __init__(self, filepath):
        """instantiates word_list to hold words and a filepath variable.
        calls read() to fill word_list
        prints number of words by calling length of word_list
        """
        self.word_list = []
        self.filepath = filepath
        self.read(filepath)
        print(f'{len(self.word_list)} words read')
    
    def read(self, filepath):
        """opens file via filepath provided on instantiation of WordFinder class
        appends the words found therein to the word_list
        closes the file
        returns updated word_list
        """
        file = open(self.filepath, 'r')
        for line in file:
            self.word_list.append(line.rstrip())
        file.close()
        return word_list
    
    def random(self):
        """returns a random word from word_list"""
        return random.choice(self.word_list)

class SpecialWordFinder(WordFinder):
    """finds random words from a document of words, empty lines, and comments. each item must be separated by a new line
    """
    def read(self, filepath):
        """opens file via filepath provided on instantiation of SpecialWordFinder class
        appends the words found therein to word_list only if they are not blank lines, lines of whitespace, or comments
        closes the file
        returns the updated word_list"""
        file = open(self.filepath, 'r')
        for line in file:
            if not line.startswith('#') and line.strip():
                self.word_list.append(line.rstrip())
        file.close()
        return self.word_list