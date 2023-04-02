#1. Написати клас для створення і роботи з хеш- таблицями. клас повинен містити наступні функції:
# -створення хеш-таблиці  заданої довжини,
# -пошук, додавання і видалення нових елементів,
# - друкування хеш-таблиці,
# - виправлення колізій

BLANK = object()

class HashTable:
    def __init__(self, capacity=5):
        self.values = capacity*[BLANK]

    def __len__(self):
        return len(self.values)

    def __setitem__(self, key, value):
        index = self._index(key)
        if self.values[index] is BLANK:
            self.values[index] = value
        else:
            while index < len(self) and self.values[index] is not BLANK:
                index += 1
                if self.values[index] is BLANK:
                    self.values[index] = value
                else:
                    IndexError("Not have enough space")

    def __getitem__(self, key):
        value = self.values[self._index(key)]
        if value is BLANK:
            raise KeyError(key)
        return value

    def __delitem__(self, key):
        self.values[self._index(key)] = BLANK

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

    def _index(self, key):
        return hash(key) % len(self)

    def __repr__(self):
        final_list = []
        for i in range(len(self.values)):
            if self.values[i] == BLANK:
                final_list.append('None')
            else:
                link_list = self.values[i]
                string = link_list.__str__()
                final_list.append(string)
        return ', '.join(final_list)

if __name__=="__main__":
    ht = HashTable(5)

    # ht['d'] = 5
    # ht['x'] = 7
    # ht['b'] = 6
    # ht['a'] = 9
    # ht['c'] = 4
    # print(len(ht))
    # print(ht)


#2.Написати програми для реєстрації  і авторизації користувача з наступним функціоналом:
# - отримання в інтерактивному режимі логіну та пароля користувача,
# - верифікація пароля і його шифрування за алгоритмом шифрування,
# - запис пари логін-пароль у словник з перевіркою на колізії,
# - авторизація  користувача за логіном і паролем.
import string
import hashlib
import os


user_dict = {}
# sign up
login, pasword = input("Please sign up. Print your login and pasword: ").split()
user_dict[login] = pasword
if len(pasword) <= 6:
    print('Your pasword too short')
else:
    print('Your password was verification successful')
salt = os.urandom(32)

pasword_encryption = hashlib.pbkdf2_hmac('sha256', 'password'.encode('utf-8'),salt, 10000)
user_dict[login] = pasword_encryption
#log in
log_new, pasword_new = input("Please log in. Print your login and pasword: ").split()

new_key = hashlib.pbkdf2_hmac('sha256', 'pasword_new'.encode('utf-8'),salt, 10000)
try:
    value = user_dict[log_new]
    print("User", log_new, "exists")
except KeyError:
    print("User is not registered")

if pasword_new == user_dict[log_new]:
    print('Pasword checked')
else:
    print('Wrong pasword')

