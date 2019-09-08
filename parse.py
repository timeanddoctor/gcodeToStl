"""Parsing .stl files with meshio and .gcode files manually in Pandas DataFrame format
"""

import numpy as np
import pandas as pd
import meshio
import copy

def parse_stl(obj_name):
  stl = meshio.read('assets/{}.stl'.format(obj_name))
  return stl

def parse_gcode(obj_name):
  print("[*] Parsing .gcode file")
  raw = open('assets/{}.gcode'.format(obj_name), "r").read()
  lines = raw.split("\n")
  lines = [line for line in lines if 'G0' in line or 'G1' in line]
  metadata = {
    'G':None,
    'X':None,
    'Y':None,
    'E':None,
  }
  stripped_lines = []
  for i, line in enumerate(lines):
    m = copy.copy(metadata)
    if line[1] == "1":
      m["G"] = 1
    elif line[1] == "0":
      m["G"] = 0
    else:
      raise RuntimeError("Gcode is corrupted")
    data = line.split(" ")
    keys = [d[0] for d in data]
    for k, key in enumerate(keys):
      if key in m.keys():
        m[key] = data[k][1:]
    if m["X"] is None and m["Y"] is None:
      # skip this item
      pass
    else:
      stripped_lines.append(m)
    print("[{}/{}]   ".format(i + 1, len(lines)), end="\r")
  print("[*] Finished! Converted to dataframe")
  df = pd.DataFrame(stripped_lines)

  return df

if __name__ == "__main__":
  obj_name = "McMicken_Hall_UC"
  stl = parse_stl(obj_name)
  gcode = parse_gcode(obj_name)
