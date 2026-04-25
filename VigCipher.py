"""
Шифр Виженера для русского текста
Чтение текста из файла plaintext.txt
Сохранение результата в ciphertext.txt
"""

ALPHABET = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
KEY = "СИНЕРГИЯ"

INPUT_FILE = "plaintext.txt"
OUTPUT_FILE = "ciphertext.txt"

def vigenere_encrypt(text: str, key: str, alphabet: str) -> str:
    text = text.upper()
    key = key.upper()

    char_to_index = {char: i for i, char in enumerate(alphabet)}
    alphabet_size = len(alphabet)

    key_shifts = [char_to_index[char] for char in key]

    result = []
    key_index = 0

    for char in text:

        if char in char_to_index:

            text_pos = char_to_index[char]
            key_shift = key_shifts[key_index % len(key_shifts)]

            encrypted_pos = (text_pos + key_shift) % alphabet_size

            result.append(alphabet[encrypted_pos])

            key_index += 1

        else:
            result.append(char)

    return "".join(result)

def read_file(filename: str) -> str:
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()

def write_file(filename: str, text: str):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)

def main():

    print(f"Чтение файла: {INPUT_FILE}")
    plaintext = read_file(INPUT_FILE)

    print("Шифрование...")
    ciphertext = vigenere_encrypt(plaintext, KEY, ALPHABET)

    print(f"Сохранение в файл: {OUTPUT_FILE}")
    write_file(OUTPUT_FILE, ciphertext)

    print("Готово.")

if __name__ == "__main__":
    main()