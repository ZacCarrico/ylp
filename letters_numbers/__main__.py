import string
import time
from playsound import playsound

def main():
    for letter in string.ascii_lowercase[1:]:
        playsound("./letters_numbers/mp3/letters/" + letter + ".mp3")
        value = input(">>>")
        if value == letter:
            playsound("./letters_numbers/mp3/responses/correct.mp3")
        else:
            incorrect_count = 0
            while value != letter:
                incorrect_count += 1
                playsound("./letters_numbers/mp3/responses/that_is_not_correct.mp3")
                if incorrect_count % 5 == 0:
                    playsound("./letters_numbers/mp3/responses/pausing.mp3")
                    time.sleep(5)
                value = input(">>>")

if __name__ == '__main__':
    main()
