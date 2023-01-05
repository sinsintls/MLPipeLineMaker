from typing import List, Dict

import numpy as np


class SetModeError(Exception):
    pass


class PrepPipe:

    def __init__(
            self,
            data_type: str,
            method_pipe_line: List[str],
            method_params: Dict[str, Dict] = None,
            batch: bool = True,
            parallel: bool = False,
                 ):

        self.data_type = data_type
        self.pipe_line = method_pipe_line
        self.params = method_params
        self.batch = batch
        self.parallel = parallel

        if parallel and not batch:
            raise SetModeError("Parallel mode is only for batch.\n")

        self.pipeline = PipeObj(self)

    def exec_pipeline(self, data: np.ndarray) -> np.ndarray:

        prep_data = self.pipeline.put_in(data)

        return prep_data

    def __call__(self, data_: np.ndarray) -> np.ndarray:

        print("Start processing!!\n")

        try:

            prep_data: np.ndarray = self.exec_pipeline(data_)

            print("End processing!!\n")

            return prep_data

        except Exception as e:

            print("Something wrong..\n", e)


class PipeObj:

    def __init__(
            self,
            pipeline: PrepPipe,
    ):
        self.pipeline = pipeline

    def make_pipeline(self):
        ### batch && stream // parallel or not ###
        self.pipeline
        pass

    def put_in(self, data: np.ndarray) -> np.ndarray:

        output = data

        return output








if __name__ == "__main__":
    prep = PrepPipe(
        data_type="audio",
        method_pipe_line=["mfcc"]
    )

    prep.set_mode(parallel=True, batch=True)

    data = np.array([1, 2, 3, 4, 5])

    prep(data)