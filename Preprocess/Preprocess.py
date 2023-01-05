from typing import List, Dict

import numpy as np


class SetError(Exception):
    pass


class PrepObj:

    def __init__(
            self,
            data_type: str,
            method_pipe_line: List[str],
            method_params: Dict[str, Dict] = None,
                 ):

        self.data_type = data_type
        self.pipe_line = method_pipe_line
        self.params = method_params
        self.parallel = False
        self.batch = True

    def set_mode(self, parallel: bool = False, batch: bool = True) -> None:

        if parallel and not batch:
            raise SetError("Parallel mode is only for batch.")

        self.parallel = parallel
        self.batch = batch
        print("Setting complete..")

    def exec_pipeline(self, data: np.ndarray) -> np.ndarray:
        prep_data = data
        return prep_data

    def __call__(self, data: np.ndarray) -> np.ndarray:
        prep_data: np.ndarray = self.exec_pipeline(data)
        print("processing..", prep_data)
        return prep_data



if __name__ == "__main__":
    prep = PrepObj(
        data_type="audio",
        method_pipe_line=["mfcc"]
    )

    prep.set_mode(parallel=True, batch=True)

    data = np.array([1, 2, 3, 4, 5])

    prep(data)