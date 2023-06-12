en_map = {
    "q": ("w", "s", "a"),
    "w": ("e", "d", "s", "a", "q"),
    "e": ("r", "f", "d", "s", "w"),
    "r": ("t", "g", "f", "d", "e"),
    "t": ("y", "h", "g", "f", "r"),
    "y": ("u", "j", "h", "g", "t"),
    "u": ("i", "k", "j", "h", "y"),
    "i": ("o", "l", "k", "j", "u"),
    "o": ("p", ";", "l", "k", "i"),
    "p": ("[", "'", ";", "l", "o"),
    "[": ("]", "'", ";", "p"),
    "]": ("'", "["),
    "a": ("z", "x", "s", "w", "q"),
    "s": ("x", "d", "e", "w", "q", "a", "z"),
    "d": ("c", "f", "r", "e", "w", "s", "x"),
    "f": ("v", "g", "t", "r", "e", "d", "c"),
    "g": ("b", "h", "y", "t", "r", "f", "v"),
    "h": ("n", "j", "u", "y", "t", "g", "b"),
    "j": ("m", "k", "i", "u", "y", "h", "n"),
    "k": (",", "l", "o", "i", "u", "j", "m"),
    "l": (".", ";", "p", "o", "i", "k", ","),
    ";": ("/", "'", "[", "p", "o", "l", "."),
    "'": ("]", "[", "p", ";", "/"),
    "z": ("x", "s", "a"),
    "x": ("c", "d", "s", "z"),
    "c": ("v", "f", "d", "x"),
    "v": ("b", "g", "f", "c"),
    "b": ("n", "h", "g", "v"),
    "n": ("m", "j", "h", "b"),
    "m": (",", "k", "j", "n"),
    ",": (".", "l", "k", "m"),
    ".": ("/", ";", "l", ","),
    "/": ("'", ";", "."),
}

en_shift_map = {
    "Q": ("W", "S", "A"),
    "W": ("E", "D", "S", "A", "Q"),
    "E": ("R", "F", "D", "S", "W"),
    "R": ("T", "G", "F", "D", "E"),
    "T": ("Y", "H", "G", "F", "R"),
    "Y": ("U", "J", "H", "G", "T"),
    "U": ("I", "K", "J", "H", "Y"),
    "I": ("O", "L", "K", "J", "U"),
    "O": ("P", ":", "L", "K", "I"),
    "P": ("{", '"', ":", "L", "O"),
    "{": ("}", '"', ":", "P"),
    "}": ('"', "{"),
    "A": ("Z", "X", "S", "W", "Q"),
    "S": ("X", "D", "E", "W", "Q", "A", "Z"),
    "D": ("C", "F", "R", "E", "W", "S", "X"),
    "F": ("V", "G", "T", "R", "E", "D", "C"),
    "G": ("B", "H", "Y", "T", "R", "F", "V"),
    "H": ("N", "J", "U", "Y", "T", "G", "B"),
    "J": ("M", "K", "I", "U", "Y", "H", "N"),
    "K": ("<", "L", "O", "I", "U", "J", "M"),
    "L": (">", ":", "P", "O", "I", "K", "<"),
    ":": ("?", '"', "{", "P", "O", "L", ">"),
    '"': ("}", "{", "P", ":", "?"),
    "Z": ("X", "S", "A"),
    "X": ("C", "D", "S", "Z"),
    "C": ("V", "F", "D", "X"),
    "V": ("B", "G", "F", "C"),
    "B": ("N", "H", "G", "V"),
    "N": ("M", "J", "H", "B"),
    "M": ("<", "K", "J", "N"),
    "<": (">", "L", "K", "M"),
    ">": ("?", ":", "L", "<"),
    "?": ('"', ":", ">"),
}

