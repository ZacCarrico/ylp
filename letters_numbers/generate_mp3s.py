from gtts import gTTS
def generate_mp3s():
    # for letter in string.ascii_lowercase:
    #     tts = gTTS("type the letter " + letter, lang='en', slow=False)
    #     tts.save(letter + ".mp3")
    # for number in range(10):
    #     tts = gTTS("type the number " + str(number), lang='en', slow=False)
    #     tts.save(str(number) + ".mp3")
    # tts = gTTS("correct", lang='en', slow=False)
    # tts.save("correct.mp3")
    tts = gTTS("Type a letter if you want to play the letter game or "
               "type a number if you want to play the number game", lang='en', slow=False)
    tts.save("choose_char.mp3")

generate_mp3s()