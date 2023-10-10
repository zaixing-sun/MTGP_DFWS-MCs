
from copy import deepcopy 
from Class.commonFunctionClass import Objectives

class workflowClass: 

    def __init__(self,DAG=None, releaseTime=0,deadline=0,terminal_workflow = None,
                 id=0, namespace=None, name=None, ): 
        self.DAG = DAG
        self.releaseTime = releaseTime  
        self.deadline = deadline
        self.deadlineFactor = None
        self.terminal_workflow = terminal_workflow  

        self.id = 0              
        self.name = name
        self.namespace = namespace
        self.DAGLevel = None        
        self._DAGLevel = None
        self.unscheduledTaskNumber = None
        self.NUMBERTASKINCLOUD = None
        self._givenMinStartTime = None
        self._givenMaxFinishTime = None
        self.objectives = None
    def __repr__(self):
        return self.name
    

    @property   
    def scheduledBoolean(self):
        return True if self.unscheduledTaskNumber==0 else False

    @property   
    def systemDeadline(self):
        ''' add_releaseTime_deadline '''
        return self.releaseTime + self.deadline

    def given_DAGLevel(self,DAGLevel):
        self._DAGLevel = deepcopy(DAGLevel)         
        self.terminal_workflow.NUMBERREMAININGTASKS = len(self.DAG)
        for name,task in self.DAG.items():
            self.terminal_workflow.TOTALEXECUTETIMEREMAININGTASKS += task.runtime
