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
            method_pipe_line_order: List[str],
            method_params: Dict[str, Dict] = None,
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
        self.params = method_params
        self.parallel = parallel

        self.pipeline = PipeObj(self)


    def __call__(self, data_: np.ndarray) -> np.ndarray:

        print("Start processing!!\n")

        try:

            prep_data: np.ndarray = self.pipeline.put_in(data_)

            print("End processing!!\n")

            return prep_data

        except Exception as e:

            print("Something wrong..\n", e)


class PipeObj:

    def __init__(
            self,
            pipeline: PrepPipe,
    ):
        self.pipeline_info = pipeline

    def put_in(self, data: np.ndarray) -> np.ndarray:

        if type(data[0]) != np.ndarray:
            data = [data]

        if self.pipeline_info.parallel:
            output = self.parallel_exec_pipe(data)

        else:
            output = self.exec_pipe(data)

        return output

    def exec_pipe(self, data: np.ndarray) -> np.ndarray:

        res = []
        for d in tqdm(data):

            for method in self.pipeline_info.pipe_line_order:

                func = eval(method)
                params = self.pipeline_info.params[method]
                d = func(d, params)

            res.append(d)

        return np.asarray(res)

    def parallel_exec_pipe(self, data: np.ndarray) -> np.ndarray:

        res = []
        for d in data:

            for method in self.pipeline_info.pipe_line_order:

                func = eval(method)
                params = self.pipeline_info.params[method]
                d = dask.delayed(func)(d, params)

            res.append(d)

        with dask.diagnostics.ProgressBar():
            res = dask.compute(*res)

        return np.asarray(res)



if __name__ == "__main__":
    import librosa

    path = "test_audio.wav"
    data = librosa.load(path)[0]

    """
        data_type: str,
        method_pipe_line_order: List[str],
        method_params: Dict[str, Dict] = None,
        parallel: bool = False,
    """

    params = {
        "data_type": "audio",
        "method_pipe_line_order": ["test1","test2"],
        "method_params": {
            "test1":{

            },
            "test2":{

            }
        },
        "parallel": True
    }

    pp = PrepPipe(**params)

    test_data = np.array([1,2,3,4,5])

    print(pp(data))
