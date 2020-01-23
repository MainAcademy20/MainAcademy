import math
import sys

orbital_radius = {"Mercury": 58, "Venus": 108, "Earth": 150, "Mars": 228, "Jupiter": 778, "Saturn": 1429,
                  "Uranus": 2871, "Neptune": 4504}  # millions of kilometres
orbital_speed = {"Mercury": 47.87, "Venus": 35.02, "Earth": 29.78, "Mars": 24.13, "Jupiter": 13.07, "Saturn": 9.69,
                 "Uranus": 6.81, "Neptune": 5.43}  # kilometres per second

def get_planet_year(planet):
    radius = orbital_radius[planet] * 1000000  # turning millions of kilometres to kilometres
    speed = orbital_speed[planet]
    year = 2 * math.pi * radius / speed
    year = year / (60 * 60 * 24)  # converting seconds to days
    return year

try:
    planet1 = input("Planet 1: ")
    planet2 = input("Planet 2: ")
    planet_year1 = get_planet_year(planet1)
    planet_year2 = get_planet_year(planet2)
    print("The year is {} days on {}".format(int(planet_year1), planet1))
    print("The year is {} days on {}".format(int(planet_year2), planet2))
    bigger_year = planet1 if planet_year1 > planet_year2 else planet2  # Looking which year is bigger
    print("The {} year is bigger".format(bigger_year))
except (KeyError):
    print("Incorrect name of planets. Try again using following names: Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune.")
