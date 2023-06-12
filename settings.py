from json import load, dump


def get_settings(filename):
    try:
        with open(filename) as file:
            return load(file)
    except FileNotFoundError:
        print(f'No file called "{filename}".')
            


def save_settings(filename, dictionary):
    try:
        with open(filename) as file:
            dump(dictionary)
    except FileNotFoundError:
        print(f'No file called "{filename}".')
