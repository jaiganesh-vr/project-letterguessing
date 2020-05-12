game_count = 1

record_game = []
record_word = []
record_word_status = []
record_bad_guesses = []
record_missed_letters = []
record_total_score = []

class Game:
    """Game class maintains the information about the games. All information are stored in arrays.
       Offers write and read functions.
    """


    def write_data(self,word,wordstatus,badguess,missedletter,totalscore):
        """ Writes the instances of game data in an array for the future reference.
            :param word: Currently played word in the game.
            :param wordstatus: Guessed or Gave Up status of the word.
            :param badguess: Number of bad guessed the player made while guessing this word.
            :param missedletter: Number of letters missed by the player while guessing this word.
            :param totalscore: Total score the player obtained for this word.
        """
        global game_count
        global record_game
        global record_word
        global record_bad_guesses
        global record_missed_letters
        global record_total_score
        global record_word_status

        record_game.append(game_count)
        record_word.append(word)
        record_word_status.append(wordstatus)
        record_bad_guesses.append(badguess)
        record_missed_letters.append(missedletter)
        record_total_score.append(totalscore)

        game_count +=1


    def print_data(self):
        """Print the results of words played so far in the game. """
        total_score = 0.0

        title_game = 'Game'
        title_word = 'Word'
        title_word_status = 'Word Status'
        title_bad_guesses = 'Bad Guesses'
        title_missed_letters = 'Missed Letters'
        title_total_score = 'Total score'

        if not record_word:
            print("No words played.")
        else:
            print('%-5s %-10s  %-12s  %-5s  %-5s  %s' %(title_game,title_word, title_word_status, title_bad_guesses, title_missed_letters,title_total_score))
            print('----  ----        ------------  -----------  --------------  -----------')
            for x in range(len(record_word)):
                print('%-5s %-10s  %-13s  %-11s  %-13s  %.2f'%(record_game[x],record_word[x],record_word_status[x],record_bad_guesses[x],record_missed_letters[x],record_total_score[x]))

            for x in range(len(record_total_score)):
                total_score = total_score + record_total_score[x]

            print('\nFinal Score: %.2f' %total_score)


