# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import math

while True:
    try:
        x = int(input("Введите x = "))
        break
    except ValueError:
        print("Введите корректное значение!")
y = math.cos(x**math.pi) +  math.e**2/(math.sin(x) + 1)
print ("Ответ", y, sep = ":", end = ".")