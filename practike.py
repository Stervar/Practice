

# Простейшие арифметические операции (1)

# Написать функцию arithmetic,
# принимающую 3 аргумента: 
# первые 2 - числа, третий - операция,
# которая должна быть произведена над ними.
# Если третий аргумент +, сложить их; если —,
# то вычесть; * — умножить; / — разделить (первое на второе).
# В остальных случаях вернуть строку "Неизвестная операция".



a =int(input("Введите первое любое число "))
    
 a =int(input("Введите второе любое число "))
  
dictionary_wor = {}
 
def add_word():
    # Добавляем новое слово
    name = input("Введите слово на русском: ")
    height = input("Введите слово на английском: ")
    dictionary_wor[name] = height
    print(f"Слово {name} добавлено в список!")