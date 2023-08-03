"""
Created on Wed Aug 2 17:42:40 2023

@author: evankurian
"""
import numpy as np

import loanPmt as ls

PV=1000
r = 5
n = 12

pmt = ls.computesPmt(PV, r, n)
print(f"pmt = {pmt}")

pmt2 = ls.computesPmt(1000, 5, 12)
print(f"and the pmt also is {pmt2}")
