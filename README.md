# GCode to STL
The goal of this code is to come up with a function that returns an `.stl` file
as a function of an input `.gcode` file.  The hope for this is that we can create
a reliable way of assessing the output of a specific piece of `.gcode` as produced
by Cura or our own software down the line. This would be valuable for producing synthetic
data for machine learning algorithms.

We are using `.gcode` because it is the final step of instructions passed to the printer.
A `.gcode` file has all of the settings of a slicing software (in our case, Cura) baked
into it. This includes quality settings, infill, print speed, and more.

However, it may turn out that this is impossible, in which case there are two ways forward.
1. Instead of returning a single `.stl` file, the function could return information
about some distribution of solids that the `.gcode` file could produce.
2. The function may require additional information about the environment and specific features of the
printer.

## Todo
Create parsers for both filetypes.