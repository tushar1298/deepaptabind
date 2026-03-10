import numpy as np

def distance(a,b):
    return np.linalg.norm(a-b)

def center_of_mass(coords):
    return np.mean(coords,axis=0)

def safe_divide(a,b):
    if b==0:
        return 0
    return a/b
