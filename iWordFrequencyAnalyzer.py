import string   # using string to prevent localisation issues in string.punctuation
import re
from typing import List, Dict
from collections import Counter


class iWordFrequencyAnalyzer:
    """
    iWordFrequencyAnalyzer is a tool to analyse an input text for the frequency
    of words.

    in this context, a word is a set of characters a z and A Z. Words are case
    insensitive. This, this and THiS are treated as being equal
    input text contains 1 or more words, separated by separator characters. by
    default, the string.punctuation and string.whitespace constants will be used
    as separators
    while processing this input text, if a character is not recognized as either
    a z, A Z or a separator character, a CharacterError is raised

    e.g. "python" is a valid word, but "python3" is not, because 3 is not in a zA Z
    :param separator: the list of separators. Default is all punctuation and whitespace
    :type separator: str

    """
    def __init__(self, separator: string = None) -> None:
        if separator:
            self.sep = separator + string.whitespace
        else:
            self.sep = string.punctuation + string.whitespace
            # nb. in C locale this defaults to
            # '!"#$%&\'()*+, ./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c'

        self.validword_regex = re.compile('^['+ string.ascii_letters +']+$')
        self.split_regex = re.compile('[' + re.escape(self.sep) + ']')

    def CalculateHighestFrequency(self, input_text: str) -> int:
        """
        Return the highest frequency in the input text.
        (several words might actually have this frequency)

        :param input_text: the text to analyze
        :type input_text: str

        :returns: the highest frequency in the text
        :rtype: int
        """
        wordFreq = self._WordSplitAndCount(input_text)
        if len(wordFreq) == 0: #default to 0 for empty input
            return 0
        return max(*wordFreq.values())


    def CalculateFrequencyForWord (self, input_text: str, word: str) -> int:
        """
        Return the frequency for the word in input_text

        :param input_text: the text to analyze
        :type input_text: str

        :param word: the word to find in the input_text
        :type word: str

        :returns: the frequency of the word in the text
        :rtype: int
        """
        return self._WordSplitAndCount(input_text)[word]

    def CalculateMostFrequentNWords (self, input_text: str, n: int ) -> List[str]:
        """
        Find all the words that occur exactly a certain number of times in the input text

        :param input_text: the text to analyze
        :type input_text: str

        :param n: the frequency to find
        :type n: int

        :returns: a list of all the words with a certain frequency
        :rtype: list[int]
        """

        # translate the dict from _WordSplitAndCount to a dict with frequency : word list
        freqNwords = {}
        for k , v in self._WordSplitAndCount(input_text).items():
            if v not in freqNwords.keys():
                freqNwords[v] = []
            freqNwords[v].append(k)

        if n not in freqNwords.keys():
            return []

        return freqNwords[n]

    def _WordSplitAndCount(self, input_text:str) -> Dict[str, int]:
        """
        method to split the input text and return a Dict with the frequency of
        each word
        e.g. _WordSplitAndCount("The sun shines over the lake") returns

        {"the": 2, "sun": 1, "shines": 1, "over": 1, "lake": 1}

        :param input_text: the text to analyze
        :type input_text: str

        :returns: a dict of list of all the words with a certain frequency
        :rtype: list[int]

        """
        input_text = input_text.lower()                 #  convert to lower case
        AllWords = self.split_regex.split(input_text)   # split the string using the separators
        AllWords = list(filter(None, AllWords))         # remove empty strings

        # check is all words are valid
        for word in set(AllWords):
            if not self.validword_regex.findall(word):
                raise CharacterError(word, 'contains invalid characters')

        return Counter(AllWords)


class CharacterError(ValueError):
    """Raised when a character is not recognized as either a zA Z or a separator"""
    pass


if __name__=="__main__":
    lorem = r"""
            Lorem ipsum dolor sit amet, consectetur adipiscing elit,
            sed do eiusmod tempor incididunt ut labore et dolore magna
            aliqua. Ut enim ad minim veniam, quis nostrud exercitation
            ullamco laboris nisi ut aliquip ex ea commodo consequat.
            Duis aute irure dolor in reprehenderit in voluptate velit
            esse cillum dolore eu fugiat nulla pariatur. Excepteur sint
            occaecat cupidatat non proident, sunt in culpa qui officia
            deserunt mollit anim id est laborum."
            """

    analyzer = iWordFrequencyAnalyzer()
    print("result for text ")
    print(lorum)
    print('max frequency:     ', analyzer.CalculateHighestFrequency(lorem))
    print('frequency of lorem:', analyzer.CalculateFrequencyForWord(lorem, 'lorem'))
    print('most frequent words:',analyzer.CalculateMostFrequentNWords(lorem, 3))
