__author__ = "Max Margolin, margolinmax@gmail.com"
# base implementation idea,not final

import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np

claim = [30]
UNIT_WIDTH = 5


def plot_waves(track_1, track_2, unit_width=UNIT_WIDTH):
    """
    show waves of 2 tracks using matplotlib
    :param track_1: original video sound
    :param track_2: lyrical video sound
    :param unit_width: time unit width
    """
    plt.figure()
    plt.plot(range(0, len(track_1) * unit_width, unit_width), track_1, color='black')
    plt.plot(range(0, len(track_2) * unit_width, unit_width), track_2, linewidth=5, markersize=16, color='green')
    plt.show()


def get_sound_wave_averages(filename, time_multiples):
    """
    get the sound wave values, averaged for every %time_multiples% time period
    :param filename: name of sound file
    :param time_multiples: time unit in second to average
    :return: array of averages over every time_multiples seconds

    note
    """
    wave, rate = librosa.load(filename)
    averages = []
    for start_index in range(0, len(wave), rate * time_multiples):
        end_index = start_index + rate * time_multiples
        averages.append(np.average(np.abs(wave[start_index:end_index])))
    return averages


def get_peak_correlation(main_sound_wave, secondary_sound_wave, unit_width=UNIT_WIDTH):
    """
    find the best offset for peak correlation.
    by returning the maximum of the correlation by offset array.
    :param main_sound_wave: original video sound
    :param secondary_sound_wave:  lyrical video sound
    :param unit_width: size of average unit in seconds
    :return: best offset (multiple of unit width) for maximum correlation
    """
    return unit_width * np.argmax(np.correlate(main_sound_wave, secondary_sound_wave))


def get_correlation_array(main_sound_wave, secondary_sound_wave, unit_width=UNIT_WIDTH):
    """
    get the correlation by offset
    :param main_sound_wave: original video sound
    :param secondary_sound_wave:  lyrical video sound
    :param unit_width: size of average unit in seconds
    :return: correlation array
    """
    return np.correlate(main_sound_wave, secondary_sound_wave)


def get_correlation_features(filename1="og.mp3", filename2="lyrical.mp3", unit_width=UNIT_WIDTH):
    """
    get all features from this file
    :param filename1: og
    :param filename2:  lyrical
    :param unit_width:  sound unit to avg
    :return:
    """
    og_wave = get_sound_wave_averages(filename1, unit_width)
    lyrical_wave = get_sound_wave_averages(filename2, unit_width)
    return get_correlation_array(og_wave, lyrical_wave), get_peak_correlation(og_wave, lyrical_wave)


def get_lengths(filename1="og.mp3", filename2="lyrical.mp3"):
    """
    TODO: rethink this 2 sounds in 1 function thing
    :param filename1: og
    :param filename2:  lyrical
    :return:  2 lengths
    """
    wave1, rate1 = librosa.load(filename1)
    wave2, rate2 = librosa.load(filename2)
    return len(wave1) / rate1, len(wave2) / rate2


