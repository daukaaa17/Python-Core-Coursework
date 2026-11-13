def replacer(s: str) -> str:
    translation_table = str.maketrans({'"': "'", "'": '"'})
    return s.translate(translation_table)

