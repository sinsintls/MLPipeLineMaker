from typing import List, Dict

import numpy as np
import dask.delayed
import dask.diagnostics
from tqdm import tqdm

from Validators import valid_pipeline
from Audio_tool import *


########### 에러메세지 스크립트 이동 #########
class SetModeError(Exception):
    pass

class PipeValidError(Exception):
    pass

#######################################

class PrepPipe:

    def __init__(
            self,
            data_type: str,
            method_pipe_line_order: List[Dict[str, Dict]],
            parallel: bool = False,
                 ):

        ### validate pipe line
        if valid_pipeline(method_pipe_line_order):
            pass
        else:
            raise PipeValidError

        ### get parameters
        self.data_type = data_type
        self.pipe_line_order = method_pipe_line_order
        self.parallel = parallel

        self.pipeline = PipeObj(self.pipe_line_order, self.parallel)


    def __call__(self, data_: np.ndarray) -> np.ndarray:

        try:

            prep_data: np.ndarray = self.pipeline(data_)

            return prep_data

        except Exception as e:

            print("Something wrong..\n", e)


class PipeObj:
    def __init__(
            self,
            pipeline_info: List[Dict[str, Dict]],
            parallel: bool,
    ):
        self.pipeline_info = pipeline_info
        self.parallel = parallel

    def __call__(self, data: np.ndarray) -> np.ndarray:

        if type(data[0]) != np.ndarray:
            data = [data]

        if self.parallel:
            output = self.parallel_exec_pipe(data)

        else:
            output = self.exec_pipe(data)

        return output

    def exec_pipe(self, data: np.ndarray) -> np.ndarray:

        res = []
        for d in tqdm(data):

            for method in self.pipeline_info:

                method_name = list(method.keys())[0]
                method_params = list(method.values())[0]

                func = eval(method_name)
                d = func(d, method_params)

            res.append(d)

        return np.asarray(res)

    def parallel_exec_pipe(self, data: np.ndarray) -> np.ndarray:

        res = []
        for d in data:

            for method in self.pipeline_info:

                method_name = list(method.keys())[0]
                method_params = list(method.values())[0]

                func = eval(method_name)
                d = dask.delayed(func)(d, method_params)

            res.append(d)

        with dask.diagnostics.ProgressBar():
            res = dask.compute(*res)

        return np.asarray(res)



if __name__ == "__main__":

    import librosa

    path = "test_audio.wav"
    data, sr = librosa.load(path)

    """
    preprocessing list

    func
    - crop_n_pad : max_length - int, padding_mode - str(zero or repeat)

    librosa_func
    - resample
    - mfcc
    - melspectrogram
    - tonnetz
    - zero_crossing_rate
    - stft
    """

    """
    TODO LIST
    => parameter class 작성
    => 
    """

    params = {
        "data_type": "audio",
        "method_pipe_line_order": [
            {
                "crop_n_pad": {
                    "max_length": 10000,
                    "padding_mode": "repeat",
                }
            },
            {
                "melspectrogram": {

                }
            },
        ],
        "parallel": True
    }

    pp = PrepPipe(**params)
    res = pp(data)

    print("shape: ", res.shape, "\n", "value: ", res)

    """
    How to use with loader parallelly
    
    dataset_path = [ ... ]
    
    pp_dataset = []
    for path in dataset_path:
        data, sr = dask.delayed(loader)(path)
        params = {..pipeline setting( preprocess order, function setting etc ..), parallel: False}
        prep = PrepPipe(**params)
        pp_dataset.append(dask.delayed(prep)(data))
    
    with dask.diagnostics.ProgressBar():
        pp_dataset = dask.compute(*pp_dataset)
    """
