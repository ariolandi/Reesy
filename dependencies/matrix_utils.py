from dependencies.decorators import verify_types


@verify_types((str, []), int)
def chunk(text, size):
    return [text[i:i + size] for i in range(0, len(text), size)]


@verify_types([([], str)])
def transpose(matrix):
    def get_column(matrix, i):
        return [row[i] for row in matrix]

    return [get_column(matrix, i) for i in range(len(matrix[0]))]
