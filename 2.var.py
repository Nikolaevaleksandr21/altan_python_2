# # Переменные, функция input (), типы данных, операции

# #PEP8

# # Операция ввода данных
# # input всегда возвращает строку
# in_1 = input ( "Введите первое число : " )
# in_2 = input ( "Введите второе число : " )

# # result = in_1 + in_2 # конкатенация

# result = int (in_1) + int (in_2) # Сложение

# print (result)

# Типы данных
int_var = 123

# Тип данных "числа с плавающей точкой" (пишутся через точку)
float_var = 3.14

# строковой тип данных (всегда пишутся с кавычками)
str_var = "Текст"
char_var = 'A' # Символ

# Булевы типы данных (Джордж Буль)
boolean_t = True # "Истина" (логическая 1)
boolean_f = False # "Ложь" (логический 0 )

# Способ форматрования строк f-string
name = "George"
age = 56

s = f"Имя: {name} Возраст: {age}"

# print (s)

# Арифметические операции 
x = 5
y = 7

# Сложение
res = x + y

# Вычитание
res = x - y

# Умножение
res = x * y

# Обычное деление (всегда возвращает float)
x = 10
y = 5
res = x / y

# Целочисленное деление
res = x // y

# Деление по остатку
x = 10
y = 7
res = x % y

# Возвдение в степень
res = x ** y

print (res)
