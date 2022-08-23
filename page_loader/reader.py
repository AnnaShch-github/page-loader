def read(file_path):
    with open(file_path, 'rb') as f:
        result = f.read()
    return result
