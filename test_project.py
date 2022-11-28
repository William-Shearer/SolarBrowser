from project import get_solar_api, clear_console, planetary_data, orbital_data, list_moons
import contextlib
import unittest
import unittest.mock


dummy_dict = {          "englishName":"Mars",
                        "moons":[{"moon":"Phobos"},{"moon":"Deïmos"}],
                        "semimajorAxis":227939200,
                        "perihelion":206700000,
                        "aphelion":249200000,
                        "eccentricity":0.09350,
                        "inclination":1.85000,
                        "mass":{
                            "massValue":6.41712,
                            "massExponent":23},
                        "vol":{
                            "volValue":1.63180,
                            "volExponent":11},
                        "density":3.93410,
                        "gravity":3.71000,
                        "escape":5030.00000,
                        "equaRadius":3396.19000,
                        "polarRadius":3376.20000,
                        "sideralOrbit":686.98000,
                        "sideralRotation":24.62290,
                        "axialTilt":25.19,
                        "avgTemp":210,
                        "argPeriapsis":286.23100,
                        "longAscNode":49.66700}

dict_1_test = {         "Name": "Mars",
                        "Number of Moons": "2",
                        "Equatorial Radius (km)": "3,396",
                        "Polar Radius (km)": "3,376",
                        "Average Temp (Kº)": "210",
                        "Density (kg/m^3)": "3,934",
                        "Mass (kg)": "6.417e+23",
                        "Volume (km^3)": "1.632e+11",
                        "Gravity (m/s^2)": "3.71",
                        "Escape Velocity (km/sec)": "5.03",
                        "Axis Tilt (degrees)": "25.19",
                        "Sidereal Rotation (days)": "1.03"}


dict_2_test = {         "Orbital Period (years)": "1.88",
                        "Semi-Major Axis (Au)": "1.52",
                        "Long. Ascending Node (degrees)": "49.67",
                        "Arg. Periapsis (degrees)": "286.23",
                        "Perihelion (Au)": "1.38",
                        "Aphelion (Au)": "1.67",
                        "Eccentricity": "0.0935",
                        "Inclination (degrees)": "1.85"}

list_moon_test = [  [   "1.  Phobos", "2.  Deïmos", "-", "-", "-"]]

"""
Class made for test case.
Run from command line with 'python test_project.py'
"""

class Test_Solar(unittest.TestCase):


    @unittest.mock.patch("project.requests.get")
    def test_get_solar_api(self, mock_request_get):
        """
        Mocking the API request.
        A false planet returns None,
        Mars returns the dummy_dict.
        """
        mock_request_get.return_value.ok = True
        self.assertTrue(get_solar_api("Planet_X"), None)
        mock_request_get.return_value.ok = True
        self.assertTrue(get_solar_api("mars"), dummy_dict)

    def test_planetary_data(self):
        """
        Not many tests can be done here. Formatted dict returned for printing.
        Other parts of the program ensure that this function gets the correct format,
        which is the downloaded API json, represented by dummy_dict.
        """
        self.assertEqual(planetary_data(dummy_dict), dict_1_test)


    def test_orbital_data(self):
        # Formatted dict returned for printing.
        self.assertEqual(orbital_data(dummy_dict), dict_2_test)


    def test_list_moons(self):
        # Not much to test here, either. It returns a formatted list.
        self.assertEqual(list_moons(dummy_dict), list_moon_test)

    @unittest.mock.patch("project.system")
    def test_clear_console(self, mock_os_system):
        """
        Interstingly, a difficult function to test!
        Needed to suppress the printed output.
        """
        with contextlib.redirect_stdout(None):
            self.assertFalse(clear_console("nosys"))
            clear_console("posix")
            mock_os_system.assert_called_with("clear")
            clear_console("nt")
            mock_os_system.assert_called_with("cls")


if __name__ == "__main__":
    unittest.main()
