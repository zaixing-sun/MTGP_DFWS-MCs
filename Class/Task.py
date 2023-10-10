# from GPClass.function_terminal import *
from copy import deepcopy
# from GPClass.multiCloudSystem import InstanceList

class Task:
    
    def __init__(self, id, name=None,namespace = None, jobsetname= None, 
                 inputs=[], outputs = [],runtime=0, MI=0,
                 terminal_task = None,Category =None,):
        self.id = id               #parents=[], storage=0 ,core=None,deepcopy(TASKTERMINAL_dict)
        self.name = name
        self.namespace = namespace
        self.Category = Category
        self.jobsetname = jobsetname
        self.runtime = runtime  # 等于权重
        self.Invocations = None
        self.MI = MI
        self.inputs =list(inputs)
        self.outputs =list(outputs)
        # self.storage =  storage
        # self.core = core
        self.terminal_task = terminal_task 
        
        self.EST = None        
        self.EFT = None       
        self.LFT = None        
        self.Assigned = None    
        self.Level = None      
        self.SubDeadline = None 
        self.XFT = 0
        self.MET= 0

        # self.currentCompletionTime = 0
        self.VMnum = None
        self.schedulingTime = None # which includes the time to caculate the priority parameters and the time to select the appraopriate instance.
        # self.VMcore = None
        self.StartTime = None 
        self.AET = None   
        # self.FinishTime = None
        # self.StatusTable = None
        self._given_start_time = None
        self._given_end_time = None 
        self._given_plan_cpu = None 
        self._given_plan_mem = None
        self._given_instance_num = None  
    def __repr__(self):
        return self.name  
    @property
    def FinishTime(self):
        return self.StartTime + self.AET
    @property
    def subDeadline(self):
        return self.LFT
    @property
    def weight(self):
        return self.runtime

    def calculateRunTime(self,MIPS):
        return self.weight/MIPS

    # def assignTask(self,)

    def addjobsetname(self, jobsetname):
        self.jobsetname = jobsetname

    def addInput(self, file_):
        self.inputs.append(file_) #add(file_)#
    
    def addOutput(self, file_):
        self.outputs.append(file_) #add(file_)#


