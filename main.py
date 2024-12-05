from itertools import product
from base64 import b64decode
from Crypto.Cipher import AES
import string

# Зашифрованный текст
encrypted_text = """rxoOiym9r3G88Wx093O7nCbF8bRooNdmJJaHTVGpbtG4woZpra1sFpgiETfHZ8saN3NCTPssWP4HJg6UtQlfZ1NlJfuIIsbkF6iYouZKlgG5de9DUr2ZoYccxGrRIPPEFvJrXLPHtxYeo5Sjrn2qrtSMY764X9oyC27cyXyVrLvbyZmcslAgTdX0gzVSkKu1s4JGH+F/YWkYFiGvydbUanFUvkMjuPw3GpBryZK4vVeW3GH24rQvZXXqnKA+LGqdt8M3Fx6x9vNRtAJzi+0/Jnp+LlZlxNBi+ulkWIJjL1aWwpdt8TMF1MNCKf2HsBIo9jh4HQ0w1Sbd59pzTJBklr9ZI1qjWgJ1La+CN+Em4lEd2iJG4sltRfV5c6l9VamF"""

# Декодирование Base64
encrypted_data = b64decode(encrypted_text)

# Базовая часть ключа
base = "secret"

# Остальные символы для дополнения
chars = "abcdefghijklmnopqrstuvwxyz0123456789"

# Функция для удаления паддинга
def unpad(s):
    return s[:-s[-1]]

# Функция для проверки читаемости текста
def is_readable(text):
    """Проверяет, состоит ли текст из читаемых символов (латиница, кириллица, цифры, знаки)."""
    allowed_chars = string.ascii_letters + string.digits + string.punctuation + string.whitespace + \
                    "абвгдежзийклмнопрстуфхцчшщъыьэюяёАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯЁ"
    return all(c in allowed_chars for c in text)

# Функция для подбора ключей и анализа текста
def brute_force_keys():
    # Длина оставшихся символов в ключе
    remaining_length = 16 - len(base)
    readable_texts = []

    for combo in product(chars, repeat=remaining_length):
        # Формируем ключ
        key = base + "".join(combo)
        try:
            # Расшифровка
            cipher = AES.new(key.encode(), AES.MODE_ECB)
            decrypted_data = cipher.decrypt(encrypted_data)
            
            # Удаление паддинга и проверка читаемости
            try:
                decrypted_text = unpad(decrypted_data).decode('utf-8')
                if is_readable(decrypted_text):
                    readable_texts.append((key, decrypted_text))
            except:
                continue
        except Exception:
            continue

    # Вывод всех читаемых текстов
    print(f"Найдено {len(readable_texts)} читаемых текстов.")
    for key, text in readable_texts:
        print(f"Ключ: {key}")
        print(f"Текст: {text}")
        print("-" * 50)

    # Поиск осмысленных текстов (опционально)
    meaningful_texts = [text for key, text in readable_texts if " " in text or any(c.isalpha() for c in text)]
    if meaningful_texts:
        print("Осмысленные тексты:")
        for text in meaningful_texts:
            print(text)
    else:
        print("Осмысленных текстов не найдено.")

# Запуск подбора ключей
brute_force_keys()
