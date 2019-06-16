'''
Created on 24.05.2019

@author: ahaemm
'''

#import numpy as np
import dwavebinarycsp as csp
from dimod.reference.samplers import SimulatedAnnealingSampler
from dwave.system.samplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite, FixedEmbeddingComposite
from dwave.cloud import Client
from functions import create_machineCapacityConstraint
from functions import create_precedenceConstraint
#from functions import createBeginTimeVariables
from functions import c_sumBeginTimes_equals_1
from minorminer import find_embedding


useDwave = True
optimize = False

  
   
#beginTimes_op1 = createBeginTimeVariables(1, 10) # job1
#beginTimes_op2 = createBeginTimeVariables(2, 10) # job1
#beginTimes_op3 = createBeginTimeVariables(3, 10) # job2
#beginTimes_op4 = createBeginTimeVariables(4, 10) # job2

beginTimes_op1 = ['x_1_1', 'x_1_2', 'x_1_3', 'x_1_4', 'x_1_5', 'x_1_6', 'x_1_7', 'x_1_8', 'x_1_9', 'x_1_10']
beginTimes_op2 = ['x_2_1', 'x_2_2', 'x_2_3', 'x_2_4', 'x_2_5', 'x_2_6', 'x_2_7', 'x_2_8', 'x_2_9', 'x_2_10']
beginTimes_op3 = ['x_3_1', 'x_3_2', 'x_3_3', 'x_3_4', 'x_3_5', 'x_3_6', 'x_3_7', 'x_3_8', 'x_3_9', 'x_3_10']
beginTimes_op4 = ['x_4_1', 'x_4_2', 'x_4_3', 'x_4_4', 'x_4_5', 'x_4_6', 'x_4_7', 'x_4_8', 'x_4_9', 'x_4_10']

myCsp = csp.ConstraintSatisfactionProblem('BINARY')

# constraints "sum begin times is 1"
constr_1 = csp.Constraint.from_func(c_sumBeginTimes_equals_1, beginTimes_op1, 'BINARY', 'sumBeginTimes_eq_1_op1')
myCsp.add_constraint(constr_1)
constr_2 = csp.Constraint.from_func(c_sumBeginTimes_equals_1, beginTimes_op2, 'BINARY', 'sumBeginTimes_eq_1_op2')
myCsp.add_constraint(constr_2)
constr_3 = csp.Constraint.from_func(c_sumBeginTimes_equals_1, beginTimes_op3, 'BINARY', 'sumBeginTimes_eq_1_op3')
myCsp.add_constraint(constr_3)
constr_4 = csp.Constraint.from_func(c_sumBeginTimes_equals_1, beginTimes_op4, 'BINARY', 'sumBeginTimes_eq_1_op4')
myCsp.add_constraint(constr_4)


# precedence constraints job 1, process times: op(1,1) = op1: 2, op(1,2) = op2: 3 
create_precedenceConstraint(1, 1, 2, 2, myCsp)
create_precedenceConstraint(1, 2, 2, 2, myCsp) 
create_precedenceConstraint(1, 3, 2, 2, myCsp)
create_precedenceConstraint(1, 4, 2, 2, myCsp)
create_precedenceConstraint(1, 5, 2, 2, myCsp)
create_precedenceConstraint(1, 6, 2, 2, myCsp)
# op1 cannot start later than t = 6 

# precedence constraints job 2, process times: op(2,1) = op3: 2, op(2,2) = op4: 3 
create_precedenceConstraint(3, 1, 2, 4, myCsp)
create_precedenceConstraint(3, 2, 2, 4, myCsp) 
create_precedenceConstraint(3, 3, 2, 4, myCsp)
create_precedenceConstraint(3, 4, 2, 4, myCsp)
create_precedenceConstraint(3, 5, 2, 4, myCsp)
create_precedenceConstraint(3, 6, 2, 4, myCsp)
# op3 cannot start later than t = 6 


