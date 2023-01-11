from typing import Dict

import librosa
import numpy as np

#######################################
class Params:
    max_length = "max_length"
    padding_mode = "padding_mode"
    repeat = "repeat"
    zero = "zero"

#######################################

def crop_n_pad(data: np.ndarray, params: Dict=None):

    max_len = params[Params.max_length]
    padding_mode = params[Params.padding_mode]
    data_len = len(data)

    if max_len < data_len:

        pp_data = data[:max_len]

    elif max_len > data_len:

        pp_data = []

        if max_len < data_len:

            pp_data = data[:len]

        elif max_len > data_len:

            pp_data = [data]
            rest = max_len % data_len

            if rest != 0 and padding_mode == "repeat":

                num_iter = int(max_len / data_len) - 1

                for i in range(num_iter):
                    pp_data.append(data)

                pp_data.append(data[:rest])

            elif rest != 0 and padding_mode == "zero":

                pp_data.append(np.zeros(max_len - data_len))

            pp_data = np.hstack(pp_data)

    else:
        pp_data = data

    return pp_data

def resample(data: np.ndarray, params: Dict=None):
    return librosa.resample(y=data, **params)


def mfcc(data: np.ndarray, params: Dict=None):
    return librosa.feature.mfcc(y=data, **params)


def melspectrogram(data: np.ndarray, params: Dict=None):
    return librosa.feature.melspectrogram(y=data, **params)


def tonnetz(data: np.ndarray, params: Dict=None):
    return librosa.feature.tonnetz(y=data, **params)


def zero_crossing_rate(data: np.ndarray, params: Dict=None):
    return librosa.feature.melspectrogram(y=data, **params)


def stft(data: np.ndarray, params: Dict=None):
    return librosa.stft(y=data, **params)


def test1(data: np.ndarray, params: Dict=None):
    return data + 1


def test2(data: np.ndarray, params: Dict=None):
    return data * -1
