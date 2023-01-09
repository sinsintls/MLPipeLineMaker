from typing import Dict

import librosa
import numpy as np


def mfcc(data: np.ndarray, params: Dict):
    return librosa.feature.mfcc(data, params)


def melspec(data: np.ndarray, params: Dict):
    return librosa.feature.melspectrogram(data, params)


if __name__ == "__main__":
    data = np.random.randn(10000)
    samplerate = 40000

    res = librosa.feature.mfcc(y=data, sr=samplerate)
    print(res)