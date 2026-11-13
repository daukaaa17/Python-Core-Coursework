def check_str(s: str):
    s1 = s.lower()
    clean_text = "".join(char for char in s1 if char.isalnum())
    a = []
    b = []
    c = bool
    for i in range(0, len(clean_text)):
        a.append(clean_text[i])
        b.append(clean_text[-i - 1])
    for i in range(0, len(clean_text)):
        if a[i] == b[i]:
            c = True
        else:
            c = False
            break
    return c


