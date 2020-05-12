import game
import stringDatabase

class Guess:
    """Guess class represents main function of the game. It includes the main menu for the game.
       It imports the modules game and stringDatabase. Performs the calculation function
       and checks the correctness of the guessed word and letter.
       Also performs the scoring for the game.
    """

    def calculate_letter_point(self,word):
        """Calculates the letter point for the given word using the letter frequency table.
           :param word: The word for which the points has to be calculated.
           :return letter_point: The frequency letter value for the entire word.
         """
        letter_point = 0
        letter_points_dictionary = {'a': 8.17, 'b': 1.49, 'c': 2.78, 'd': 4.25, 'e': 12.70, 'f': 2.23, 'g': 2.02, 'h': 6.09,
                                    'i': 6.97, 'j': 0.15, 'k': 0.77,
                                    'l': 4.03, 'm': 2.41, 'n': 6.75, 'o': 7.51, 'p': 1.93, 'q': 0.10, 'r': 5.99, 's': 6.33,
                                    't': 9.06, 'u': 2.76, 'v': 0.98,
                                    'w': 2.36, 'x': 0.15, 'y': 1.97, 'z': 0.07}

        for x in word:
            if x in letter_points_dictionary:
                letter_point += letter_points_dictionary[x]
        return letter_point

    def guess_by_word(self,gussed_word):
        """Validates the correctness of the guessed word.
           :param gussed_word: The word that has to be checked for the match.
           :return true or false based on the match result.
        """
        global bad_guesses
        global current_word_status
        if gussed_word == current_word:
            current_word_status = 'Guessed'
            return 'true'
        else:
            bad_guesses += 1
            print('Your Guess is wrong !')
            return 'false'

    def guess_by_letter(self,guessed_letter):
        """Validates the correctness of the guessed letter.
           :param guessed_letter: The letter for which its presence has to be checked.
           :return true or false based on the match result.
        """
        loop_count = 0
        global turnover_count
        global unguessed_word
        global missed_letter
        global guessed_points
        guessed_letter_count = 0
        if(guessed_letter in current_word):
            turnover_count += 1
            if(guessed_letter not in guessed_letter_array):
                for x in current_word:
                    if guessed_letter == x:
                        unguessed_word[loop_count] = guessed_letter
                        guessed_letter_count += 1
                    loop_count += 1
                print('You guessed ',guessed_letter_count,' letter(s) correct !')
                guessed_letter_array.append(guessed_letter)
                guessed_letter_value = GuessObj.calculate_letter_point(guessed_letter)
                guessed_points = guessed_points + (guessed_letter_value * guessed_letter_count)
                return 'true'
            else:
                print('Already guessed !')
        else:
            turnover_count += 1
            missed_letter += 1
            print('Your Guess is wrong !')
            return 'false'

    def calculate_totalscore(self):
        """Calculates the total score for the word that has been played."""
        global total_score
        global guessed_points
        global unguessed_points
        unguessed_points = total_score - guessed_points
        unguessed_points = unguessed_points/turnover_count
        for x in range(1,bad_guesses+1):
            unguessed_points = unguessed_points - ((unguessed_points*10)/100)


while('true'):

    GuessObj = Guess()
    Game = game.Game()
    StringDatabase = stringDatabase.StringDatabase()

    game_quit = 'false'
    bad_guesses = 0
    missed_letter = 0
    turnover_count = 1
    guessed_letter_array = []
    current_word_status = ''
    current_word = StringDatabase.get_a_new_word()
    unguessed_word = ['-', '-', '-', '-']
    total_score = GuessObj.calculate_letter_point(current_word)
    guessed_points = 0
    unguessed_points = 0

    while('true'):
        print('\n**** The Great Guessing Game ****')
        print('Guess:',unguessed_word[0],unguessed_word[1],unguessed_word[2],unguessed_word[3])
        print('g -> Guess the word t -> Tell the word, l -> Guess a letter, q -> Quit the game')

        player_choice = input()

        if player_choice == 'g':
            guessed_word = input('Enter the Word: ')
            guessed_result = GuessObj.guess_by_word(guessed_word)
            if(guessed_result == 'true'):
                GuessObj.calculate_totalscore()
                Game.write_data(current_word,current_word_status,bad_guesses,missed_letter,unguessed_points)
                print('Correctly guessed the word: ',current_word)
                break
            else:
                continue
        elif (player_choice == 't'):
            current_word_status = 'Gave Up'
            Game.write_data(current_word, current_word_status, bad_guesses, missed_letter,guessed_points-total_score)
            print('The word you gave up is ',current_word)
            break
        elif (player_choice == 'l'):
            guessed_letter = input('Enter the letter: ')
            guessed_result = GuessObj.guess_by_letter(guessed_letter)
            if (guessed_result == 'true'):
                continue
            else:
                continue
        elif (player_choice == 'q'):
            game_quit = 'true'
            Game.print_data()
            break
    if(game_quit == 'true'):
        break

