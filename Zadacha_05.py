# Напишите программу, которая принимает на вход координаты
# двух точек и находит расстояние между ними в 2D пространстве.

# Пример:

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

print ("Введите координаты точки А:")
xA = float(input("Значение Х: "))
yA = float(input("Значение Y: "))
print ("Введите координаты точки B:")
xB = float(input("Значение Х: "))
yB = float(input("Значение Y: "))

from math import sqrt
AB = round(sqrt((xA - xB)**2 + (yA - yB)**2), 2)
print("Расстояние между двумя точками А и В =", AB)