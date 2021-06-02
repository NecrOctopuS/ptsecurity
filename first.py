def dict_to_string(dict_value: dict, nesting=0):
    string = ''
    for key, value in dict_value.items():
        if string:
            string = string + '\n'
        if isinstance(value, dict):
            sub_string = dict_to_string(value, nesting=nesting+1)
        else:
            sub_string = value
        string = string + f'{key}:\n {" " * nesting}{sub_string}'
    return string


def my_code(dict_value: dict):
    print(dict_to_string(dict_value))


if __name__ == '__main__':
    my_code({
        'first': 'first_value',
        'second': 'second_value'
    })
    my_code({
        '1': {
            'child': '1/child/value'
        },
        '2': '2/value'
    })
