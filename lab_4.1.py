import math
import sys

orbital_radius = {"Mercury": 58, "Venus": 108, "Earth": 150, "Mars": 228, "Jupiter": 778, "Saturn": 1429, "Uranus": 2871, "Neptune": 4504}  # millions of kilometres
orbital_speed = {"Mercury": 47.87, "Venus": 35.02, "Earth": 29.78, "Mars": 24.13, "Jupiter": 13.07, "Saturn": 9.69, "Uranus": 6.81, "Neptune": 5.43} # kilometres per second

def year_duration (planet):
    orbital_radius_local = orbital_radius[planet] * 1000000  # turning millions of kilometres to kilometres
    orbital_speed_local = orbital_speed[planet]
    planet_year = 2 * math.pi * orbital_radius_local / orbital_speed_local
    return planet_year, planet
planet_year1, planet1 = year_duration(input("Planet 1: "))
planet_year2, planet2 = year_duration(input("Planet 2: "))

bigger_year = planet1 if planet_year1 > planet_year2 else planet2  # Looking which year is bigger 

print("The {} year is bigger".format(bigger_year))

