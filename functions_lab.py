import math
import sys

orbital_radius = {"Mercury": 58, "Venus": 108, "Earth": 150, "Mars": 228, "Jupiter": 778, "Saturn": 1429, "Uranus": 2871, "Neptune": 4504}  # millions of kilometres
orbital_speed = {"Mercury": 47.87, "Venus": 35.02, "Earth": 29.78, "Mars": 24.13, "Jupiter": 13.07, "Saturn": 9.69, "Uranus": 6.81, "Neptune": 5.43} # kilometres per second

planet1 = input("Planet 1: ")
planet2 = input("Planet 2: ")

def funct_planet(planet_ ) :

    orbital_radius_ = orbital_radius[planet_] * 1000000  # turning millions of kilometres to kilometres
    orbital_speed_ = orbital_speed[planet_]

    planet_year_ = 2 * math.pi * orbital_radius_ / orbital_speed_
    planet_year_ = planet_year_ / (60 * 60 * 24) # converting seconds to days

    print("The year is {} days on {}".format(int(planet_year_), planet_))
    return planet_year_

planet_year1 = funct_planet(planet1)
planet_year2 = funct_planet(planet2)

bigger_year = planet1 if planet_year1 > planet_year2 else planet2  # Looking which year is bigger
print("The {} year is bigger".format(bigger_year))