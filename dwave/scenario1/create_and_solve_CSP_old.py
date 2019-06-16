'''
Created on 13.05.2019

@author: ahaemm
'''
import numpy as np
import dwavebinarycsp as csp
import penaltymodel.core as pm
import networkx as nx
import dimod
from penaltymodel.cache.interface import cache_penalty_model, get_penalty_model
import os
#import operator
#from code import args

# create and return an array of operation begin time variables
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

#### scenario1: 2 jobs a 2 ops, 2 machines, JSP

## create constraints "sum begin times over job ops = 1"
beginTimes_op1 = createBeginTimeVariables(1, 10) # job1
beginTimes_op2 = createBeginTimeVariables(2, 10) # job1
beginTimes_op3 = createBeginTimeVariables(3, 10) # job2
beginTimes_op4 = createBeginTimeVariables(4, 10) # job2


myCsp = csp.ConstraintSatisfactionProblem('BINARY')

constr_1 = csp.Constraint.from_func(c_sumBeginTimes_equals_1, beginTimes_op1, 'BINARY', 'sumBeginTimes_eq_1_op1')
myCsp.add_constraint(constr_1)
constr_2 = csp.Constraint.from_func(c_sumBeginTimes_equals_1, beginTimes_op2, 'BINARY', 'sumBeginTimes_eq_1_op2')
myCsp.add_constraint(constr_2)
constr_3 = csp.Constraint.from_func(c_sumBeginTimes_equals_1, beginTimes_op3, 'BINARY', 'sumBeginTimes_eq_1_op3')
myCsp.add_constraint(constr_3)
constr_4 = csp.Constraint.from_func(c_sumBeginTimes_equals_1, beginTimes_op4, 'BINARY', 'sumBeginTimes_eq_1_op4')
myCsp.add_constraint(constr_4)


bb = myCsp.check({'x_1_1':1, 'x_1_2':0, 'x_1_3':0, 'x_1_4':0, 'x_1_5':0, 'x_1_6':0, 'x_1_7':0, 'x_1_8':0, 'x_1_9':0, 'x_1_10':0, 'x_2_1':1, 'x_2_2':0, 'x_2_3':0, 'x_2_4':0, 'x_2_5':0, 'x_2_6':0, 'x_2_7':0, 'x_2_8':0, 'x_2_9':0, 'x_2_10':0, 
                  'x_3_1':1, 'x_3_2':0, 'x_3_3':0, 'x_3_4':0, 'x_3_5':0, 'x_3_6':0, 'x_3_7':0, 'x_3_8':0, 'x_3_9':0, 'x_3_10':0, 'x_4_1':1, 'x_4_2':0, 'x_4_3':0, 'x_4_4':0, 'x_4_5':0, 'x_4_6':0, 'x_4_7':0, 'x_4_8':0, 'x_4_9':0, 'x_4_10':0})

print('myCsp check: ', bb)

feas_configs_sumBeginTimes = {(1, 0, 0, 0, 0, 0, 0, 0, 0, 0), (0, 1, 0, 0, 0, 0, 0, 0, 0, 0), (0, 0, 1, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 1, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 1, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 1, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 1, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0, 1, 0, 0), (0, 0, 0, 0, 0, 0, 0, 0, 1, 0), (0, 0, 0, 0, 0, 0, 0, 0, 0, 1)}

