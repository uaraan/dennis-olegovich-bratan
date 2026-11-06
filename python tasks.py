class User:
    def __init__(self, username, password):
        self.username = username
        self.__password = password  

    def check_password(self, password):
        return self.__password == password


u = User("alex", "qwerty123")
print(u.check_password("qwerty123")) 
print(u.check_password("wrong"))      

# ---------- Задача 21 ----------
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Сумма должна быть положительной")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Недостаточно средств или неверная сумма")

    def get_balance(self):
        return self.__balance


acc = BankAccount("Анна", 1000)
acc.deposit(500)
acc.withdraw(200)
print(acc.get_balance())  


# ---------- Задача 22 ----------
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius 

    @property
    def celsius(self):
        return self.__celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Температура не может быть ниже -273.15 °C")
        self.__celsius = value


t = Temperature(25)
print(t.celsius)  
t.celsius = -100
print(t.celsius)
try:
    t.celsius = -300
except ValueError as e:
    print("Ошибка:", e)


# ---------- Задача 23 ----------
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price 
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Цена не может быть отрицательной")
        self._price = value


p = Product("Ноутбук", 50000)
print(p.price) 
p.price = 45000
print(p.price) 
try:
    p.price = -10
except ValueError as e:
    print("Ошибка:", e)


# ---------- Задача 24 ----------
class Age:
    def __init__(self, value):
        self.value = value  
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if not 0 <= new_value <= 120:
            raise ValueError("Возраст должен быть в диапазоне от 0 до 120")
        self._value = new_value


a = Age(30)
print(a.value)  
try:
    a.value = 150
except ValueError as e:
    print("Ошибка:", e)


# ---------- Задача 25 ----------
class Playlist:
    def __init__(self):
        self._songs = []  

    def add_song(self, song):
        self._songs.append(song)

    def remove_song(self, song):
        if song in self._songs:
            self._songs.remove(song)
        else:
            print(f"Песни '{song}' нет в плейлисте")

    def show(self):
        print("Плейлист:", self._songs)


pl = Playlist()
pl.add_song("Song A")
pl.add_song("Song B")
pl.remove_song("Song A")
pl.show()  