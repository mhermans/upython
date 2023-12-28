"""CircuitPython Essentials Audio Out MP3 Example"""
import board
import audioio
import audiomp3 

# The listed mp3files will be played in order
mp3files = ["begins.mp3", "xfiles.mp3"]

# You have to specify some mp3 file when creating the decoder
mp3 = open(mp3files[0], "rb")
decoder = audiomp3.MP3Decoder(mp3)
audio = audioio.AudioOut(board.A0)

while True:
    for filename in mp3files:
        # Updating the .file property of the existing decoder
        # helps avoid running out of memory (MemoryError exception)
        decoder.file = open(filename, "rb")
        audio.play(decoder)
        print("playing", filename)

        # This allows you to do other things while the audio plays!
        while audio.playing:
            pass
