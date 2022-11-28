import requests
import json
import pandas as pd
from os import name as os_name
from os import system
from tabulate import tabulate

"""
Solar System Browser.
By William Shearer, November 2022, for CS50P Final Project.
Programmed with Python3, Windows / Linux compatible.
"""

# A list of the solar system planets, for command comparison.
planet_list = [ "mercury",
                "venus",
                "earth",
                "mars",
                "jupiter",
                "saturn",
                "uranus",
                "neptune"]

#  *************** MAIN ***************

def main():
    """
    Contains code for handling the menu and input commands.
    """
    set_planet = "None"
    target_planet = None

    # WHILE LOOP STARTS HERE...

    while True:
        """
        Start of the loop. Screen is always cleared, and QG displayed.
        Prompt for input.
        """
        if clear_console(os_name) == False:
            exit("OS clear screen issue. Program terminated.\n")

        print("Quick Guide\nType planet name to set target\n(p) for planetary, (o) for orbital, (m) for moon list, (q) to quit")
        print(f"Currently set planet: {set_planet.upper()}")

        command = input("Your command: ").strip().lower()

        if command == "q":
            """
            Quit the program. Exit right out, no messing around.
            Trusting Python garbage collector.
            """
            clear_console(os_name)
            exit("Program terminated. Thank you.\n")

        if command in planet_list:
            """
            Get the planet general data from the API.
            """
            set_planet = command
            url = fr"https://api.le-systeme-solaire.net/rest.php/bodies/{set_planet}"

            if (target_planet := get_solar_api(url)):
                print("\nData acquired successfully.")
                input("\nHit ENTER to continue.")
            else:
                print("\nBad response from API.")
                input("\nHit ENTER to continue.")

        elif command == "p":
            """
            Obtain the data relevant to planetary information from the downloaded json.
            Print using pandas.
            """
            if set_planet != "None":
                planet_data = planetary_data(target_planet)
                pd_data = pd.DataFrame.from_dict(planet_data, orient = "index", columns = ["DATA"])
                print(f"\nPlanetary data of {set_planet.capitalize()}")
                print(pd_data)
                input("\nHit ENTER to continue.")
            else:
                print("\nNo target planet set.")
                input("\nHit ENTER to continue.")

        elif command == "o":
            """
            Obtain the data for orbital information to be displayed.
            Print using pandas.
            """
            if set_planet != "None":
                planet_data = orbital_data(target_planet)
                pd_data = pd.DataFrame.from_dict(planet_data, orient = "index", columns = ["DATA"])
                print(f"\nOrbital data of {set_planet.capitalize()}")
                print(pd_data)
                input("\nHit ENTER to continue.")
            else:
                print("\nNo target planet set.")
                input("\nHit ENTER to continue.")

        elif command == "m":
            """
            Obtain the names of the moons of a planet, if it has any.
            Returned formatted to be printed by tabulate.
            """
            if set_planet != "None":
                moon_data = list_moons(target_planet)

                if moon_data != None:
                    print(f"\nList of moons of {set_planet.capitalize()}")
                    print(tabulate(moon_data))
                    input("\nHit ENTER to continue.")
                else:
                    print(f"\nTarget planet {set_planet.capitalize()} has no moons.")
                    input("\nHit ENTER to continue.")

            else:
                print("\nNo target planet set.")
                input("\nHit ENTER to continue.")

        else:
            """
            Default, re-enter the loop.
            """
            print("\nInvalid command!")
            input("\nHit ENTER to continue")

            # END OF MAIN LOOP


# *************** FUNCTIONS ***************

# API CALL FUNCTION

def get_solar_api(body_url):
    """
    API call.
    If anything other than a good response, None is returned.
    """
    try:
        response = requests.get(body_url)
        return_data = response.json()
    except requests.exceptions.RequestException:
        return_data = None

    return return_data

    # END OF API CALL


# PLANETARY DATA FUNCTION

