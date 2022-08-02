def read(file_path):
    """
    Function for reading files
    :param file_path: path to file
    :return: content of the file
    """
    with open(file_path, 'r') as f:
        result = f.read()
    return result
