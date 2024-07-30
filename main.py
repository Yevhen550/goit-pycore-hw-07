# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __repr__(self):
#         return f"Point(x={self.x}, y={self.y})"


# point = Point(2, 3)
# print(repr(point))


# class SimpleDict:
#     def __init__(self):
#         self.__data = {}

#     def __getitem__(self, key):
#         return self.__data.get(key, "Key not found")

#     def __setitem__(self, key, value):
#         self.__data[key] = value


# # Використання класу
# simple_dict = SimpleDict()
# simple_dict["name"] = "Boris"
# print(simple_dict["name"])
# print(simple_dict["age"])


# class BoundedList:
#     def __init__(self, min_value: int, max_value: int):
#         self.min_value = min_value
#         self.max_value = max_value
#         self.__data = []

#     def __getitem__(self, index: int):
#         return self.__data[index]

#     def __setitem__(self, index: int, value: int):
#         if not (self.min_value <= value <= self.max_value):
#             raise ValueError(
#                 f"Value {value} must be between
#                   {self.min_value} and {self.max_value}"
#             )
#         if index >= len(self.__data):
#             # Додати новий елемент, якщо індекс виходить за межі
#             self.__data.append(value)
#         else:
#             # Замінити існуючий елемент
#             self.__data[index] = value

#     def __repr__(self):
#         return f"BoundedList({self.max_value}, {self.min_value})"

#     def __str__(self):
#         return str(self.__data)


# if __name__ == "__main__":
#     temperatures = BoundedList(18, 26)

#     for i, el in enumerate([20, 22, 25, 27]):
#         try:
#             temperatures[i] = el
#         except ValueError as e:
#             print(e)

#     print(temperatures)

#
# from collections import UserDict


# class MyDict(UserDict):
#     def __add__(self, other):
#         temp_dict = self.data.copy()
#         temp_dict.update(other)
#         return MyDict(temp_dict)

#     def __sub__(self, other):
#         temp_dict = self.data.copy()
#         for key in other:
#             if key in temp_dict:
#                 temp_dict.pop(key)
#         return MyDict(temp_dict)


# if __name__ == "__main__":
#     d1 = MyDict({1: "a", 2: "b"})
#     d2 = MyDict({3: "c", 4: "d"})

#     d3 = d1 + d2
#     print(d3)

#     d4 = d3 - d2
#     print(d4)


# class ComplexNumber:
#     def __init__(self, real, imag):
#         self.real = real
#         self.imag = imag

#     def __add__(self, other):
#         return ComplexNumber(self.real + other.real, self.imag + other.imag)

#     def __sub__(self, other):
#         return ComplexNumber(self.real - other.real, self.imag - other.imag)

#     def __mul__(self, other):
#         real_part = self.real * other.real - self.imag * other.imag
#         imag_part = self.real * other.imag + self.imag * other.real
#         return ComplexNumber(real_part, imag_part)

#     def __str__(self):
#         return f"{self.real} + {self.imag}i"


# if __name__ == "__main__":
#     num1 = ComplexNumber(1, 2)
#     num2 = ComplexNumber(3, 4)
#     print(f"Сума: {num1 + num2}")
#     print(f"Різниця: {num1 - num2}")
#     print(f"Добуток: {num1 * num2}")

# from collections import UserList


# class MulArray(UserList):
#     def __init__(self, *args):
#         self.data = list(args)

#     def __mul__(self, other):
#         return self.__scalar_mul(other)

#     def __rmul__(self, other):
#         return self.__scalar_mul(other)

#     def __scalar_mul(self, other):
#         result = 0
#         for i in range(min(len(self.data), len(other))):
#             result += self.data[i] * other[i]
#         return result


# if __name__ == "__main__":
#     vec1 = MulArray(1, 2, 3)
#     vec2 = MulArray(3, 4, 5)

#     print(vec1 * vec2)
#     print(vec1 * [1, 2, 3])
#     print([1, 1, 1] * vec2)


# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def area(self):
#         return self.width * self.height

#     def __eq__(self, other):
#         if not isinstance(other, Rectangle):
#             return NotImplemented
#         return self.area() == other.area()

#     def __ne__(self, other):
#         return not self.__eq__(other)

#     def __lt__(self, other):
#         if not isinstance(other, Rectangle):
#             return NotImplemented
#         return self.area() < other.area()

#     def __le__(self, other):
#         return self.__lt__(other) or self.__eq__(other)

#     def __gt__(self, other):
#         if not isinstance(other, Rectangle):
#             return NotImplemented
#         return self.area() > other.area()

#     def __ge__(self, other):
#         return self.__gt__(other) or self.__eq__(other)


