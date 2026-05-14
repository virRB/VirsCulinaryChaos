import os


def save(value, callback):
    path = callback + '.txt'

    try:
        with open(path, "w") as f:
            f.write(str(value))
        return True

    except Exception as e:
        print(f'Save error: {e}')
        return False


def load(callback, dat_type):
    path = callback + '.txt'

    if not os.path.exists(path):
        print('Err. Callback not found')

        if dat_type == 'str':
            return ""

        elif dat_type == 'int':
            return 0

        return None

    try:
        with open(path, "r") as f:
            content = f.read()

        if dat_type == 'str':
            return content

        elif dat_type == 'int':
            try:
                return int(content)

            except ValueError:
                print('Err. Invalid integer data')
                return 0

        else:
            print('Err. Unsupported data type')
            return None

    except Exception as e:
        print(f'Load error: {e}')
        return None