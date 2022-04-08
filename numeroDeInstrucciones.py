# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 09:55:26 2022

@author: IPIMENTEM
"""

import numpy as np

def numeroDeInstrucciones(f,tr):
    T = 1/f
    return tr//T

F = 16e6/1024
print("Caso NUM_A=1")
print(numeroDeInstrucciones(F, 0.6))
print(numeroDeInstrucciones(F, 0.15))
print("*-*-*-*-*-*-*-*-*-*-*-*-*-")
print("Caso NUM_A=2")
print(numeroDeInstrucciones(F, 1.2))
print(numeroDeInstrucciones(F, 0.3))
print("*-*-*-*-*-*-*-*-*-*-*-*-*-")
print("Caso NUM_A=3")
print(numeroDeInstrucciones(F, 1.8))
print(numeroDeInstrucciones(F, 0.45))
print("*-*-*-*-*-*-*-*-*-*-*-*-*-")
print("Caso NUM_A=4")
print(numeroDeInstrucciones(F, 2.4))
print(numeroDeInstrucciones(F, 0.6))
print("*-*-*-*-*-*-*-*-*-*-*-*-*-")
print("Caso NUM_A>=5")
print(numeroDeInstrucciones(F, 3))
print(numeroDeInstrucciones(F, 0.75))
print("*-*-*-*-*-*-*-*-*-*-*-*-*-")
print(numeroDeInstrucciones(F, 3/4))
    