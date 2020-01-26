import math
import sys

planet1 = input(
    'Введите планету1 со списка (Меркурий, Венера, Земля, Марс, Юпитер, Сатурн, Уран, Нептун, Плутон):')
planet2 = input(
    'Введите планету2 со списка (Меркурий, Венера, Земля, Марс, Юпитер, Сатурн, Уран, Нептун, Плутон):')
lst_planets = ['Меркурий', 'Венера', 'Земля', 'Марс', 'Юпитер', 'Сатурн', 'Уран', 'Нептун', 'Плутон']
planets_r = [58, 108, 150, 228, 778, 1429, 2872, 4504, 5906]
planets_s = [47.87, 35.02, 29.76, 24.13, 13.07, 9.69, 6.84, 5.48, 4.75]

if planet1 not in lst_planets and planet2 not in lst_planets:
    print('Вы ввели не корректное название планеты1 и планеты2')
    exit()
elif planet1 not in lst_planets:
    print('Вы ввели не корректное название планеты1')
    exit()
elif planet2 not in lst_planets:
    print('Вы ввели не корректное название планеты2')
    exit()
else:
    print('Вы ввели планеты:', planet1, planet2)

planet_data = {
    "orbital_radius": dict(zip(lst_planets, planets_r)),
    "orbital_speed": dict(zip(lst_planets, planets_s))}


def days_in_year(planet):
    orbital_radius = planet_data['orbital_radius'][planet] * 1000000
    orbital_speed = planet_data['orbital_speed'][planet]

    planet_year = 2 * math.pi * orbital_radius / orbital_speed / (60 * 60 * 24)

    print("На планете {} {} дней".format(planet, int(planet_year)))

    return int(planet_year)


def bigger_year():
    planet_days1 = days_in_year(planet1)
    planet_days2 = days_in_year(planet2)

    is_bigger = planet1 if planet_days1 > planet_days2 else planet2

    print("Год на планете {} больше".format(is_bigger))


bigger_year()