graph_sumBeginTimes_op1 = nx.Graph()
graph_sumBeginTimes_op1.add_edges_from([('x_1_1', 'x_1_2'), ('x_1_1', 'x_1_3'), ('x_1_1', 'x_1_4'), ('x_1_1', 'x_1_5'), ('x_1_1', 'x_1_6'), ('x_1_1', 'x_1_7'), ('x_1_1', 'x_1_8'), ('x_1_1', 'x_1_9'), ('x_1_1', 'x_1_10'),
                       ('x_1_2', 'x_1_3'), ('x_1_2', 'x_1_4'), ('x_1_2', 'x_1_5'), ('x_1_2', 'x_1_6'), ('x_1_2', 'x_1_7'), ('x_1_2', 'x_1_8'), ('x_1_2', 'x_1_9'), ('x_1_2', 'x_1_10'), 
                       ('x_1_3', 'x_1_4'), ('x_1_3', 'x_1_5'), ('x_1_3', 'x_1_6'), ('x_1_3', 'x_1_7'), ('x_1_3', 'x_1_8'), ('x_1_3', 'x_1_9'), ('x_1_3', 'x_1_10'),
                       ('x_1_4', 'x_1_5'), ('x_1_4', 'x_1_6'), ('x_1_4', 'x_1_7'), ('x_1_4', 'x_1_8'), ('x_1_4', 'x_1_9'), ('x_1_4', 'x_1_10'),
                       ('x_1_5', 'x_1_6'), ('x_1_5', 'x_1_7'), ('x_1_5', 'x_1_8'), ('x_1_5', 'x_1_9'), ('x_1_5', 'x_1_10'),
                       ('x_1_6', 'x_1_7'), ('x_1_6', 'x_1_8'), ('x_1_6', 'x_1_9'), ('x_1_6', 'x_1_10'), 
                       ('x_1_7', 'x_1_8'), ('x_1_7', 'x_1_9'), ('x_1_7', 'x_1_10'), 
                       ('x_1_8', 'x_1_9'), ('x_1_8', 'x_1_10'), 
                       ('x_1_9', 'x_1_10')])
spec_sumBeginTimes_op1 = pm.Specification(graph_sumBeginTimes_op1, beginTimes_op1, feas_configs_sumBeginTimes, dimod.BINARY)
#penaltyModel_sumBeginTimes_op1 = pm.get_penalty_model(spec_sumBeginTimes_op1)
qubo_sumBeginTimes_op1 = dimod.BinaryQuadraticModel({'x_1_1':-1., 'x_1_2':-1., 'x_1_3':-1., 'x_1_4':-1., 'x_1_5':-1., 'x_1_6':-1., 'x_1_7':-1., 'x_1_8':-1., 'x_1_9':-1., 'x_1_10':-1.,},
                               {('x_1_1', 'x_1_2'):2., ('x_1_1', 'x_1_3'):2., ('x_1_1', 'x_1_4'):2., ('x_1_1', 'x_1_5'):2., ('x_1_1', 'x_1_6'):2., ('x_1_1', 'x_1_7'):2., ('x_1_1', 'x_1_8'):2., ('x_1_1', 'x_1_9'):2., ('x_1_1', 'x_1_10'):2.,
                       ('x_1_2', 'x_1_3'):2., ('x_1_2', 'x_1_4'):2., ('x_1_2', 'x_1_5'):2., ('x_1_2', 'x_1_6'):2., ('x_1_2', 'x_1_7'):2., ('x_1_2', 'x_1_8'):2., ('x_1_2', 'x_1_9'):2., ('x_1_2', 'x_1_10'):2., 
                       ('x_1_3', 'x_1_4'):2., ('x_1_3', 'x_1_5'):2., ('x_1_3', 'x_1_6'):2., ('x_1_3', 'x_1_7'):2., ('x_1_3', 'x_1_8'):2., ('x_1_3', 'x_1_9'):2., ('x_1_3', 'x_1_10'):2.,
                       ('x_1_4', 'x_1_5'):2., ('x_1_4', 'x_1_6'):2., ('x_1_4', 'x_1_7'):2., ('x_1_4', 'x_1_8'):2., ('x_1_4', 'x_1_9'):2., ('x_1_4', 'x_1_10'):2.,
                       ('x_1_5', 'x_1_6'):2., ('x_1_5', 'x_1_7'):2., ('x_1_5', 'x_1_8'):2., ('x_1_5', 'x_1_9'):2., ('x_1_5', 'x_1_10'):2.,
                       ('x_1_6', 'x_1_7'):2., ('x_1_6', 'x_1_8'):2., ('x_1_6', 'x_1_9'):2., ('x_1_6', 'x_1_10'):2., 
                       ('x_1_7', 'x_1_8'):2., ('x_1_7', 'x_1_9'):2., ('x_1_7', 'x_1_10'):2., 
                       ('x_1_8', 'x_1_9'):2., ('x_1_8', 'x_1_10'):2., 
                       ('x_1_9', 'x_1_10'):2.}, 1.0,
                               dimod.BINARY)

