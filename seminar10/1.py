import re
import hashlib

def check_password_complexity(password):
    if len(password) < 8:
        return False
    if not re.search("[a-z]", password):
        return False
    if not re.search("[A-Z]", password):
        return False
    if not re.search("[0-9]", password):
        return False
    return True

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def main():
    password = input("Введите пароль: ")

    if check_password_complexity(password):
        hashed_password = hash_password(password)
        print("Пароль соответствует требованиям сложности.")
        print("Хэш пароля:", hashed_password)
    else:
        print("Пароль не соответствует требованиям сложности.")

if __name__ == "__main__":
    main()
