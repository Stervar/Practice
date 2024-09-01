

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

def delete_word():
    # Удаляем слово из списка
    name = input("Введите слово для удаления: ")
    if name in dictionary_wor:
        del dictionary_wor[name]
        print(f"Слово {name} удалено из списка!")
    else:
        print(f"Слово {name} не найдено в списке!")

def search_word():
    # Ищем слово на русском
    name = input("Введите слово для поиска: ")
    if name in dictionary_wor:
        print(f"Слово {name} найдено! Это слово по-английски: {dictionary_wor[name]} ")
    else:
        print(f"Слово {name} не найдено в списке!")
        
def replace_word():
    # Заменяем информацию о слове
    name = input("Введите слово на русском для замены: ")
    if name in dictionary_wor:
        new_height = input("Введите новое слово на английском: ")
        dictionary_wor[name] = new_height
        print(f"Информация о слове {name} обновлена!")
    else:
        print(f"Слово {name} не найдено в списке!")