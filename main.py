# 1) :Создайте класс BankAccount с атрибутом класса
# interest_rate и методами экземпляра deposit() и withdraw().
# Метод deposit() увеличивает баланс на указанную сумму,
# а метод withdraw() уменьшает баланс. При создании объекта
# этого класса, установите начальный баланс и процентную ставку.
# Затем выполните несколько операций по депозиту и снятию средств,
# используя методы экземпляра, и выведите итоговый баланс.

class BankAccount:

    def __init__(self, money, interest_rate):
        self.money = money
        self.interest_rate = interest_rate

    def deposit(self, deposit):
        self.money += deposit

    def withdraw(self, spend):
        self.money -= spend

    def pro(self):
        return self.money * (self.interest_rate/100)


bank = BankAccount(10000, 10)
bank.deposit(10000)
bank.withdraw(8000)
print(bank.money)
print(bank.pro())




# 2) Создайте класс Rectangle, у которого есть атрибуты экземпляра
# width и height. Добавьте метод экземпляра calculate_area(),
# который возвращает площадь прямоугольника (ширина * высота).
# Создайте объект этого класса и вызовите метод calculate_area().
print('*' * 50)
class Rectangle:

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height


rectangle_1 = Rectangle(5, 5)
rectangle_2 = Rectangle(8, 11)
print(rectangle_1.calculate_area())
print(rectangle_2.calculate_area())



# 3)Создайте класс Counter, у которого есть атрибут экземпляра count со
# значением 0. Добавьте методы increment() и decrement(), которые увеличивают
# и уменьшают значение атрибута count. Создайте объект этого класса и вызовите
# методы для изменения значения count.
print('*' * 50)
class Counter:

    def __init__(self):
        self.count = 0

    def increment(self, num):
        self.count += num

    def decrement(self, num):
        self.count -= num


counter = Counter()
print(counter.count)
counter.increment(5)
print(counter.count)
counter.decrement(1000)
print(counter.count)

