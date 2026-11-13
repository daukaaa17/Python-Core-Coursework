def get_longest_word(s: str) -> str:
    a = s.replace("!", "")
    words = a.strip().split()
    result = ""
    for word in words:
        if len(word) > len(result):
            result = word
    return result

