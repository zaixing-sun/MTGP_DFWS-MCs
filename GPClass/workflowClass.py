
from copy import deepcopy 
# import json
from Class.commonFunctionClass import Objectives

# DeadlineFactor = 1 # 0.85 # 0.85
class workflowClass: 

    def __init__(self,DAG=None, releaseTime=0,deadline=0,terminal_workflow = None,
                 id=0, namespace=None, name=None, ): #  ALLTERMINAL_DICT   taskQueue = [],deepcopy(WORKFLOWTERMINAL_dict)
        self.DAG = DAG
        self.releaseTime = releaseTime  # 释放时间为到达时间，也为工作流的最早开始时间
        self.deadline = deadline
        self.deadlineFactor = None
        # self.taskQueue = []
        self.terminal_workflow = terminal_workflow  # deepcopy(WORKFLOWTERMINAL_dict) # deepcopy(ALLTERMINAL_DICT) # WORKFLOWTERMINAL
        # self._terminal = workflowTerminalClass()
        # # # self.taskQueue = taskQueue  # 当当前时间大于释放时间时才会有任务队列
        # # # self.numberTasksQueue = 0  # 在队列中的任务数 the number of tasks in the queue
        # # # self.TOTALEXECUTETIMEQUEUE = 0 # 在队列中任务的执行时间之和  total weight of the operations in the queue. 
        # # # self.numberRemainingTasks = 0  # 剩余任务的数量 the number of remaining tasks
        # # # self.TOTALEXECUTETIMEREMAININGTASKS = 0 #剩余任务的的执行时间之和  total 执行时间 of the remaining tasks. totalWeightRemainingTasks
        # # # self.slackTime = 0 # 松弛时间 deadline减去 当前伪关键路径（剩余任务执行时间之和）的大小
        # # # self.waitingTime = 0 # 等待时间

        self.id = 0              
        self.name = name
        self.namespace = namespace
        self.DAGLevel = None    #DAG分层处理        
        self._DAGLevel = None
        self.unscheduledTaskNumber = None
        # self.scheduledBoolean = False
        self.NUMBERTASKINCLOUD = None
        self._givenMinStartTime = None
        self._givenMaxFinishTime = None
        self.objectives = None
    def __repr__(self):
        return self.name
    
    # def toJson(self):
    #     return json.dumps(self, default=lambda o: o.__dict__,indent=4,sort_keys=True,ensure_ascii=False)   
    # # def toJson(self,f):
    # #     return json.dumps(self, f,default=lambda o: o.__dict__,indent=4,sort_keys=True,ensure_ascii=False)  
     
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


    # def add_TaskQueue(self,taskList):
    #     for each in taskList:
    #         self.taskQueue.append(each)
    #         self.terminal['TOTALEXECUTETIMEQUEUE'] += self.DAG[each].runtime
    #     self.terminal['NUMBERTASKSQUEUE'] = len( self.taskQueue)
    # def sub_TaskQueue(self,taskList):
    #     for each in taskList:
    #         self.taskQueue.remove(each)
    #         self.terminal['TOTALEXECUTETIMEQUEUE'] -= self.DAG[each].runtime
    #         self.terminal['TOTALEXECUTETIMEREMAININGTASKS'] -= self.DAG[each].runtime
    #         self.terminal['NUMBERREMAININGTASKS'] -= 1
    #     self.terminal['NUMBERTASKSQUEUE'] = len( self.taskQueue)


# class dynamicWorkflowClass: 

#     def __init__(self,multipleWorkflowsSet = [],systemTime=0,workflowQueue = [],workflowPriority=[], ):
#         self.multipleWorkflowsSet = multipleWorkflowsSet
#         self.workflowQueue = workflowQueue # 
#         self.systemTime = systemTime
#         self.workflowPriority = workflowPriority#

