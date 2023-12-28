# MP3 in mixer example working
import board
import audioio
import audiomp3
import audiomixer

#  ---Set Volume Max Here---
VOLUME_MULT = 0.9  # 1 = full volume, 0.1 is very quiet, 0 is muted

print('setup')

speaker = audioio.AudioOut(board.A0)


# You have to specify some mp3 file when creating the decoder
sample0 = audiomp3.MP3Decoder(open("bgmheal.mp3", "rb"))
sample1 = audiomp3.MP3Decoder(open("shoot.mp3", "rb"))

print(sample0.sample_rate)
mixer = audiomixer.Mixer(channel_count=sample0.channel_count, 
    buffer_size=2304, sample_rate=sample0.sample_rate)

speaker.play(mixer)
mixer.voice[0].play(sample0, loop=True)
mixer.voice[0].level = 0.3 * VOLUME_MULT
mixer.voice[1].level = 0.7 * VOLUME_MULT

print('setup finished')

while True:
    pass
