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
Visualizations of parsed data as a sanity check.
For .stl, this would be as simple as using a package like
pyvista.
For .gcode, we could use matplotlib to visualize the
lines followed by the printer in a 3D plot.

## Formats

### `.stl`
A list of triangular facets which are all defined by 3 points, as well
as the normal unit vector pointing outwards from the face. Used to define the inner
and outer side of a solid.

### `.gcode`
A language of instructions specific to CAM and specifically 3D printing.
The most common commands, and the ones we will be concerned with, are listed
below.

**Instructions**
* `G0` - instruction to move to a certain coordinate 
* `G1` - instruction to print at a certain coordinate

**Parameters**

These parameters can be passed to different commands
* `X`, `Y`, or `Z` - coordinate (Z is often exchanged for E)
* `F` - Update the feedrate (speed), in mm/min
* `E` - lay down some amount of filament at given Z coordinate

Here's a [good comprehensive guide](http://marlinfw.org/docs/gcode/G000-G001.html) of gcode.

## Dependencies
* numpy - `pip install numpy`
* meshio - `pip install meshio`
* pandas - `pip install pandas`
* matplotlib - `pip install matplotlib`