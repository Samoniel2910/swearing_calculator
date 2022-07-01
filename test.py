from pygame import mixer
from time import sleep

mixer.init()
mixer.music.load("not code/sound.mp3")

mixer.music.play()
sleep(1)
mixer.music.stop()