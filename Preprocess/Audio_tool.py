import librosa
import numpy as np





if __name__ == "__main__":
    data = np.random.randn(10000)
    samplerate = 40000

    res = librosa.feature.mfcc(y=data, sr=samplerate)
    print(res)