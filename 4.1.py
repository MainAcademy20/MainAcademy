import math
import sys

orbital_radius = {"Mercury": 58, "Venus": 108, "Earth": 150, "Mars": 228, "Jupiter": 778, "Saturn": 1429,
                  "Uranus": 2871, "Neptune": 4504}  # millions of kilometres
orbital_speed = {"Mercury": 47.87, "Venus": 35.02, "Earth": 29.78, "Mars": 24.13, "Jupiter": 13.07, "Saturn": 9.69,
                 "Uranus": 6.81, "Neptune": 5.43}  # kilometres per second
planet1 = input("Planet 1: ")
planet2 = input("Planet 2: ")


def planet_year_day(planet):
    radius = orbital_radius[planet] * 1000000  # turning millions of kilometres to kilometres
    speed = orbital_speed[planet]
    year_sec = 2 * math.pi * radius / speed
    year_day = year_sec / (60 * 60 * 24)
    return year_day


def bigger_year(planet1, planet2):
    planet_year1 = planet_year_day(planet1)
    planet_year2 = planet_year_day(planet2)
    print('The year is {} days on {}'.format(planet_year1, planet1))
    print('The year is {} days on {}'.format(planet_year2, planet2))
    bigger_year = planet1 if planet_year1 > planet_year2 else planet2  # Looking which year is bigger
    print("The {} year is bigger".format(bigger_year))



bigger_year(planet1, planet2)