graph_sumBeginTimes_op2 = nx.Graph()
graph_sumBeginTimes_op2.add_edges_from([('x_2_1', 'x_2_2'), ('x_2_1', 'x_2_3'), ('x_2_1', 'x_2_4'), ('x_2_1', 'x_2_5'), ('x_2_1', 'x_2_6'), ('x_2_1', 'x_2_7'), ('x_2_1', 'x_2_8'), ('x_2_1', 'x_2_9'), ('x_2_1', 'x_2_10'),
                       ('x_2_2', 'x_2_3'), ('x_2_2', 'x_2_4'), ('x_2_2', 'x_2_5'), ('x_2_2', 'x_2_6'), ('x_2_2', 'x_2_7'), ('x_2_2', 'x_2_8'), ('x_2_2', 'x_2_9'), ('x_2_2', 'x_2_10'), 
                       ('x_2_3', 'x_2_4'), ('x_2_3', 'x_2_5'), ('x_2_3', 'x_2_6'), ('x_2_3', 'x_2_7'), ('x_2_3', 'x_2_8'), ('x_2_3', 'x_2_9'), ('x_2_3', 'x_2_10'),
                       ('x_2_4', 'x_2_5'), ('x_2_4', 'x_2_6'), ('x_2_4', 'x_2_7'), ('x_2_4', 'x_2_8'), ('x_2_4', 'x_2_9'), ('x_2_4', 'x_2_10'),
                       ('x_2_5', 'x_2_6'), ('x_2_5', 'x_2_7'), ('x_2_5', 'x_2_8'), ('x_2_5', 'x_2_9'), ('x_2_5', 'x_2_10'),
                       ('x_2_6', 'x_2_7'), ('x_2_6', 'x_2_8'), ('x_2_6', 'x_2_9'), ('x_2_6', 'x_2_10'), 
                       ('x_2_7', 'x_2_8'), ('x_2_7', 'x_2_9'), ('x_2_7', 'x_2_10'), 
                       ('x_2_8', 'x_2_9'), ('x_2_8', 'x_2_10'), 
                       ('x_2_9', 'x_2_10')])
spec_sumBeginTimes_op2 = pm.Specification(graph_sumBeginTimes_op2, beginTimes_op2, feas_configs_sumBeginTimes, dimod.BINARY)
qubo_sumBeginTimes_op2 = dimod.BinaryQuadraticModel({'x_2_1':-1., 'x_2_2':-1., 'x_2_3':-1., 'x_2_4':-1., 'x_2_5':-1., 'x_2_6':-1., 'x_2_7':-1., 'x_2_8':-1., 'x_2_9':-1., 'x_2_10':-1.,},
                               {('x_2_1', 'x_2_2'):2., ('x_2_1', 'x_2_3'):2., ('x_2_1', 'x_2_4'):2., ('x_2_1', 'x_2_5'):2., ('x_2_1', 'x_2_6'):2., ('x_2_1', 'x_2_7'):2., ('x_2_1', 'x_2_8'):2., ('x_2_1', 'x_2_9'):2., ('x_2_1', 'x_2_10'):2.,
                       ('x_2_2', 'x_2_3'):2., ('x_2_2', 'x_2_4'):2., ('x_2_2', 'x_2_5'):2., ('x_2_2', 'x_2_6'):2., ('x_2_2', 'x_2_7'):2., ('x_2_2', 'x_2_8'):2., ('x_2_2', 'x_2_9'):2., ('x_2_2', 'x_2_10'):2., 
                       ('x_2_3', 'x_2_4'):2., ('x_2_3', 'x_2_5'):2., ('x_2_3', 'x_2_6'):2., ('x_2_3', 'x_2_7'):2., ('x_2_3', 'x_2_8'):2., ('x_2_3', 'x_2_9'):2., ('x_2_3', 'x_2_10'):2.,
                       ('x_2_4', 'x_2_5'):2., ('x_2_4', 'x_2_6'):2., ('x_2_4', 'x_2_7'):2., ('x_2_4', 'x_2_8'):2., ('x_2_4', 'x_2_9'):2., ('x_2_4', 'x_2_10'):2.,
                       ('x_2_5', 'x_2_6'):2., ('x_2_5', 'x_2_7'):2., ('x_2_5', 'x_2_8'):2., ('x_2_5', 'x_2_9'):2., ('x_2_5', 'x_2_10'):2.,
                       ('x_2_6', 'x_2_7'):2., ('x_2_6', 'x_2_8'):2., ('x_2_6', 'x_2_9'):2., ('x_2_6', 'x_2_10'):2., 
                       ('x_2_7', 'x_2_8'):2., ('x_2_7', 'x_2_9'):2., ('x_2_7', 'x_2_10'):2., 
                       ('x_2_8', 'x_2_9'):2., ('x_2_8', 'x_2_10'):2., 
                       ('x_2_9', 'x_2_10'):2.}, 1.0,
                               dimod.BINARY)