#     # # @property
#     # # def workflowPriority(self,):
#     # #     return [None]*len(self.workflowQueue)
#     # # @property
#     # # def workflowPriority(self,value):
#     # #     return 
#     # @property
#     def sortQueue(self,):
#         for i in range(len(self.workflowPriority)-1):
#             for j in range(i+1,len(self.workflowPriority)):
#                 if self.workflowPriority[i]>self.workflowPriority[j]:
#                     self.workflowPriority[i],self.workflowPriority[j] = self.workflowPriority[j],self.workflowPriority[i]
#                     self.workflowQueue[i],self.workflowQueue[j] = self.workflowQueue[j],self.workflowQueue[i]
    
#     # def updateWotkflowTerminal(self,):

    
#     def updateWorkflowQueue(self,):
#         while True: 
#             for wfID in range(len(self.multipleWorkflowsSet)):
#                 if ((wfID not in self.workflowQueue) and (self.multipleWorkflowsSet[wfID].releaseTime>=self.systemTime)
#                     and(not self.multipleWorkflowsSet[wfID].scheduledBoolean)):
#                     self.workflowQueue += [wfID]
#                     ## 为新增到队列中的工作流  添加任务队列：首层拓扑层的任务
#                     self.multipleWorkflowsSet[wfID].add_TaskQueue(self.multipleWorkflowsSet[wfID].DAGLevel[0]) 
#             if self.workflowQueue==[]:
#                 self.systemTime += 10  #  等价于系统休眠10秒钟
#             else:
#                 break
        
    
    
#     # @property   
#     # def workflowQueue(self,):
#     #     return self._workflowQueue
    
#     # @workflowQueue.setter   
#     # def workflowQueue(self,):
#     #     for wfID in range(len(self.multipleWorkflowsSet)):
#     #         if ((wfID not in self._workflowQueue) and (self.multipleWorkflowsSet[wfID].releaseTime<=self.systemTime)
#     #             (not self.multipleWorkflowsSet[wfID].scheduledBoolean)):
#     #             self._workflowQueue += [wfID]
#     #     # return True if self.DAGLevel==[] else False

#     # @property   
#     # def systemDeadline(self):
#     #     ''' add_releaseTime_deadline '''
#     #     return self.releaseTime + self.deadline

#     # def given_DAGLevel(self,DAGLevel):
#     #     self._DAGLevel = deepcopy(DAGLevel)         
#     #     self.terminal['NUMBERREMAININGTASKS'] = len(self.DAG)
#     #     for name,task in self.DAG.items():
#     #         self.terminal['TOTALEXECUTETIMEREMAININGTASKS'] += task.runtime


#     # def add_TaskQueue(self,taskList):
#     #     for each in taskList:
#     #         self.taskQueue.append(each)
#     #         self.terminal['TOTALEXECUTETIMEQUEUE'] += self.DAG[each].runtime
#     #     self.terminal['NUMBERTASKSQUEUE'] = len( self.taskQueue)
#     # def sub_TaskQueue(self,taskList):
#     #     for each in taskList:
#     #         self.taskQueue.remove(each)
#     #         self.terminal['TOTALEXECUTETIMEQUEUE'] -= self.DAG[each].runtime
#     #         self.terminal['TOTALEXECUTETIMEREMAININGTASKS'] -= self.DAG[each].runtime
#     #         self.terminal['NUMBERREMAININGTASKS'] -= 1

#     #     self.terminal['NUMBERTASKSQUEUE'] = len( self.taskQueue)



#     # @property
#     # def __terminal(self):
#     #     self.terminal['NUMBERTASKSQUEUE'] = len( self.taskQueue)




#     # @property
#     # def __NUMBERTASKSQUEUE(self):
#     #     self.terminal['NUMBERTASKSQUEUE'] = len( self.taskQueue)

#     # @property
#     # def __TOTALEXECUTETIMEQUEUE(self):
#     #     self.terminal['TOTALEXECUTETIMEQUEUE'] = 0
#     #     for each in self.taskQueue:
#     #         self.terminal['TOTALEXECUTETIMEQUEUE'] += self.DAG[each].runtime
        

