'''
Created on 26.05.2019

@author: ahaemm
'''
import numpy as np
import dwavebinarycsp as csp

# create and return an array of binary operation begin time variables; 
# example: 'x_1_4' = 1, if operation 1 starts at the beginning of time slot 4
# operations are lexicographically ordered {1,2,3,4}

def createBeginTimeVariables(job,nrTimeSlots):
    aList = []
    for i in range(nrTimeSlots):
        a = 'x_' + str(job) + '_' + str(i+1)
        aList.append(a)
    
    variables = np.array(aList)
    return variables

# constraint: sum of variable values in arg anArray must equal 1
def c_sumBeginTimes_equals_1(*args):
    anArray = np.array(args)
    ssum = 0
    for i in range(anArray.size):
        #print(i, anArray[i])
        ssum = ssum + anArray[i]
    #print("sum: ", ssum)
    if ssum == 1: 
        return True
    else: 
        return False

# creates the precedence constraint between op1, op2 for time1, the start time for op1 
# parameter "aCSP" is the constraint satisfaction problem
def create_precedenceConstraint(op1, time1, op1_processTime, op2, aCSP):
    var1 = 'x_' + str(op1) + '_' + str(time1)
    op1_completionTime = time1 + op1_processTime - 1
    for t in range(op1_completionTime):
        var2 = 'x_' + str(op2) + '_' + str(t+1)
        constraint = csp.Constraint.from_configurations([(1, 0), (0, 0), (0, 1)], 
                                                        [var1, var2], csp.BINARY)
        aCSP.add_constraint(constraint) 
        
# creates the machine capacity constraint between op1, op2 for time1, the start time for op1 
# parameter "aCSP" is the constraint satisfaction problem
def create_machineCapacityConstraint(op1, time1, op1_processTime, op2, aCSP):
    var1 = 'x_' + str(op1) + '_' + str(time1)
    op1_completionTime = time1 + op1_processTime - 1
    for t in range(op1_completionTime):
        if t > time1-2:
            var2 = 'x_' + str(op2) + '_' + str(t+1)
            constraint = csp.Constraint.from_configurations([(1, 0), (0, 0), (0, 1)], 
                                                        [var1, var2], csp.BINARY)
            aCSP.add_constraint(constraint)       