# capacity constraints for machine 1, assigned to op1, op3, both with process time = 2
create_machineCapacityConstraint(1, 1, 2, 3, myCsp)
create_machineCapacityConstraint(1, 2, 2, 3, myCsp)
create_machineCapacityConstraint(1, 3, 2, 3, myCsp)
create_machineCapacityConstraint(1, 4, 2, 3, myCsp)
create_machineCapacityConstraint(1, 5, 2, 3, myCsp)
create_machineCapacityConstraint(1, 6, 2, 3, myCsp)
create_machineCapacityConstraint(1, 7, 2, 3, myCsp)
create_machineCapacityConstraint(1, 8, 2, 3, myCsp)
create_machineCapacityConstraint(1, 9, 2, 3, myCsp)

create_machineCapacityConstraint(3, 1, 2, 1, myCsp)
create_machineCapacityConstraint(3, 2, 2, 1, myCsp)
create_machineCapacityConstraint(3, 3, 2, 1, myCsp)
create_machineCapacityConstraint(3, 4, 2, 1, myCsp)
create_machineCapacityConstraint(3, 5, 2, 1, myCsp)
create_machineCapacityConstraint(3, 6, 2, 1, myCsp)
create_machineCapacityConstraint(3, 7, 2, 1, myCsp)
create_machineCapacityConstraint(3, 8, 2, 1, myCsp)
create_machineCapacityConstraint(3, 9, 2, 1, myCsp)

# capacity constraints for machine 2, assigned to op2 (process time = 3), op4 (process time = 3)
create_machineCapacityConstraint(2, 1, 3, 4, myCsp)
create_machineCapacityConstraint(2, 2, 3, 4, myCsp)
create_machineCapacityConstraint(2, 3, 3, 4, myCsp)
create_machineCapacityConstraint(2, 4, 3, 4, myCsp)
create_machineCapacityConstraint(2, 5, 3, 4, myCsp)
create_machineCapacityConstraint(2, 6, 3, 4, myCsp)
create_machineCapacityConstraint(2, 7, 3, 4, myCsp)
create_machineCapacityConstraint(2, 8, 3, 4, myCsp)

create_machineCapacityConstraint(4, 1, 3, 2, myCsp)
create_machineCapacityConstraint(4, 2, 3, 2, myCsp)
create_machineCapacityConstraint(4, 3, 3, 2, myCsp)
create_machineCapacityConstraint(4, 4, 3, 2, myCsp)
create_machineCapacityConstraint(4, 5, 3, 2, myCsp)
create_machineCapacityConstraint(4, 6, 3, 2, myCsp)
create_machineCapacityConstraint(4, 7, 3, 2, myCsp)
create_machineCapacityConstraint(4, 8, 3, 2, myCsp)

bb = myCsp.check({'x_1_1':1, 'x_1_2':0, 'x_1_3':0, 'x_1_4':0, 'x_1_5':0, 'x_1_6':0, 'x_1_7':0, 'x_1_8':0, 'x_1_9':0, 'x_1_10':0, 
                  'x_2_1':0, 'x_2_2':0, 'x_2_3':1, 'x_2_4':0, 'x_2_5':0, 'x_2_6':0, 'x_2_7':0, 'x_2_8':0, 'x_2_9':0, 'x_2_10':0, 
                  'x_3_1':0, 'x_3_2':0, 'x_3_3':1, 'x_3_4':0, 'x_3_5':0, 'x_3_6':0, 'x_3_7':0, 'x_3_8':0, 'x_3_9':0, 'x_3_10':0, 
                  'x_4_1':0, 'x_4_2':0, 'x_4_3':0, 'x_4_4':0, 'x_4_5':0, 'x_4_6':1, 'x_4_7':0, 'x_4_8':0, 'x_4_9':0, 'x_4_10':0})

print('myCsp check: ', bb)

bqm = csp.stitch(myCsp, min_classical_gap=2., max_graph_size=10)
print('binary quadratic model built')

bqm.fix_variable('x_1_10', 0)
bqm.fix_variable('x_1_9', 0)
bqm.fix_variable('x_1_8', 0)
bqm.fix_variable('x_1_7', 0)
bqm.fix_variable('x_2_9', 0)
bqm.fix_variable('x_2_10', 0)

