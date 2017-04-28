import BeatSynthUtility
import librosa
import librosa.display
import IPython.display
import numpy as np

import matplotlib.pyplot as plt
import matplotlib.style as ms
beat_names = ["Playboi Cari 1", "Playboi Carti 2"]
beat_paths = ["Beats/beat1.mp3", "Beats/beat2.mp3"]

beats = BeatSynthUtility.load_sound_files(beat_paths)
print(beats[1][0].shape)
print(beats[0][0].shape)

#BeatSynthUtility.plot_specgram(beat_names, beats)
#BeatSynthUtility.plot_waves(beat_names, beats)
#BeatSynthUtility.plot_log_power_specgram(beat_names, beats)

plt.figure()
librosa.display.waveplot(y=beats[1][0], sr=beats[1][1])
librosa.display.waveplot(y=beats[0][0], sr=beats[0][1])

plt.show()
