import os
import sys
import math

def LGC(a=1103515245, m=2**32, c=12345, no_sample=1, x0=0.1):
    """
    A function to generate Pseudo Random Number based LCG Algorithm

    args:
    a: A parameter(multiplier) which is used in the algorithm
    m: A parameter which is used in the algorithm
    c: A parameter(increment) used in the algorithm
    no_sample: The number of random numbers to generate, returns a list
    x0: The initial value from which the algorithm should start
    """
    rand = []
    x = x0
    for i in range(no_sample):
        rand.append(x)
        x = (a*x+c)%m
    return rand
