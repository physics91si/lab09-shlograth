import numpy as np

import particle

class Molecule:
    '''This takes in two positionsm masses, a spring consant, and equillibrium distance, and makes a molecule that      is modeled like a spring'''



    def __init__(self, p1, p2, m1, m2, k, L0):
        self.p1 = particle.Particle(p1, m1)
        self.p2 = particle.Particle(p2, m2)
        self.m1 = m1
        self.m2 = m2
        self.k = k
        self.L0 = L0

    #below you just have to subract the vectors
    def get_displ(self):
        return self.p2.pos - self.p1.pos


    #below just uses hooks law, F = kx, to calculate the force on the particles
    def get_force(self):
        return self.get_displ() * self.k

