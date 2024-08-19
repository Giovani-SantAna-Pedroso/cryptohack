import add_round_key

def bytes2matrix(text):
    """ Converts a 16-byte array into a 4x4 matrix.  """
    return [list(text[i:i+4]) for i in range(0, len(text), 4)]

def matrix2bytes(matrix):
    matrix1d = [item for sublist in matrix for item in sublist]
    return bytes(matrix1d)

matrix = [
    [99, 114, 121, 112],
    [116, 111, 123, 105],
    [110, 109, 97, 116],
    [114, 105, 120, 125],
]

print(matrix2bytes(matrix))

rounded_key = add_round_key.get_round_key()
print(rounded_key)
print(matrix2bytes(rounded_key))

