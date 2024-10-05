import re
import os

palabra = "L2C5 L1C6   L2C12 L3C4      L3C10"
matches = re.findall(r'L(\d+)', palabra)
max_num = max(map(int, matches))
print(max_num)
