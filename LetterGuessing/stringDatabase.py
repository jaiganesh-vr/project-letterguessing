import random

class StringDatabase():
    """
        StringDatabase class is responsible for all the IO operations.
    """

    def get_a_new_word(self):
        """ Reads all the 4-letter words from the file present
            in the directory and returns a word randomly.
            :return Returns a randomly fetched 4-letter word from the word list array.
        """

        wordlist = []
        file = open('four_letters.txt','r')
        words = file.read()
        wordlist = words.split()

        random_number = random.randrange(1000)
        return (wordlist[random_number])

