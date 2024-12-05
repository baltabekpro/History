from itertools import product
from base64 import b64decode
from Crypto.Cipher import AES

# Зашифрованный текст
encrypted_text = """rxoOiym9r3G88Wx093O7nCbF8bRooNdmJJaHTVGpbtG4woZpra1sFpgiETfHZ8saN3NCTPssWP4HJg6UtQlfZ1NlJfuIIsbkF6iYouZKlgG5de9DUr2ZoYccxGrRIPPEFvJrXLPHtxYeo5Sjrn2qrtSMY764X9oyC27cyXyVrLvbyZmcslAgTdX0gzVSkKu1s4JGH+F/YWkYFiGvydbUanFUvkMjuPw3GpBryZK4vVeW3GH24rQvZXXqnKA+LGqdt8M3Fx6x9vNRtAJzi+0/Jnp+LlZlxNBi+ulkWIJjL1aWwpdt8TMF1MNCKf2HsBIo9jh4HQ0w1Sbd59pzTJBklr9ZI1qjWgJ1La+CN+Em4lEd2iJG4sltRfV5c6l9VamF"""

# Декодирование Base64
encrypted_data = b64decode(encrypted_text)

# Базовая часть ключа
base = "secret"

# Остальные символы для дополнения
chars = "abcdefghijklmnopqrstuvwxyz0123456789"

# Генерация возможных ключей и расшифровка
def unpad(s):
    """Удаляет паддинг из данных."""
    return s[:-s[-1]]

found = False
for combo in product(chars, repeat=(16 - len(base))):
    key = base + "".join(combo)
    try:
        cipher = AES.new(key.encode(), AES.MODE_ECB)
        decrypted_data = cipher.decrypt(encrypted_data)
        decrypted_text = unpad(decrypted_data).decode('utf-8')
        print(f"Ключ найден: {key}")
        print(f"Расшифрованный текст: {decrypted_text}")
        found = True
        break
    except Exception:
        continue

if not found:
    print("Ключ не найден.")
