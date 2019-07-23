__author__ = "Max Margolin, margolinmax@gmail.com"
# pay no attention to this yet

import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np

filename = "og.mp3"


def extract(current_time, wave, sr, time_multiples):
    """

    :param current_time:
    :param wave:
    :param sr:
    :param time_multiples:
    :return:
    """
    current = current_time * sr
    arr = []
    for i in range(-10, 10):
        start = current + sr * i * time_multiples
        finish = current + sr * (i + 1) * time_multiples
        arr.append(np.average(np.abs(wave[start:finish])))
    return arr


def get_nearby(filename, claims):
    y, sr = librosa.load(filename)
    e = extract(claims[0], y, sr, 1)
    return e


def get_nearby_up_down(filename, claims):
    a = get_nearby(filename, claims)
    diff = np.diff(a)
    return diff > 0
