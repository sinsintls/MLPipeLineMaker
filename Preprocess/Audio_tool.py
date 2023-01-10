from typing import Dict

import librosa
import numpy as np


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


if __name__ == "__main__":
    data = np.random.randn(10000)
    samplerate = 40000

    res = librosa.feature.mfcc(y=data, sr=samplerate)
    print(res)