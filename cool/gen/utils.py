import keyword
import warnings

warnings.filterwarnings('always')


def is_valid_name(string: str):
    return not keyword.iskeyword(string) and not keyword.issoftkeyword(
        string) and string.isidentifier()


def replace_invalid_character_with_underscore(string: str):
    string = string[0] + ''.join([s if ('_' + s).isidentifier() else '_' for s in string[1:]])
    if not ('_' + string[0]).isidentifier():
        string = '_' + string[1:]
    elif not string[0].isidentifier():
        string = '_' + string
    return string


def create_function_name(string: str):
    message = '{!r}'.format(string)
    string = '_'.join(string.lower().split())
    if not is_valid_name(string):
        warnings.warn(message, RuntimeWarning)
    string = replace_invalid_character_with_underscore(string)
    if not is_valid_name(string):
        raise RuntimeError('{} {}'.format(message, string))
    return string


def create_class_name(string: str):
    message = '{!r}'.format(string)
    string = ''.join([s[0].upper() + s[1:] for s in string.split()])
    if not is_valid_name(string):
        warnings.warn(message, RuntimeWarning)
    string = replace_invalid_character_with_underscore(string)
    if not is_valid_name(string):
        raise RuntimeError
    return string
