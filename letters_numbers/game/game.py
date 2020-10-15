import random
import string
import time
from playsound import playsound

class Game:
    def __init__(self):
        self.game_opts = {
            'letters': [_ for _ in string.ascii_lowercase],
            'numbers': [str(_) for _ in range(10)]
        }
        random.shuffle(self.game_opts['letters'])
        random.shuffle(self.game_opts['numbers'])

    def choose_char_type(self):
        playsound("./letters_numbers/mp3/choose_char.mp3")
        value = input(">>>")
        if value in self.game_opts['letters']:
            self.typing_game('letters')
        elif value in self.game_opts['numbers']:
            self.typing_game('numbers')

    def typing_game(self, game_type):

        for char in self.game_opts[game_type]:
            playsound(f"./letters_numbers/mp3/{game_type}/{char}.mp3")
            value = input(">>>")
            if value != char:
                incorrect_count = 0
                while value != char:
                    incorrect_count += 1
                    playsound("./letters_numbers/mp3/responses/that_is_not_correct.mp3")
                    if incorrect_count % 5 == 0:
                        playsound("./letters_numbers/mp3/responses/pausing.mp3")
                        time.sleep(5)
                    value = input(">>>")
            playsound("./letters_numbers/mp3/responses/correct.mp3")
            playsound("./letters_numbers/mp3/responses/congratulations.mp3")