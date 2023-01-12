from typing import List

def valid_pipeline(method_pipe_line_order: List[str]) -> None:
    return True

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

input shape: (n, any)                 =>//     crop_n_pad     //=>    output shape : n, max_length

input shape: (n, input_data_length)   =>//      resample      //=>    output shape : (n, input_data_length * (target_sr / orig_sr))

input shape: (n, input_data_length)   =>//         mfcc       //=>    output shape : (n, n_mfcc ,int(input_data_length/hop_length)+1)

input shape: (n, input_data_length)   =>//   melspectrogram   //=>    output shape : (n, n_mels ,int(input_data_length/hop_length)+1)

input shape: (n, input_data_length)   =>//       tonnetz      //=>    output shape : (n, 6 ,int(input_data_length/hop_length)+1)

input shape: (n, input_data_length)   =>// zero_crossing_rate //=>    output shape : (n, 1 ,int(input_data_length/hop_length)+1)

input shape: (n, input_data_length)   =>//         stft       //=>    output shape : (n, 1 ,int(input_data_length/hop_length)+1)

"""