#!/usr/local/bin/python3
import numpy as np

from model import *

data = UserInput()

print(data)
data.draw(0,0)
data.draw(1,1)
print(data)

print(np.sum(data.get_data()))
