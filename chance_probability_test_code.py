#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 13:14:54 2024

@author: lucaizzo
"""

#this is a quick and dirty code to derive the chance probability detection with sampling on two variables
#this code is just an example of the final code used in the analysis

import random, math
R = 2
niters = 100_0000
total, in_range = 0, 0
for j in range(10):
    for i in range(niters):
        x = random.uniform(20, 1000)
        y = random.uniform(1e-5, 1e-3)
        if y < 6.9e-4 and y > 2.9e-4 and x < 481.5 and x > 476.5:
            in_range += 1
        total += 1
        prob = (in_range / total)
    print(f'After {(j + 1) * niters:>8} iterations, chance probability is {prob:.08f} ', flush = True)