def planetary_data(t_planet):
    """
    Format and return the data recovered from the API.
    This subroutine formats planetary data.
    """
    data_dict = dict()
    # Build the scientific notation.
    mass = f"{(t_planet['mass']['massValue'] * (10 ** t_planet['mass']['massExponent'])):.3e}"
    volume = f"{(t_planet['vol']['volValue'] * (10 ** t_planet['vol']['volExponent'])):.3e}"

    # Human readability. If the planet's rotation is more than 24 hours, express as days. Venus is a prime example.

    if t_planet['sideralRotation'] > 24.0 or t_planet['sideralRotation'] < -24.0:
        rotation = t_planet['sideralRotation'] / 24.0
        period = "days"
    else:
        rotation = t_planet['sideralRotation']
        period = "hours"

    if rotation < 0.0:
        prefix = "(R) "
        rotation = abs(rotation)
    else:
        prefix = ""

    """
    The data to be returned built into a dict.
    """
    data_dict["Name"] = t_planet["englishName"]

    # Avoid problems when a planet has not got any moons.

    data_dict["Number of Moons"] = (lambda: f"{len(t_planet['moons'])}", lambda: f"{0}")[t_planet['moons'] == None]()
    data_dict["Equatorial Radius (km)"] = f"{int(t_planet['equaRadius']):,}"
    data_dict["Polar Radius (km)"] = f"{int(t_planet['polarRadius']):,}"
    data_dict["Average Temp (Kº)"] = f"{int(t_planet['avgTemp'])}"
    data_dict["Density (kg/m^3)"] = f"{int(t_planet['density'] * 1000.0):,}"
    data_dict["Mass (kg)"] = mass
    data_dict["Volume (km^3)"] = volume
    data_dict["Gravity (m/s^2)"] = f"{(t_planet['gravity']):,.2f}"
    data_dict["Escape Velocity (km/sec)"] = f"{(t_planet['escape'] / 1000.0):,.2f}"
    data_dict["Axis Tilt (degrees)"] = f"{(t_planet['axialTilt']):,.2f}"
    data_dict[f"Sidereal Rotation ({period})"] = f"{prefix}{rotation:,.2f}"

    return data_dict

    # END OF PLANETARY DATA


# ORBITAL DATA FUNCTION

def orbital_data(t_planet):
    """
    Format and return the data recovered from the API.
    This subroutine formats orbital data.
    """
    data_dict = dict()

    # Astronimical unit.

    Au = 149597870.7

    # Adjust the output to make more human sense. If more than 365 days, express orbit as years.

    if t_planet["sideralOrbit"] > 365.256:
        orbit = f"{(t_planet['sideralOrbit'] / 365.256):,.2f}"
        period = "years"
    else:
        orbit = f"{t_planet['sideralOrbit']:,.2f}"
        period = "days"

    """
    The data to be returned built into a dict.
    """
    data_dict[f"Orbital Period ({period})"] = orbit
    data_dict["Semi-Major Axis (Au)"] = f"{(t_planet['semimajorAxis'] / Au):,.2f}"
    data_dict["Long. Ascending Node (degrees)"] = f"{t_planet['longAscNode']:.2f}"
    data_dict["Arg. Periapsis (degrees)"] = f"{t_planet['argPeriapsis']:.2f}"
    data_dict["Perihelion (Au)"] = f"{(t_planet['perihelion'] / Au):,.2f}"
    data_dict["Aphelion (Au)"] = f"{(t_planet['aphelion'] / Au):,.2f}"
    data_dict["Eccentricity"] = f"{t_planet['eccentricity']:.4f}"
    data_dict["Inclination (degrees)"] = f"{t_planet['inclination']}"

    return data_dict

    # END OF ORBITAL DATA


# MOON LIST FUNCTION

def list_moons(t_planet):
    """
    This subroutine recovers the names of the moons from the API.
    Formats the dinformation to be tabulated, so that it does not
    make a long list in the console after execution.
    """
    moon_list = list()
    temp_list = list()
    if t_planet["moons"] == None:
        return None
    else:
        len_moons = len(t_planet["moons"])
        if len_moons > 5:
            if (len_moons % 5) != 0:
                mn_iter = (int(len_moons / 5) * 5) + 5
            else:
                mn_iter = len_moons
        else:
            mn_iter = 5

        for i in range(mn_iter):
            """
            Creates five columns, with as many rows as needed, for
            the names of the moons to be efficiently tabulated.
            """
            if i < len_moons:
                temp_list.append(f"{i + 1}.\t{t_planet['moons'][i]['moon']}".expandtabs(4))
            else:
                temp_list.append("-")

            if ((i + 1) % 5) == 0:
                moon_list.append(temp_list.copy())
                temp_list.clear()

        return moon_list

        # END OF MOON LIST


# CLEAR SCREEN FUNCTION

def clear_console(osn):
    """
    General function for clearing the console based on the os.
    """
    if osn == "nt" or osn == "posix":
        system((lambda:"cls", lambda:"clear")[osn == "posix"]())
        print("SOLAR SYSTEM BROWSER\n")
        return True

    return False

    # END OF CLEAR SCREEN


if __name__ == "__main__":
    main()


"""
*PS NOTES:*
[REQUIREMENTS.TXT]
-
How to make a requirements.txt file automatically.
1. Install 'pip install pipreqs'
2. Run 'python -m  pipreqs.pipreqs .' (Note the '.' at the end for CWD).
-
The requirements.txt file will be created. To install the dependencies, do:
3. 'pip install -r requirements.txt'
"""


