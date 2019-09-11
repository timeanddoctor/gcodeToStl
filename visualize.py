"""Visualization of parsed data
"""
import code

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

from parse import parse_stl, parse_gcode

if __name__ == "__main__":
  df = parse_gcode("McMicken_Hall_UC")
  data = df.to_numpy()
  grab_indices = np.where(data[:, 0] == 1)[0]
  starts = data[grab_indices]
  ends = data[grab_indices + 1]

  fig = plt.figure()
  ax = fig.add_subplot(111, projection='3d')
  print("[*] Visualizing gcode")
  code.interact(local=locals())
  # not functional
  ax.plot([starts[:, 0], ends[:, 0]], [starts[:, 1], ends[:, 1]], [starts[:, 2], ends[:, 2]])