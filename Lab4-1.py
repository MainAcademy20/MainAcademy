import math

orbital_radius = {"Mercury": 58, "Venus": 108, "Earth": 150, "Mars": 228, "Jupiter": 778, "Saturn": 1429,
                  "Uranus": 2871, "Neptune": 4504}  # millions of kilometres
orbital_speed = {"Mercury": 47.87, "Venus": 35.02, "Earth": 29.78, "Mars": 24.13, "Jupiter": 13.07, "Saturn": 9.69,
                 "Uranus": 6.81, "Neptune": 5.43}  # kilometres per second


def get_name_planet():
    planet1_local = input("Planet 1: ")
    planet2_local = input("Planet 2: ")
    return planet1_local, planet2_local


def get_bigger_year(*args):
    return max(args) if args else 'Not enough parameters'


def get_count_of_days_in_year(planet):
    orbital_radius_local = convert_millions_of_kilometres_to_kilometres(planet)  # turning millions of kilometres to kilometres
    orbital_speed_local = orbital_speed[planet]
    planet_year = 2 * math.pi * orbital_radius_local / orbital_speed_local
    planet_year = planet_year / (60 * 60 * 24)  # converting seconds to days
    print("The year is {} days on {}".format(int(planet_year), planet))
    return planet_year


def convert_millions_of_kilometres_to_kilometres(planet):
    return orbital_radius[planet] * 1000000


if __name__ == '__main__':
    planet1, planet2 = get_name_planet()

    try:
        planet_year1 = get_count_of_days_in_year(planet1)
        planet_year2 = get_count_of_days_in_year(planet2)
        print("The {} year is bigger".format(get_bigger_year(planet_year1, planet_year2)))
    except KeyError:
        print('Wrong planet name was entered!')
