from wordninja import split
from dependencies.decorators import verify_types
from dependencies.matrix_utils import chunk, transpose
from dependencies.text_recognition_utils import filter_only_valid
from dependencies.text_transformation_utils import substitute


@verify_types(int)
def find_bandwidth(size):
    return [i for i in range(2, size) if size % i == 0]


@verify_types(str)
def scytale(text):
    possible_bandwidth = find_bandwidth(len(text))
    text_matrixes = [transpose(chunk(text, i)) for i in possible_bandwidth]
    all_texts = [substitute(''.join([''.join(row) for row in m]))
                 for m in text_matrixes]
    
    valid_texts = filter_only_valid(all_texts)
    return valid_texts if valid_texts\
        else filter_only_valid([' '.join(split(text)) for text in all_texts])
