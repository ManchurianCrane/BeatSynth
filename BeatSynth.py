


import BeatSynthUtility
import librosa
import librosa.display
import IPython.display
import numpy as np
import array
import os
import tensorflow as tf

import pickle
import matplotlib.pyplot as plt
import matplotlib.style as ms

from audio_signal_processing import AudioSignalProcessiong

beat_names = ["Playboi Carti 1", "Playboi Carti 2"]
beat_paths = ["Beats/beat1.mp3", "Beats/beat2.mp3"]


retrieveBeat = {
    "Playboi Carti 1": "Beats/beat1.mp3",
    "Playboi Carti 2": "Beats/beat2.mp3",
}

from pydub import AudioSegment
from pydub.utils import get_array_type, get_encoder_name, get_frame_width, get_min_max_value, get_player_name, get_prober_name


SoundProcessing = AudioSignalProcessiong()

def getAudioData(name):
    '''
    sound._data is a bytestring. I'm not sure what input Mpm expects, but you may need to convert the bytestring to an array like so:
    '''
    sound = AudioSegment.from_mp3(retrieveBeat[name])

    bytes_per_sample = sound.sample_width   #1 means 8 bit, 2 meaans 16 bit
    print("BYTES PER SAMPLE: ")
    print(bytes_per_sample)

    bit_depth = sound.sample_width * 8

    frame_rate = sound.frame_rate
    print("FRAME RATE IS: " + str(frame_rate))

    number_of_frames_in_sound = sound.frame_count()
    number_of_frames_in_sound_200ms = sound.frame_count(ms=200)

    print("NUMBER OF FRAMES IS " + str(number_of_frames_in_sound))
    print("NUMBER OF FRAMES IN SOUND PER 200 MS: " + str(number_of_frames_in_sound_200ms))

    array_type = get_array_type(bit_depth)
    print(array_type)
    numeric_array = array.array(array_type, sound.raw_data)
    channel_count = sound.channels
    print("Number of channels in the audio is: ")
    print(channel_count)


    #audio get array of samples

    samples = sound.get_array_of_samples()
    print("SAMPLES ARE")
    print(len(samples))

    left_sound, right_sound = sound.split_to_mono()     #Split it
    print("FRAMES IN LEFT SOUND " + str(left_sound.frame_count()))
    print("FRAMES IN Right SOUND " + str(right_sound.frame_count()))

    print("LEngth of sample left: " + str(len(left_sound.get_array_of_samples())) )
    print("LEngth of sample right: " + str(len(left_sound.get_array_of_samples())) )

    #number_of_frames_in_sound_for_every_20s = sound.frame_count(ms=20000)
    #print("length of song is: " + str(len(samples)/number_of_frames_in_sound_for_every_20s * 20) + " seconds")

    '''
    COLLECTED DATA:
    BYTES PER SAMPLE: 
    2
    FRAME RATE IS: 48000
    NUMBER OF FRAMES IS 7688495.0
    NUMBER OF FRAMES IN SOUND PER 200 MS: 9600.0
    h
    Number of channels in the audio is: 
    2
    SAMPLES ARE
    15376990
    FRAMES IN LEFT SOUND 7688495.0
    FRAMES IN Right SOUND 7688495.0
    LEngth of sample left: 7688495
    LEngth of sample right: 7688495
    15376990
    '''

    counter = 0
    for i in range(0, len(samples)-1):
        if(samples[i] + counter < 10000):
            samples[i] += counter
        if(counter < 500):
            counter += 2
        else:
            counter = 0

        #print(samples[i])
      #  if(i % 2 == 0):
       #     samples[i] = samples[len(samples) - i] #int(samples[i]/2)
       # else:
        #    samples[i] = samples[len(samples) - i] #int(samples[i] - 0.7*samples[i])
        #samples[i] = 10000    #This mutes the sound
        #samples[i+1] = 500

    new_sound = sound._spawn(samples)
    new_sound.export("aaay", format='mp3')

    '''
    note that when using numpy or scipy you will need to convert back to an array before you spawn:

    import array
    import numpy as np
    from pydub import AudioSegment

    sound = AudioSegment.from_file(“sound1.wav”)
    samples = sound.get_array_of_samples()

    shifted_samples = np.right_shift(samples, 1)

    # now you have to convert back to an array.array
    shifted_samples_array = array.array(sound.array_type, shifted_samples)

    new_sound = sound._spawn(shifted_samples_array)
    '''

    return numeric_array
    #raw_data = sound.raw_data
    #return raw_data


