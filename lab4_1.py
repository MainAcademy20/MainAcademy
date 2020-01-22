import math
import sys

orbital_radius = {"Mercury": 58, "Venus": 108, "Earth": 150, "Mars": 228, "Jupiter": 778, "Saturn": 1429,
                  "Uranus": 2871, "Neptune": 4504}  # millions of kilometres
orbital_speed = {"Mercury": 47.87, "Venus": 35.02, "Earth": 29.78, "Mars": 24.13, "Jupiter": 13.07, "Saturn": 9.69,
                 "Uranus": 6.81, "Neptune": 5.43}  # kilometres per second


def year(planet):
    radius = orbital_radius[planet] * 1000000  # turning millions of kilometres to kilometres
    speed = orbital_speed[planet]
    planet_year = 2 * math.pi * radius / speed
    planet_year = planet_year / (60 * 60 * 24)  # converting seconds to days
    return planet_year


def planet_input():
    while True:
        try:
            planet = input("Planet: ")
            planet_year = year(planet)
            break
        except KeyError:
            print('Input the Planet')
    return planet, planet_year


print("Input Planet1")
planet1, planet_year1 = planet_input()
print("Input Planet2")
planet2, planet_year2 = planet_input()

print("The year is {} days on {}".format(int(planet_year1), planet1))
print("The year is {} days on {}".format(int(planet_year2), planet2))

bigger_year = planet1 if planet_year1 > planet_year2 else planet2  # Looking which year is bigger 

print("The {} year is bigger".format(bigger_year))
