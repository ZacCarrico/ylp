gtts (google text to speech) was unusably slow for this project. Specifically gtts object creation took > 1 min for one 
liners of text.

pyttsx3 works offline, but sounds absurdly robotic
need to first install espeak:
sudo apt-get update && sudo apt-get install espeak

going back to gtts and will let it run overnight

four mp3, both pygame and vlc threw errors. playsound worked
