

# Простейшие арифметические операции (1)
# 
# Написать функцию arithmetic, принимающую 3 аргумента: первые 2 - числа, третий - операция, которая должна быть произведена над ними. Если третий аргумент +, сложить их; если —, то вычесть; * — умножить; / — разделить (первое на второе). В остальных случаях вернуть строку "Неизвестная операция".






# def arithmetic(a, b, operation):
#     """
#     Функция, выполняющая арифметические операции над двумя числами.
# 
#     Args:
#         a (int): Первое число.
#         b (int): Второе число.
#         operation (str): Операция, которую нужно выполнить. Может быть "+", "-", "*", "/".
# 
# 
#     Returns:
#         int или float: Результат операции. Если операция неизвестна, возвращает строку "Неизвестная операция".
#     """
#     if operation == "+":
#         return a + b
#     elif operation == "-":
#         return a - b
#     elif operation == "*":
#         return a * b
#     elif operation == "/":
#         if b != 0:
#             return a / b
#         else:
#             return "Деление на ноль!"
#     else:
#         return "Неизвестная операция"
# 
# 
# Пример использования функции
# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))
# operation = input("Введите операцию (+, -, *, /): ")
# 
# result = arithmetic(a, b, operation)
# print("Результат:", result)
# 
# def main():
#     while True:
#         print("Меню:")
#         print("1. Прибавить два числа")
#         print("2. Убавить два числа ")
#         print("3. Умножить два числа")
#         print("4. Разделить два числа")
#         print("5. Выход")
# 
#         choice = int(input("Выберите пункт меню: "))
# 
#         if choice == 1:
#             a = int(input("Введите первое число: "))
#             b = int(input("Введите второе число: "))
#             print("Результат:", arithmetic(a, b, "+"))
#         elif choice == 2:
#             a = int(input("Введите первое число: "))
#             b = int(input("Введите второе число: "))
#             print("Результат:", arithmetic(a, b, "-"))
#         elif choice == 3:
#             a = int(input("Введите первое число: "))
#             b = int(input("Введите второе число: "))
#             print("Результат:", arithmetic(a, b, "*"))
#         elif choice == 4:
#             a = int(input("Введите первое число: "))
#             b = int(input("Введите второе число: "))
#             print("Результат:", arithmetic(a, b, "/"))
#         elif choice == 5:
#             break
#         else:
#             print("Неверный выбор!")
# 
# if name == "main":
#     main()
#     
   



    
# Високосный год (2)
# Написать функцию is_year_leap, принимающую 1 аргумент — год, и возвращающую True, если год високосный, и False иначе.
    
    



#     
#  def is_year_leap(year):
#     if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
#         return True
#     else:
#         return False
#         year = int(input("Введите год: "))
#          result = is_year_leap(year)
# print(result)
#    
# 
# 
# 
# 
#  
### Квадрат (3)
 
## Написать функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения (с помощью кортежа): периметр квадрата, площадь квадрата и диагональ квадрата.
# 


# import math
# 
# def square(side):
#     """
#     Возвращает периметр, площадь и диагональ квадрата.
# 
#     Args:
#         side (int): Сторона квадрата.
# 
#     Returns:
#         tuple: (периметр, площадь, диагональ)
#     """
#     perimeter = 4 * side
#     area = side ** 2
#     diagonal = side * math.sqrt(2)
#     return perimeter, area, diagonal
# 





## Времена года (4)
 
## Написать функцию season, принимающую 1 аргумент — номер месяца (от 1 до 12), и возвращающую время года, которому этот месяц принадлежит (зима, весна, лето или осень). 

 
 
# def season(a):
#   
#     if a in [1, 2, 3]:
#         return "Зима"
#     elif a in [4, 5, 6]:
#         return "Весна"
#     elif a in [7, 8, 9]:
#         return "Лето"
#     elif a in [10, 11, 12]:
#         return "Осень"
#     else:
#         return "Неправильный номер месяца"