# if __name__ == "__main__":
#     rect1 = Rectangle(5, 10)
#     rect2 = Rectangle(3, 20)
#     rect3 = Rectangle(5, 10)
#     print(f"Площа прямокутників: {rect1.area()},
# {rect2.area()}, {rect3.area()}")
#     print(rect1 == rect3)  # True: площі рівні
#     print(rect1 != rect2)  # True: площі не рівні
#     print(rect1 < rect2)  # True: площа rect1  менша, ніж у rect2
#     print(rect1 <= rect3)  # True: площі рівні, тому rect1 <= rect3
#     print(rect1 > rect2)  # False: площа rect1 менша, ніж у rect2
#     print(rect1 >= rect3)  # True: площі рівні, тому rect1 >= rect3


# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __eq__(self, other):
#         if not isinstance(other, Point):
#             return NotImplemented
#         return self.x == other.x and self.y == other.y

#     def __ne__(self, other):
#         return not self.__eq__(other)

#     def __lt__(self, other):
#         if not isinstance(other, Point):
#             return NotImplemented
#         return self.x < other.x and self.y < other.y

#     def __gt__(self, other):
#         if not isinstance(other, Point):
#             return NotImplemented
#         return self.x > other.x and self.y > other.y

#     def __le__(self, other):
#         if not isinstance(other, Point):
#             return NotImplemented
#         return self.x <= other.x and self.y <= other.y

#     def __ge__(self, other):
#         if not isinstance(other, Point):
#             return NotImplemented
#         return self.x >= other.x and self.y >= other.y


# if __name__ == "__main__":
#     print(Point(0, 0) == Point(0, 0))  # True
#     print(Point(0, 0) != Point(0, 0))  # False
#     print(Point(0, 0) < Point(1, 0))  # False
#     print(Point(0, 0) > Point(0, 1))  # False
#     print(Point(0, 2) >= Point(0, 1))  # True
#     print(Point(0, 0) <= Point(0, 0))  # True


# class Person:
#     def __init__(self, age):
#         self.__age = age  # Пряме присвоєння значення атрибуту в конструкторі

#     @property
#     def age(self):
#         return self.__age  # Геттер повертає значення приватного поля

#     @age.setter
#     def age(self, value):
#         if value < 0:
#             # Валідація вхідного значення
#             raise ValueError("Вік не може бути від'ємним")
#         # Присвоєння валідного значення приватному полю
#         self.__age = value


# if __name__ == "__main__":
#     person = Person(10)
#     print(person.age)
#     person.age = -5


# class Person:
#     def __init__(self, name: str, age: int, is_active: bool, is_admin: bool):
#         self.name = name
#         self.age = age
#         self._is_active = None
#         self.__is_admin = None
#         self._is_active = is_active
#         self.__is_admin = is_admin

#     @property
#     def is_active(self):
#         return self._is_active

#     @is_active.setter
#     def is_active(self, value: bool):
#         # Тут можна додати будь-яку логіку перевірки або обробки
#         self._is_active = value

#     @property
#     def is_admin(self):
#         return self.__is_admin

#     @is_admin.setter
#     def is_admin(self, value: bool):
#         # Тут можна додати будь-яку логіку перевірки або обробки
#         self.__is_admin = value

#     def greeting(self):
#         return f"Hi {self.name}"


# if __name__ == "__main__":
#     p = Person("Boris", 34, True, False)
#     print(p.is_admin)  # Використовуємо геттер
#     p.is_admin = True  # Використовуємо сеттер
#     print(p.is_admin)


# class Multiplier:
#     def __init__(self, factor):
#         self.factor = factor

#     def __call__(self, other):
#         return self.factor * other


# # Створення екземпляра функтора
# double = Multiplier(2)
# # triple = Multiplier(3)

# # Виклик функтора
# print(double(5))  # Виведе: 10
# # print(triple(3))  # Виведе: 9


# class Counter:
#     def __init__(self):
#         self.count = 0

#     def __call__(self, *args, **kwargs):
#         self.count += 1


# counter = Counter()
# counter()
# counter()
# counter()
# counter()
# counter()
# print(f"Викликано {counter.count} разів")


# class CountDown:
#     def __init__(self, start):
#         self.current = start

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.current == 0:
#             raise StopIteration
#         self.current -= 1
#         return self.current


# if __name__ == "__main__":
#     counter = CountDown(5)
#     for count in counter:
#         print(count)


# def my_generator():
#     received = yield "Ready"
#     yield f"Received: {received}"


# gen = my_generator()
# print(next(gen))
# print(gen.send("Hello"))


# class Point:
#     def __init__(self, x, y):
#         self.__x = None
#         self.__y = None
#         self.x = x
#         self.y = y

#     @property
#     def x(self):
#         return self.__x

#     @x.setter
#     def x(self, x):
#         if isinstance(x, (int, float)):
#             self.__x = x

#     @property
#     def y(self):
#         return self.__y

#     @y.setter
#     def y(self, y):
#         if isinstance(y, (int, float)):
#             self.__y = y


# point = Point("a", 10)

# print(point.x)  # None
# print(point.y)  # 10
# # point = Point(3, "invalid")
# # print(point.x)  # 3
# # print(point.y)  # None
