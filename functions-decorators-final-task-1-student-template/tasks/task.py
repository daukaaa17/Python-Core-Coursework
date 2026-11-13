def split(data: str, sep=None, maxsplit=-1):
    if sep is None:
        # Default behavior: split on any whitespace
        result = []
        current = ''
        count = 0

        for char in data:
            if char.isspace():
                if current != '' and (maxsplit == -1 or count < maxsplit):
                    result.append(current)
                    current = ''
                    count += 1
            else:
                current += char

        if current != '':
            result.append(current)

        return result

    else:
        # Custom separator behavior
        result = []
        current = ''
        i = 0
        count = 0
        sep_len = len(sep)

        while i < len(data):
            if data[i:i + sep_len] == sep and (maxsplit == -1 or count < maxsplit):
                result.append(current)
                current = ''
                i += sep_len
                count += 1
            else:
                current += data[i]
                i += 1

        result.append(current)

        return result

if __name__ == '__main__':
    assert split('') == []
    assert split(',123,', sep=',') == ['', '123', '']
    assert split('test') == ['test']
    assert split('Python    2     3', maxsplit=1) == ['Python', '2     3']
    assert split('    test     6    7', maxsplit=1) == ['test', '6    7']
    assert split('    Hi     8    9', maxsplit=0) == ['Hi     8    9']
    assert split('    set   3     4') == ['set', '3', '4']
    assert split('set;:23', sep=';:', maxsplit=0) == ['set;:23']
    assert split('set;:;:23', sep=';:', maxsplit=2) == ['set', '', '23']