#foook = getAudioData("Playboi Carti 1")

#print(len(foook))

#MAYBE WE SHUD SPLIT THE BEAT, EVERY SO OFTEN AT PLACES WHERE THE BEAT LOOPS

def trimBeat(sound_data):
    #Remove the white noise from the start and the end.
    return 2+2

def beatSplitter(sound_data):
    #Split the beat after every 20 seconds or more depending on where the beat sounds the same as the previous split
    2+2

def getLenghtOfAudioInSeconds(sound):
    return sound.duration_seconds


#sound = AudioSegment.from_mp3(retrieveBeat["Playboi Carti 1"])

#data = sound.get_array_of_samples()
#frames = sound.frame_count()
#frames_per_second = len(data)/frames

#print("FRAMES PER SECOND ARE: " + str(frames_per_second))

#IT WAS 2 FRAMES PER SECOND

def getLenghtOfAudioData(data):
    return len(data)/2000

#print("length of audio from data is: " + str(getLenghtOfAudioData(data)))
#print("actual length of audio from data is: " + str(getLenghtOfAudioInSeconds(sound)))


def splitAudio(sound, numberOfSeconds, DEBUG = False):


    #left, right = sound.split_to_mono()
    #left = left.get_array_of_samples()

    #right = right.get_array_of_samples()
    full = sound.get_array_of_samples()

    '''
    duration_in_seconds = sound.duration_seconds
    frames_per_second = len(left)/ duration_in_seconds
    print("FRAMES PER SECOND IS :" + str(frames_per_second))
    number_of_frames_per_split = int(frames_per_second * 20)
    print("Number of frames per split " + str(number_of_frames_per_split))

    
    for i in range(0, int(len(left)/number_of_frames_per_split) - 1):
        if(len(left[i:]) > number_of_frames_per_split):
            itemLeft = left[i:number_of_frames_per_split]
            itemRight = right[i: number_of_frames_per_split]
            splitted.append(itemLeft)
            splittedRight.append(itemRight)
            i += number_of_frames_per_split
            print("fook")
        else:
            print("fook")
    '''
    splitted = []

    duration_in_seconds = sound.duration_seconds
    frames_per_second = len(full) / duration_in_seconds
    numberOfFramesPerSplit = frames_per_second * numberOfSeconds
    numberOfSplits = len(full)/numberOfFramesPerSplit

    lenghtOfData = len(full)
    #sizeOfEachSplit = lenghtOfData/

    a = 0
    for i in range(0, int(numberOfSplits)):
        splitted.append(full[int(a): int(a + numberOfFramesPerSplit)])
        a += numberOfFramesPerSplit


    if(DEBUG == True):
        sound = AudioSegment.from_mp3(file="Beats/beat1.mp3")
        for i in range(0, len(splitted)):
            #
            print(str(i) + "split")
            new_sound = sound._spawn(splitted[i])
            new_sound.export("aaay" + str(i), format='mp3')




    return splitted, frames_per_second, numberOfFramesPerSplit, numberOfSplits