graph_sumBeginTimes_op3 = nx.Graph()
graph_sumBeginTimes_op3.add_edges_from([('x_3_1', 'x_3_2'), ('x_3_1', 'x_3_3'), ('x_3_1', 'x_3_4'), ('x_3_1', 'x_3_5'), ('x_3_1', 'x_3_6'), ('x_3_1', 'x_3_7'), ('x_3_1', 'x_3_8'), ('x_3_1', 'x_3_9'), ('x_3_1', 'x_3_10'),
                       ('x_3_2', 'x_3_3'), ('x_3_2', 'x_3_4'), ('x_3_2', 'x_3_5'), ('x_3_2', 'x_3_6'), ('x_3_2', 'x_3_7'), ('x_3_2', 'x_3_8'), ('x_3_2', 'x_3_9'), ('x_3_2', 'x_3_10'), 
                       ('x_3_3', 'x_3_4'), ('x_3_3', 'x_3_5'), ('x_3_3', 'x_3_6'), ('x_3_3', 'x_3_7'), ('x_3_3', 'x_3_8'), ('x_3_3', 'x_3_9'), ('x_3_3', 'x_3_10'),
                       ('x_3_4', 'x_3_5'), ('x_3_4', 'x_3_6'), ('x_3_4', 'x_3_7'), ('x_3_4', 'x_3_8'), ('x_3_4', 'x_3_9'), ('x_3_4', 'x_3_10'),
                       ('x_3_5', 'x_3_6'), ('x_3_5', 'x_3_7'), ('x_3_5', 'x_3_8'), ('x_3_5', 'x_3_9'), ('x_3_5', 'x_3_10'),
                       ('x_3_6', 'x_3_7'), ('x_3_6', 'x_3_8'), ('x_3_6', 'x_3_9'), ('x_3_6', 'x_3_10'), 
                       ('x_3_7', 'x_3_8'), ('x_3_7', 'x_3_9'), ('x_3_7', 'x_3_10'), 
                       ('x_3_8', 'x_3_9'), ('x_3_8', 'x_3_10'), 
                       ('x_3_9', 'x_3_10')])
spec_sumBeginTimes_op3 = pm.Specification(graph_sumBeginTimes_op3, beginTimes_op3, feas_configs_sumBeginTimes, dimod.BINARY)
qubo_sumBeginTimes_op3 = dimod.BinaryQuadraticModel({'x_3_1':-1., 'x_3_2':-1., 'x_3_3':-1., 'x_3_4':-1., 'x_3_5':-1., 'x_3_6':-1., 'x_3_7':-1., 'x_3_8':-1., 'x_3_9':-1., 'x_3_10':-1.,},
                               {('x_3_1', 'x_3_2'):2., ('x_3_1', 'x_3_3'):2., ('x_3_1', 'x_3_4'):2., ('x_3_1', 'x_3_5'):2., ('x_3_1', 'x_3_6'):2., ('x_3_1', 'x_3_7'):2., ('x_3_1', 'x_3_8'):2., ('x_3_1', 'x_3_9'):2., ('x_3_1', 'x_3_10'):2.,
                       ('x_3_2', 'x_3_3'):2., ('x_3_2', 'x_3_4'):2., ('x_3_2', 'x_3_5'):2., ('x_3_2', 'x_3_6'):2., ('x_3_2', 'x_3_7'):2., ('x_3_2', 'x_3_8'):2., ('x_3_2', 'x_3_9'):2., ('x_3_2', 'x_3_10'):2., 
                       ('x_3_3', 'x_3_4'):2., ('x_3_3', 'x_3_5'):2., ('x_3_3', 'x_3_6'):2., ('x_3_3', 'x_3_7'):2., ('x_3_3', 'x_3_8'):2., ('x_3_3', 'x_3_9'):2., ('x_3_3', 'x_3_10'):2.,
                       ('x_3_4', 'x_3_5'):2., ('x_3_4', 'x_3_6'):2., ('x_3_4', 'x_3_7'):2., ('x_3_4', 'x_3_8'):2., ('x_3_4', 'x_3_9'):2., ('x_3_4', 'x_3_10'):2.,
                       ('x_3_5', 'x_3_6'):2., ('x_3_5', 'x_3_7'):2., ('x_3_5', 'x_3_8'):2., ('x_3_5', 'x_3_9'):2., ('x_3_5', 'x_3_10'):2.,
                       ('x_3_6', 'x_3_7'):2., ('x_3_6', 'x_3_8'):2., ('x_3_6', 'x_3_9'):2., ('x_3_6', 'x_3_10'):2., 
                       ('x_3_7', 'x_3_8'):2., ('x_3_7', 'x_3_9'):2., ('x_3_7', 'x_3_10'):2., 
                       ('x_3_8', 'x_3_9'):2., ('x_3_8', 'x_3_10'):2., 
                       ('x_3_9', 'x_3_10'):2.}, 1.0,
                               dimod.BINARY)

