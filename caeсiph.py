## типа импортировали и пофигу что там не такая функция была
ENGLISH_ALPHABET = "abcdefghijklmnopqrstuvwxyz"
RUSSIAN_ALPHABET = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

"""
Определяет к какому алфавиту принадлежит символ
"""
def get_alphabet(char: str) -> str:
    char = char.strip().lower()
    if char in ENGLISH_ALPHABET:
        return ENGLISH_ALPHABET
    else:
        return RUSSIAN_ALPHABET

## типа импортировали
"""
Применяет сдвиг к одному символу с учётом регистра
"""
def shift_char(char: str, shift: int, alphabet: str) -> str:
    if char.lower() not in alphabet:
        return char  # Выйти рано если символа нет в словаре
    caseflag = char.islower()  # True - малый регистр, False - большой
    char = char.lower()
    charpos = (alphabet.index(char) + shift) % len(alphabet)

    return alphabet[charpos].upper() if not caseflag else alphabet[charpos]

"""
Шифрует текст шифром Цезаря
"""
def encrypt(text: str, shift: int) -> str:
    otv = ""
    for i in text:
        otv += shift_char(i, shift, get_alphabet(i))
    return otv

"""
Дешифрует текст, зашифрованный шифром Цезаря
"""
def decrypt(text: str, shift: int) -> str:
    otv = ""
    for i in text:
        otv += shift_char(i, -shift, get_alphabet(i))
    return otv

"""
Вывод помощи
"""
def help():
    print("""
Использование: python3 CaeCiph.py [ОПЕРАЦИЯ] [ТЕКСТ] [ШАГ]
        или python3 CaeCiph.py [ТЕКСТ] для шифрования с шагом 1
        или python3 CaeCiph.py для входа в интерактивную оболочку
Шифрует тест шифром Цезаря. Поддерживает русский и английский языки
    encode   Шифрует текст с заданным шагом
    decode   Дешифрует текст с заданным шагом
    help     Показывает этот текст помощи

Репозиторий кода <https://github.com/novvux/CaeCiph>
          """)

"""
Вывод помощи при использовании интерактивной оболочки
"""
def interactive_shell_help():
    print("""
Введите Текст, Шаг и 1 для шифрования текста, 2 для дешифровки
""")


import sys
def cae_ciph():
    if len(sys.argv) == 1:
        interactive_shell_help()
        run_interactive_shell()
        return 0
    elif sys.argv[1] == "help":
        help()
        return 0
    elif len(sys.argv) == 2:
        print(encrypt(sys.argv[1], 1))
        return 1
    elif len(sys.argv) < 4:
        print("Недостаточно аргументов")
        help()
        return 1
    elif len(sys.argv) > 4:
        print("Избыток аргументов")
        help()
        return 1
    match sys.argv[1]:
        case "help":
            help()
        case "encode":
            try:
                print(encrypt(sys.argv[2], int(sys.argv[3])))
            except ValueError:
                print("Шаг должен быть числом")
        case "decode":
            try:
                print(decrypt(sys.argv[2], int(sys.argv[3])))
            except ValueError:
                print("Шаг должен быть числом")
        case _:
            print(encrypt(sys.argv[1], 1))

    return 0

"""
Консольный интерфейс для шифра Цезаря
"""
def run_interactive_shell():
    text = input()
    shift = int(input())
    flag = bool(int(input()) - 1)  # False - Шифруем, True - не шифруем.

    if not flag:
        print(encrypt(text, shift))
    else:
        print(decrypt(text, shift))


## Наверное тесты тут уже не нужны.
if __name__ == "__main__":
    cae_ciph()