def splitAudioOnDataLenght(sound, split_length = 2000, DEBUG=False):
    # left, right = sound.split_to_mono()
    # left = left.get_array_of_samples()

    # right = right.get_array_of_samples()
    full = sound.get_array_of_samples()

    '''
    duration_in_seconds = sound.duration_seconds
    frames_per_second = len(left)/ duration_in_seconds
    print("FRAMES PER SECOND IS :" + str(frames_per_second))
    number_of_frames_per_split = int(frames_per_second * 20)
    print("Number of frames per split " + str(number_of_frames_per_split))


    for i in range(0, int(len(left)/number_of_frames_per_split) - 1):
        if(len(left[i:]) > number_of_frames_per_split):
            itemLeft = left[i:number_of_frames_per_split]
            itemRight = right[i: number_of_frames_per_split]
            splitted.append(itemLeft)
            splittedRight.append(itemRight)
            i += number_of_frames_per_split
            print("fook")
        else:
            print("fook")
    '''
    splitted = []

    duration_in_seconds = sound.duration_seconds
    seconds_per_frame = duration_in_seconds / len(full)
    numberOfFramesPerSplit = split_length
    durationOfSplit = seconds_per_frame * numberOfFramesPerSplit
    numberOfSplits = len(full) / numberOfFramesPerSplit

    lenghtOfData = len(full)
    # sizeOfEachSplit = lenghtOfData/

    a = 0
    for i in range(0, int(numberOfSplits)):
        splitted.append(full[int(a): int(a + numberOfFramesPerSplit)])
        a += numberOfFramesPerSplit

    if (DEBUG == True):
        sound = AudioSegment.from_mp3(file="Beats/beat1.mp3")
        for i in range(0, len(splitted)):
            #
            print(str(i) + "split")
            new_sound = sound._spawn(splitted[i])
            new_sound.export("aaay" + str(i), format='mp3')

    return splitted, durationOfSplit, numberOfSplits

#splitAudio(sound, 1)
#splitted, durationOfSplit, numberOfSplits = splitAudioOnDataLenght(sound)

#print("Duration of Split is" + str(durationOfSplit))
#print("Number of Splits is " + str(numberOfSplits))

#stft_analysis()

"""
def stft_analysis(_input, window, N, H) :
Analysis of a sound using the short-time Fourier transform
Inputs:
_input: tensor of shape [batch_size, audio_samples]
window: analysis window, tensor of shape [N]
N: FFT size, Integer
H: hop size, Integer
Returns:
magnitudes, phases: 3D tensor with magnitude and phase spectra of shape
[batch_size, coefficients, frames]
"""

#windowTensor = tf.variable(shape=[1])
#magnitude, phases = stft_analysis(splitted, window=windowTensor, N=40, H=5)

#Need something to collect audio data.



#Save and Preprocess the files

def getAudioData(directoryAndFile):
    '''
    sound._data is a bytestring. I'm not sure what input Mpm expects, but you may need to convert the bytestring to an array like so:
    '''
    sound = AudioSegment.from_mp3(directoryAndFile)
    return sound

#Do this processing

def load_data(data = "audio.dat"):
    processed_audio = None
    with open(data, "rb") as f:
        processed_audio = pickle.load(f)
    return processed_audio

def save_data(data, filename = "audio.dat"):
    with open(filename, "wb") as f:
        pickle.dump(data, f)

#This will add all the beats we have to mp3Beats
def collectData(directory = "Beats/"):
    mp3Beats = []
    for filename in os.listdir(directory):
        if filename.endswith("U.mp3"):
            print(filename)
            beat = getAudioData(directory + filename)
            print(beat.duration_seconds)
            mp3Beats.append(beat)
            continue
        else:
            continue
    print("AMOUT OF BEATS IS" + str(len(mp3Beats)))

    save_data(mp3Beats)

if os.path.isfile("audio.dat") == False:
    collectData()


processedData = load_data()
print(len(processedData))

print(processedData[0].duration_seconds)

'''
	Analysis of a sound using the short-time Fourier transform
	Inputs:
	_input: tensor of shape [batch_size, audio_samples]
	window: analysis window, tensor of shape [N]
	N: FFT size, Integer
	H: hop size, Integer
	Returns:
	magnitudes, phases: 3D tensor with magnitude and phase spectra of shape
	[batch_size, coefficients, frames]
'''
#########################FOURIER TRANSFORM THE DATA

sound = processedData[0]
splitted, durationOfSplit, numberOfSplits = splitAudioOnDataLenght(sound, 20000)

data_placeholder = tf.placeholder(dtype=tf.float32, shape=[None, 20000])
window = tf.constant([128]) #HAS TO BE SAME AS FFT SIZE (N)
data_samples = np.array(splitted).reshape([-1, 20000])

sess = tf.InteractiveSession()
sess.run(tf.global_variables_initializer())

op = SoundProcessing.stft_analysis(data_placeholder, window=window, N=128, H=5)

magnitude, phases = sess.run(op, feed_dict={data_placeholder: data_samples})
print(magnitude)
print(phases)



























