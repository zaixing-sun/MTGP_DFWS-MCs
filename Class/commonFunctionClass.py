import os
import numpy as np
from copy import deepcopy
from random import randint,seed,random



class Objectives:
    def __init__(self):
        self.Cost = None
        self.Cmax= None 
        self.ResourceUtilization = None 
        self.AlgorithmRunTime = None
        self.Speedup = None
        self.SLR = None
        self.Energy = None
        self.missDDL = None
        self.TotalTardiness = None
        self.cost_VM = None
        self.cost_FaaS = None
        self.cost_Trans = None
        self.successfulrate = None
        self.deadlineDeviation = None
    def __repr__(self):
        return 'Objectives'

