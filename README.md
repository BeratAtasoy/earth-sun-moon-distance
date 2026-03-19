# Earth-Sun & Earth-Moon Distance Simulator

Basically, this program calculates the exact distance between the Earth-Sun and Earth-Moon based on the user's input dates. 

The code is built to be completely impervious to invalid inputs:
* Any zero, negative inputs and non-integer inputs are automatically blocked.
* Years are restricted to a 1-2100 range.
* Month values cannot exceed 12.
* Day limits are dynamically arranged according to the specific month entered. 
* It includes a flawless leap year algorithm, handling February's day count perfectly (including century exceptions).

This simulator actually mimics real orbital mechanics. Since planets don't move in perfect circles, their orbits are elliptical. This means the distances in space are constantly expanding and shrinking like a wave. To calculate the exact distance for input date, the code uses periodic wave equations and cosine function. Also, the symmetry of the cosine function allows the program to seamlessly handle negative time shifts. I set a fixed astronomical reference date (January 1, 1900) and calculate the mathematical phase shift for the day you entered. This allows the program to accurately track when the Earth is at its Perihelion/Aphelion (closest/farthest to the Sun) and when the Moon hits its Perigee/Apogee.

Basically, the code takes a simple calendar date and turns it into a precise point on an astronomical space wave.
















Once the date is verified, the simulator uses periodic wave equations and cosine functions to calculate and display the exact celestial distances.

### How to Run
```bash
python solarearth.py

Basicly it calculates the distance between Earth-Sun and Earth-Moon according to given input dates. Code is impervious to invalid inputs. Years can only be between 1-2100, month values cannot be bigger than 12, especially days are arrenged fluently according to given month input, even the leap years are calculated and month February is thought additionally. Also, values less than 0 and 0 is blocked. Then, periodic wave equations and cosine functions is used to get the exact celestial distances.
