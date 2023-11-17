import os


def get_file_as_string(filename):
    '''

    :param filename:
    :return:
    '''
    file_content = None

    script_dir = os.path.dirname(__file__)
    abs_file_path = os.path.join(script_dir, filename)

    with open(abs_file_path, 'r') as file:
        file_content = file.read()
    return file_content


def save_string_as_file(filename, content):
    text_file = open(filename, "w")
    n = text_file.write(content)
    text_file.close()