graph_sumBeginTimes_op4 = nx.Graph()
graph_sumBeginTimes_op4.add_edges_from([('x_4_1', 'x_4_2'), ('x_4_1', 'x_4_3'), ('x_4_1', 'x_4_4'), ('x_4_1', 'x_4_5'), ('x_4_1', 'x_4_6'), ('x_4_1', 'x_4_7'), ('x_4_1', 'x_4_8'), ('x_4_1', 'x_4_9'), ('x_4_1', 'x_4_10'),
                       ('x_4_2', 'x_4_3'), ('x_4_2', 'x_4_4'), ('x_4_2', 'x_4_5'), ('x_4_2', 'x_4_6'), ('x_4_2', 'x_4_7'), ('x_4_2', 'x_4_8'), ('x_4_2', 'x_4_9'), ('x_4_2', 'x_4_10'), 
                       ('x_4_3', 'x_4_4'), ('x_4_3', 'x_4_5'), ('x_4_3', 'x_4_6'), ('x_4_3', 'x_4_7'), ('x_4_3', 'x_4_8'), ('x_4_3', 'x_4_9'), ('x_4_3', 'x_4_10'),
                       ('x_4_4', 'x_4_5'), ('x_4_4', 'x_4_6'), ('x_4_4', 'x_4_7'), ('x_4_4', 'x_4_8'), ('x_4_4', 'x_4_9'), ('x_4_4', 'x_4_10'),
                       ('x_4_5', 'x_4_6'), ('x_4_5', 'x_4_7'), ('x_4_5', 'x_4_8'), ('x_4_5', 'x_4_9'), ('x_4_5', 'x_4_10'),
                       ('x_4_6', 'x_4_7'), ('x_4_6', 'x_4_8'), ('x_4_6', 'x_4_9'), ('x_4_6', 'x_4_10'), 
                       ('x_4_7', 'x_4_8'), ('x_4_7', 'x_4_9'), ('x_4_7', 'x_4_10'), 
                       ('x_4_8', 'x_4_9'), ('x_4_8', 'x_4_10'), 
                       ('x_4_9', 'x_4_10')])