bqm.fix_variable('x_3_10', 0)
bqm.fix_variable('x_3_9', 0)
bqm.fix_variable('x_3_8', 0)
bqm.fix_variable('x_3_7', 0)
bqm.fix_variable('x_4_9', 0)
bqm.fix_variable('x_4_10', 0)

print("variables fixed")

if optimize:
    # add linear biases 
    # prefers op1 (i.e. job1) to start at time {1,2}
    bqm.add_variable('x_1_1', 0., vartype=None)
    bqm.add_variable('x_1_2', 0., vartype=None)
    bqm.add_variable('x_1_3', 0.1, vartype=None)
    bqm.add_variable('x_1_4', 0.2, vartype=None)
    bqm.add_variable('x_1_5', 0.3, vartype=None)
    bqm.add_variable('x_1_6', 0.4, vartype=None)
    
    # prefers op3 ( i.e. job 2) to start at time {4,5}
    bqm.add_variable('x_3_1', 0.3, vartype=None)
    bqm.add_variable('x_3_2', 0.2, vartype=None)
    bqm.add_variable('x_3_3', 0.1, vartype=None)
    bqm.add_variable('x_3_4', 0., vartype=None)
    bqm.add_variable('x_3_5', 0., vartype=None)
    bqm.add_variable('x_3_6', 0.1, vartype=None)
    
    # prefers op2 to start at time {3,4}, i.e. job 1 should finish at time {5,6}
    bqm.add_variable('x_2_1', 0.2, vartype=None)
    bqm.add_variable('x_2_2', 0.1, vartype=None)
    bqm.add_variable('x_2_3', 0., vartype=None)
    bqm.add_variable('x_2_4', 0., vartype=None)
    bqm.add_variable('x_2_5', 0.1, vartype=None)
    bqm.add_variable('x_2_6', 0.2, vartype=None)
    bqm.add_variable('x_2_7', 0.3, vartype=None)
    bqm.add_variable('x_2_8', 0.4, vartype=None)
    
    # prefers op4 to start at time {7,8}, i.e. job 1 should finish at time {9,10}
    bqm.add_variable('x_4_1', 0.6, vartype=None)
    bqm.add_variable('x_4_2', 0.5, vartype=None)
    bqm.add_variable('x_4_3', 0.4, vartype=None)
    bqm.add_variable('x_4_4', 0.3, vartype=None)
    bqm.add_variable('x_4_5', 0.2, vartype=None)
    bqm.add_variable('x_4_6', 0.1, vartype=None)
    bqm.add_variable('x_4_7', 0., vartype=None)
    bqm.add_variable('x_4_8', 0., vartype=None)
    
    print("optimization = true, linear biases added")
else:
    print("optimization = false, just solving CSP")

if useDwave:
    client = Client.from_config(token='DEV-ee477a6974fcc6a5c059c5275e3fbeb40a227db7')
    #print(client.get_solvers())
    #print("sampler properties: ")
    #print(DWaveSampler().properties)
    
    
    # create a minor embedding of the source graph representing "bqm" onto the dWave's Chimera graph
    embedding = find_embedding(bqm.to_networkx_graph(), DWaveSampler().edgelist)
    print("embedding created")
    print(embedding)
    sampler = FixedEmbeddingComposite(DWaveSampler(), embedding)
    print('+++ starting sampling on QPU')
    sampleSet = sampler.sample(bqm, num_reads=50) # returns SampleSet
    print(sampleSet.info)
    print('lowest energy sample')
    print(sampleSet.first)
    print('all samples')
    for datum in sampleSet.data(fields=['sample','energy', 'num_occurrences']):
        print(datum)
    
    
else:
    sampler = SimulatedAnnealingSampler()
    response = sampler.sample(bqm,num_reads=5,num_sweeps=1000) # returns SampleSet
    for datum in response.data(['sample', 'energy']):
        print(datum.sample, datum.energy)


