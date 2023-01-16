from typing import List, Tuple, Dict


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
    
Input data 

input shape: (n, any)                 =>//     crop_n_pad     //=>    output shape : (n, max_length)

input shape: (n, input_data_length)   =>//      resample      //=>    output shape : (n, input_data_length * (target_sr / orig_sr))

input shape: (n, input_data_length)   =>//         mfcc       //=>    output shape : (n, n_mfcc ,int(input_data_length/hop_length)+1)

input shape: (n, input_data_length)   =>//   melspectrogram   //=>    output shape : (n, n_mels ,int(input_data_length/hop_length)+1)

input shape: (n, input_data_length)   =>//       tonnetz      //=>    output shape : (n, 6 ,int(input_data_length/hop_length)+1)

input shape: (n, input_data_length)   =>// zero_crossing_rate //=>    output shape : (n, 1 ,int(input_data_length/hop_length)+1)

input shape: (n, input_data_length)   =>//         stft       //=>    output shape : (n, 1 + n_fft/2, n_frames)

"""
###
###
SHAPE_LIST = {

    "crop_n_pad"         : (1,1),

    "resample"           : (1,1),

    "mfcc"               : (1,2),

    "melspectrogram"     : (1,2),

    "tonnetz"            : (1,2),

    "zero_crossing_rate" : (1,2),

    "stft"               : (1,2),

}
def get_output_shape(prep_kind: str) -> Tuple[int]:
    return SHAPE_LIST[prep_kind][1]


def get_input_shape(prep_kind: str) -> Tuple[int]:
    return SHAPE_LIST[prep_kind][0]


def valid_pipeline(prep_pipe_line_order: List[Dict[str, Dict]]) -> bool:

    for i, prep_n_config in enumerate(prep_pipe_line_order):

        if i == 0:
            continue

        for prep_kind, prep_config in prep_n_config.items():
            output_shape = get_output_shape(list(prep_pipe_line_order[i-1].keys())[0])
            input_shape = get_input_shape(prep_kind)

            if output_shape != input_shape:
                return False

    return True
