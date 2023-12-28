# basic wav sample working on Feather M4 Express
import board
import audioio
import audiocore

data = open("StreetChicken.wav", "rb")
wav = audiocore.WaveFile(data)
a = audioio.AudioOut(board.A0)

print("playing")
a.play(wav)
while a.playing:
  pass
