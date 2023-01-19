from dependencies.decorators import verify_types
from dependencies.common import filter_list
from dependencies.matrix_utils import chunk, transpose
from dependencies.text_recognition_utils import is_valid_text
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

    return filter_list(is_valid_text, all_texts)