ru_map = {
    "й": ("ц", "ы", "ф"),
    "ц": ("у", "в", "ы", "ф", "й"),
    "у": ("к", "а", "в", "ы", "ц"),
    "к": ("е", "п", "а", "в", "у"),
    "е": ("н", "р", "п", "а", "к"),
    "н": ("г", "о", "р", "п", "е"),
    "г": ("ш", "л", "о", "р", "н"),
    "ш": ("щ", "д", "л", "о", "г"),
    "щ": ("з", "ж", "д", "л", "ш"),
    "з": ("х", "э", "ж", "д", "щ"),
    "х": ("ъ", "э", "ж", "з"),
    "ъ": ("х", "э"),
    "ф": ("я", "ч", "ы", "ц", "й"),
    "ы": ("ч", "в", "у", "ц", "й", "ф", "я"),
    "в": ("с", "а", "к", "у", "ц", "ы", "ч"),
    "а": ("м", "п", "е", "к", "у", "в", "с"),
    "п": ("и", "р", "н", "е", "к", "а", "м"),
    "р": ("т", "о", "г", "н", "е", "п", "и"),
    "о": ("ь", "л", "ш", "г", "н", "р", "т"),
    "л": ("б", "д", "щ", "ш", "г", "о", "ь"),
    "д": ("ю", "ж", "з", "щ", "ш", "л", "б"),
    "ж": (".", "э", "х", "з" "щ", "д", "ю"),
    "э": ("ъ", "х", "ж", "з", "."),
    "я": ("ч", "ы", "ф"),
    "ч": ("с", "м", "и", "я"),
    "с": ("м", "а", "в", "ч"),
    "м": ("и", "п", "а", "с"),
    "и": ("т", "р", "п", "м"),
    "т": ("ь", "о", "р", "и"),
    "ь": ("б", "л", "о", "т"),
    "б": ("ю", "д", "л", "ь"),
    "ю": (".", "ж", "д", "б"),
    ".": ("э", "ж", "ю"),
}

ru_shift_map = {
    "Й": ("Ц", "Ы", "Ф"),
    "Ц": ("У", "В", "Ы", "Ф", "Й"),
    "У": ("К", "А", "В", "Ы", "Ц"),
    "К": ("Е", "П", "А", "В", "У"),
    "Е": ("Н", "Р", "П", "А", "К"),
    "Н": ("Г", "О", "Р", "П", "Е"),
    "Г": ("Ш", "Л", "О", "Р", "Н"),
    "Ш": ("Щ", "Д", "Л", "О", "Г"),
    "Щ": ("З", "Ж", "Д", "Л", "Ш"),
    "З": ("Х", "Э", "Ж", "Д", "Щ"),
    "Х": ("Ъ", "Э", "Ж", "З"),
    "Ъ": ("Х", "Э"),
    "Ф": ("Я", "Ч", "Ы", "Ц", "Й"),
    "Ы": ("Ч", "В", "У", "Ц", "Й", "Ф", "Я"),
    "В": ("С", "А", "К", "У", "Ц", "Ы", "Ч"),
    "А": ("М", "П", "Е", "К", "У", "В", "С"),
    "П": ("И", "Р", "Н", "Е", "К", "А", "М"),
    "Р": ("Т", "О", "Г", "Н", "Е", "П", "И"),
    "О": ("Ь", "Л", "Ш", "Г", "Н", "Р", "Т"),
    "Л": ("Б", "Д", "Щ", "Ш", "Г", "О", "Ь"),
    "Д": ("Ю", "Ж", "З", "Щ", "Ш", "Л", "Б"),
    "Ж": (",", "Э", "Х", "З", "Щ", "Д", "Ю"),
    "Э": ("Ъ", "Х", "Ж", "З", ","),
    "Я": ("Ч", "Ы", "Ф"),
    "Ч": ("С", "М", "И", "Я"),
    "С": ("М", "А", "В", "Ч"),
    "М": ("И", "П", "А", "С"),
    "И": ("Т", "Р", "П", "М"),
    "Т": ("Ь", "О", "Р", "И"),
    "Ь": ("Б", "Л", "О", "Т"),
    "Б": ("Ю", "Д", "Л", "Ь"),
    "Ю": (",", "Ж", "Д", "Б"),
    ".": ("Э", "Ж", "Ю"),
}

ALPHABETS = {
    "en": "abcdefghijklmnopqrstuvwxyz",
    "ru": "абвгдеёжзийклмнопрстуфхцчшщъыьэюя",
}

NEIGHBORS_FUNCS = {
    "en": lambda char: en_map[char],
    "ru": lambda char: ru_map[char],
}


def get_language(char):
    for language, alphabet in ALPHABETS.items():
        if char in alphabet:
            return language
    return None


def get_neighbors(char_a, char_b):
    language_a = get_language(char_a)
    if language_a == get_language(char_b) and language_a in NEIGHBORS_FUNCS:
        return NEIGHBORS_FUNCS[language_a](char_b)
    return []