spec_sumBeginTimes_op4 = pm.Specification(graph_sumBeginTimes_op4, beginTimes_op4, feas_configs_sumBeginTimes, dimod.BINARY)
#penaltyModel_sumBeginTimes_op1 = pm.get_penalty_model(spec_sumBeginTimes_op1)
qubo_sumBeginTimes_op4 = dimod.BinaryQuadraticModel({'x_4_1':-1., 'x_4_2':-1., 'x_4_3':-1., 'x_4_4':-1., 'x_4_5':-1., 'x_4_6':-1., 'x_4_7':-1., 'x_4_8':-1., 'x_4_9':-1., 'x_4_10':-1.,},
                               {('x_4_1', 'x_4_2'):2., ('x_4_1', 'x_4_3'):2., ('x_4_1', 'x_4_4'):2., ('x_4_1', 'x_4_5'):2., ('x_4_1', 'x_4_6'):2., ('x_4_1', 'x_4_7'):2., ('x_4_1', 'x_4_8'):2., ('x_4_1', 'x_4_9'):2., ('x_4_1', 'x_4_10'):2.,
                       ('x_4_2', 'x_4_3'):2., ('x_4_2', 'x_4_4'):2., ('x_4_2', 'x_4_5'):2., ('x_4_2', 'x_4_6'):2., ('x_4_2', 'x_4_7'):2., ('x_4_2', 'x_4_8'):2., ('x_4_2', 'x_4_9'):2., ('x_4_2', 'x_4_10'):2., 
                       ('x_4_3', 'x_4_4'):2., ('x_4_3', 'x_4_5'):2., ('x_4_3', 'x_4_6'):2., ('x_4_3', 'x_4_7'):2., ('x_4_3', 'x_4_8'):2., ('x_4_3', 'x_4_9'):2., ('x_4_3', 'x_4_10'):2.,
                       ('x_4_4', 'x_4_5'):2., ('x_4_4', 'x_4_6'):2., ('x_4_4', 'x_4_7'):2., ('x_4_4', 'x_4_8'):2., ('x_4_4', 'x_4_9'):2., ('x_4_4', 'x_4_10'):2.,
                       ('x_4_5', 'x_4_6'):2., ('x_4_5', 'x_4_7'):2., ('x_4_5', 'x_4_8'):2., ('x_4_5', 'x_4_9'):2., ('x_4_5', 'x_4_10'):2.,
                       ('x_4_6', 'x_4_7'):2., ('x_4_6', 'x_4_8'):2., ('x_4_6', 'x_4_9'):2., ('x_4_6', 'x_4_10'):2., 
                       ('x_4_7', 'x_4_8'):2., ('x_4_7', 'x_4_9'):2., ('x_4_7', 'x_4_10'):2., 
                       ('x_4_8', 'x_4_9'):2., ('x_4_8', 'x_4_10'):2., 
                       ('x_4_9', 'x_4_10'):2.}, 1.0,
                               dimod.BINARY)

#pModel_sumBeginTimes_op1 = pm.PenaltyModel.from_specification(spec_sumBeginTimes_op1, qubo_sumBeginTimes_op1, 2, 0)
#pModel = pm.get_penalty_model(spec_sumBeginTimes_op1)
#cache_penalty_model(pModel_sumBeginTimes_op1, 'c:\\Users\\ahaemm\\workspace\\dwave\\env\\data\\dwave-penaltymodel-cache\\penaltymodel_cache_v0.4.0.db')

#pModel_sumBeginTimes_op2 = pm.PenaltyModel.from_specification(spec_sumBeginTimes_op2, qubo_sumBeginTimes_op2, 2, 0)
#pModel = pm.get_penalty_model(spec_sumBeginTimes_op1)
#cache_penalty_model(pModel_sumBeginTimes_op2, 'c:\\Users\\ahaemm\\workspace\\dwave\\env\\data\\dwave-penaltymodel-cache\\penaltymodel_cache_v0.4.0.db')

#pModel_sumBeginTimes_op3 = pm.PenaltyModel.from_specification(spec_sumBeginTimes_op3, qubo_sumBeginTimes_op3, 2, 0)
#pModel = pm.get_penalty_model(spec_sumBeginTimes_op1)
#cache_penalty_model(pModel_sumBeginTimes_op3, 'c:\\Users\\ahaemm\\workspace\\dwave\\env\\data\\dwave-penaltymodel-cache\\penaltymodel_cache_v0.4.0.db')

#pModel_sumBeginTimes_op4 = pm.PenaltyModel.from_specification(spec_sumBeginTimes_op4, qubo_sumBeginTimes_op4, 2, 0)
#pModel = pm.get_penalty_model(spec_sumBeginTimes_op1)
#cache_penalty_model(pModel_sumBeginTimes_op4, 'c:\\Users\\ahaemm\\workspace\\dwave\\env\\data\\dwave-penaltymodel-cache\\penaltymodel_cache_v0.4.0.db')

pm_tmp = get_penalty_model(spec_sumBeginTimes_op4, 'c:\\Users\\ahaemm\\workspace\\dwave\\env\\data\\dwave-penaltymodel-cache\\penaltymodel_cache_v0.4.0.db')

bqm = csp.stitch(myCsp, 2, 10)
print(bqm)


#############################
#filename = '.\\TestData\\' + 'MyBlackFriday.csv'
#working_dir = 'c:\\Users\\rsteri\\Documents\\Python\\'     
#os.chdir(working_dir)
#print('Trying to read file \"{0:s}\" from  \"{1:s}\" ... '.format(filename,os.getcwd()))

#if not os.path.isfile( filename):
#    print('File does not exist. Current working directory \"{0:s}\"; -->  Exit program'.format(os.getcwd()))
#    exit()


#df = pd.read_csv(filename,sep=";")

