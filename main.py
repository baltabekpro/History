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
    """Проверяет, состоит ли текст из читаемых символов."""
    return all(c in string.printable for c in text)

# Функция для подбора ключа
def brute_force_key():
    # Длина оставшихся символов в ключе
    remaining_length = 16 - len(base)
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
                    print(f"Ключ найден: {key}")
                    print(f"Расшифрованный текст:\n{decrypted_text}")
                    return
            except:
                continue
        except Exception:
            continue
    print("Ключ не найден.")

# Запуск подбора ключа
brute_force_key()
