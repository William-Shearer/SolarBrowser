# SOLAR SYSTEM BROWSER

#### Video Demo:  [Introduction Video](https://youtu.be/HlEc_I9S2pI)

### Description:

#### Introduction:

This program was created by **William Shearer**, from Quito, Ecuador, for the final project of the **2022 HarvardX CS50P** online course.

The program is the **Solar System Browser**. It is a simplified, console program that allows the user to acquire static data about the solar system.

The source of the information represented is [The Solar System OpenData](https://api.le-systeme-solaire.net/en/), a French site that offers the information free via their API. More information can be obtained at this link, [Le systeme solaire](https://www.le-systeme-solaire.net/), if you are comfortable with French (or good with online translators).

The program is written exclusively in **Python 3**. External Python libraries used, which must be installed prior to use (with pip, for example) are:

- pandas 1.5.1
- requests 2.28.1
- tabulate 0.9.0

#### Project Contents:

The project contains the following files:

- project.py: The main program source code
- test_project.py: The test program.
- requirements.txt: A list of pip installable dependencies
- README.md: This file

Associated with the project is the video linked at the top of this README.

The program *(project.py)* is run from the command line of both Windows and Linux systems with:

- python project.py

The asscoiated test file *(test_project.py)* is run from the command line of both Windows and Linux systems with:

- python test_project.py

#### Usage:

The program is run from the console by entering commands. The following options are available:

- Enter the **planet's name** directly to set the target planet. Any of the name's of the eight planets may be entered (sorry, Pluto!).
- Enter **p**, once a target planet has been set, to obtain some basic **planetary data**.
- Enter **o**, once a target planet has been set, to obtain some basic **orbital data**.
- Enter **m**, once a target planet has been set, to obtain a list of the **moons** that orbit the planet (if any).
- Enter **q** to quit the program.

#### Units and Measurements:

Some familiarity with astronomical measurements will be necessary to understand the presented data. There follows a brief rundown.

**Astronomical Unit**: The average distance between the Earth and the Sun, determined as **149,597,870.7 km**.

**Zenith**: Simply, the moment when a star is at its maximum elevation above any horizon of the body it is observed from.

**Sidereal Rotation**: The rotation of a body (planet) about its axis. A sidereal day is exactly 360º of rotation about this axis. This is not the same as a solar day. Because a body is also in orbit around the star, as well as rotating on its own axis, the degrees the planet will have to rotate to achieve zenith over a given position may be more or less than 360º about its axis. On Earth, for example, the planet needs to rotate a little more than 360º from midday to midday. This latter is known as a **Solar Day**.

**Orbit**: Movement of a less massive body around a central, high mass body.

**Eccentricity**: The orbit of any body is rarely completely circular around the orbited body. Usually, they describe an ellipse around the central body, with the central body at one of the foci. There is a point of closest proximity, known as the **periapsis**, between the central body and the orbiting body, and roughly on the diametrically opposing position, a point of furthest elongation, known as the **apoapsis**.

**Semi Major Axis**: The longest radius of an ellipse. This is *not* the same distance as the apoapsis, it should be noted, because the central body is not (usually) concentric with the ellipse.

**Northern Vernal Equinox**: Also known as the **First Point of Aries**. It is a major reference point for orbital measurements of the Sol solar system, and is determined as the point around the orbit of Earth when the March (Vernal) Equinox (transition of the Sun from one hemisphere to another) occurs.

**Inclination**: Orbits, being three dimensional, are therefore not all on the same plane as Earth for each respective planet. However, the plane of Earth is used as a reference for the rest of the planets. Which planet is the most inclined, relative to Earth? The Solar System Browser will help you find out (shameless plug)!

**Longitude of Ascending Node**: When an orbit of another planet in inclined, relative to the "flat" plane of Earth, approximately half of that planet's orbit will occur south of Earth, and the remainder north. The northern part is the ascending segment, roughly speaking. The point at which the trajectory of the planet's orbit crosses the plane of Earth's orbit (incidentally, known as the **ecliptic**) into the ascending segment is the ascending node. It is identified by its displacement around the orbit, in degrees, from the First Point of Aries.

**Argument of Periapsis**: The point at which the orbiting body is at its periapsis, as measured in degrees, from the Longitude of the Ascending Node. With this data, it becomes possible to visualize the shape of a planet's orbit.

**Eccentricity**: A measure of how eccentric the orbit is. In effect, it is a measure of how "flattened" the circularity of the orbit appears. In slightly more complex terms, calculating the arcsine of the eccentricity reveals an "apparent tilt" factor, which is translated into how many degrees off a perpendicular view of a circular orbit the real orbit appears.

**Kelvin**: A unit of temperature, measured from Absolute Zero, with the same interval as Celcius.

#### Further Reading

[FAA - Describing Orbits](https://www.faa.gov/about/office_org/headquarters_offices/avs/offices/aam/cami/library/online_libraries/aerospace_medicine/tutorial/media/iii.4.1.4_describing_orbits.pdf)

#### Further Development Possibilities

Outside of the scope of the CS50P project, the source could form the basis of a website or a GUI application, possibly using [tkinter](https://docs.python.org/3/library/tkinter.html), that provides graphical representation of the solar system.

Additionally, the Python library [SkyField](https://rhodesmill.org/skyfield/) can be integrated to obtain realtime osculating data. In fact, this project, as presented, is one of two "prototypes" that were created for the CS50P final project, one utilizing **SkyField**, and the other the **le-systeme-solaire API**.

The author opted for utilizing the API instead of the library because the trend of accessing external data online appears to be more popular, of late.

#### Video Credits

The video was created with **Microsoft ClipChamp**, video editor free edition. It includes the links mentioned above for **le-systeme-solaire** and the **FAA documentation library**. Still plates were created with **Paint.net**, free image creation and processing software. The closing animation was made with **Blender**, free 3D animation software. The textures utilized to create the planet can be found, free, at [solarsystemscope.com](https://www.solarsystemscope.com/textures/), for those interested.

With many thanks for kind your attention, all the best,

The author.