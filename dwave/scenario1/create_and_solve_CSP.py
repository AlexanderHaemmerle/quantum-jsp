''''
Created on 13.05.2019

@author: ahaemm
'''
import numpy as np
import dwavebinarycsp as csp
from dimod.reference.samplers import SimulatedAnnealingSampler
from functions import create_machineCapacityConstraint
from functions import create_precedenceConstraint
from functions import createBeginTimeVariables
from functions import c_sumBeginTimes_equals_1



'''
# precedence constraint between op_i, op_i+1, with length 2, i.e. 
# the process time of op_i = 2
def c_precedence(op1_1, op2_1, op2_2):
    ssum = int(op1_1)*int(op2_1) + int(op1_1)*int(op2_2)
    if ssum == 0:
        return True
    else:
        return False
'''
   
beginTimes_op1 = createBeginTimeVariables(1, 10) # job1
beginTimes_op2 = createBeginTimeVariables(2, 10) # job1
beginTimes_op3 = createBeginTimeVariables(3, 10) # job2
beginTimes_op4 = createBeginTimeVariables(4, 10) # job2


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
myCsp.add_constraint(csp.Constraint.from_configurations([(1, 0, 0), (0, 0, 0), (0, 1, 0), (0, 0, 1)], 
                                                        ['x_1_1', 'x_2_1', 'x_2_2'], csp.BINARY, name = 'c_prec'))

myCsp.add_constraint(csp.Constraint.from_configurations([(1, 0, 0, 0), (0, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1)], 
                                                        ['x_1_2', 'x_2_1', 'x_2_2', 'x_2_3'], csp.BINARY, name = 'c_prec'))

myCsp.add_constraint(csp.Constraint.from_configurations([(1, 0, 0, 0, 0), (0, 0, 0, 0, 0), (0, 1, 0, 0, 0), (0, 0, 1, 0, 0), (0, 0, 0, 1, 0), (0, 0, 0, 0, 1)], 
                                                        ['x_1_3', 'x_2_1', 'x_2_2', 'x_2_3', 'x_2_4'], csp.BINARY, name = 'c_prec'))

myCsp.add_constraint(csp.Constraint.from_configurations([(1, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0), (0, 1, 0, 0, 0, 0), (0, 0, 1, 0, 0, 0), (0, 0, 0, 1, 0, 0), (0, 0, 0, 0, 1, 0), (0, 0, 0, 0, 0, 1)], 
                                                        ['x_1_4', 'x_2_1', 'x_2_2', 'x_2_3', 'x_2_4', 'x_2_5'], csp.BINARY, name = 'c_prec'))

myCsp.add_constraint(csp.Constraint.from_configurations([(1, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 1, 0, 0, 0, 0, 0), (0, 0, 1, 0, 0, 0, 0), (0, 0, 0, 1, 0, 0, 0), (0, 0, 0, 0, 1, 0, 0), (0, 0, 0, 0, 0, 1, 0), 
                                                         (0, 0, 0, 0, 0, 0, 1)], ['x_1_5', 'x_2_1', 'x_2_2', 'x_2_3', 'x_2_4', 'x_2_5', 'x_2_6'], csp.BINARY, name = 'c_prec'))

myCsp.add_constraint(csp.Constraint.from_configurations([(1, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0, 0), (0, 1, 0, 0, 0, 0, 0, 0), (0, 0, 1, 0, 0, 0, 0, 0), 
                                                         (0, 0, 0, 1, 0, 0, 0, 0), (0, 0, 0, 0, 1, 0, 0, 0), (0, 0, 0, 0, 0, 1, 0, 0), (0, 0, 0, 0, 0, 0, 1, 0), (0, 0, 0, 0, 0, 0, 0, 1)], 
                                                         ['x_1_6', 'x_2_1', 'x_2_2', 'x_2_3', 'x_2_4', 'x_2_5', 'x_2_6', 'x_2_7'], csp.BINARY, name = 'c_prec'))

'''
the following 3 constraints are not necessary, as op2 cannot start later than t = 8 

myCsp.add_constraint(csp.Constraint.from_configurations([(1, 0, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0, 0, 0), (0, 1, 0, 0, 0, 0, 0, 0, 0), (0, 0, 1, 0, 0, 0, 0, 0, 0), 
                                                         (0, 0, 0, 1, 0, 0, 0, 0, 0), (0, 0, 0, 0, 1, 0, 0, 0, 0), (0, 0, 0, 0, 0, 1, 0, 0, 0), (0, 0, 0, 0, 0, 0, 1, 0, 0), 
                                                         (0, 0, 0, 0, 0, 0, 0, 1, 0), (0, 0, 0, 0, 0, 0, 0, 0, 1)],['x_1_7', 'x_2_1', 'x_2_2', 'x_2_3', 'x_2_4', 'x_2_5', 'x_2_6', 'x_2_7', 'x_2_8'], 
                                                         csp.BINARY, name = 'c_prec'))

myCsp.add_constraint(csp.Constraint.from_configurations([(1, 0, 0, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0, 0, 0, 0), (0, 1, 0, 0, 0, 0, 0, 0, 0, 0), 
                                                         (0, 0, 1, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 1, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 1, 0, 0, 0, 0, 0), 
                                                         (0, 0, 0, 0, 0, 1, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 1, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0, 1, 0, 0), 
                                                         (0, 0, 0, 0, 0, 0, 0, 0, 1, 0), (0, 0, 0, 0, 0, 0, 0, 0, 0, 1)],
                                                         ['x_1_8', 'x_2_1', 'x_2_2', 'x_2_3', 'x_2_4', 'x_2_5', 'x_2_6', 'x_2_7', 'x_2_8', 'x_2_9'], csp.BINARY, name = 'c_prec'))
myCsp.add_constraint(csp.Constraint.from_configurations([(1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), (0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0), 
                                                         (0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0), 
                                                         (0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0), 
                                                         (0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0), (0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0), (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1)], 
                                                         ['x_1_9', 'x_2_1', 'x_2_2', 'x_2_3', 'x_2_4', 'x_2_5', 'x_2_6', 'x_2_7', 'x_2_8', 'x_2_9', 'x_2_10'], csp.BINARY, name = 'c_prec'))
'''

# precedence constraints job 2, process times: op(2,1) = op3: 2, op(2,2) = op4: 3 
myCsp.add_constraint(csp.Constraint.from_configurations([(1, 0, 0), (0, 0, 0), (0, 1, 0), (0, 0, 1)], 
                                                        ['x_3_1', 'x_4_1', 'x_4_2'], csp.BINARY, name = 'c_prec'))
myCsp.add_constraint(csp.Constraint.from_configurations([(1, 0, 0, 0), (0, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1)], 
                                                        ['x_3_2', 'x_4_1', 'x_4_2', 'x_4_3'], csp.BINARY, name = 'c_prec'))
myCsp.add_constraint(csp.Constraint.from_configurations([(1, 0, 0, 0, 0), (0, 0, 0, 0, 0), (0, 1, 0, 0, 0), (0, 0, 1, 0, 0), (0, 0, 0, 1, 0), (0, 0, 0, 0, 1)], 
                                                        ['x_3_3', 'x_4_1', 'x_4_2', 'x_4_3', 'x_4_4'], csp.BINARY, name = 'c_prec'))
myCsp.add_constraint(csp.Constraint.from_configurations([(1, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0), (0, 1, 0, 0, 0, 0), (0, 0, 1, 0, 0, 0), (0, 0, 0, 1, 0, 0), (0, 0, 0, 0, 1, 0), (0, 0, 0, 0, 0, 1)], 
                                                        ['x_3_4', 'x_4_1', 'x_4_2', 'x_4_3', 'x_4_4', 'x_4_5'], csp.BINARY, name = 'c_prec'))
myCsp.add_constraint(csp.Constraint.from_configurations([(1, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 1, 0, 0, 0, 0, 0), (0, 0, 1, 0, 0, 0, 0), (0, 0, 0, 1, 0, 0, 0), (0, 0, 0, 0, 1, 0, 0), (0, 0, 0, 0, 0, 1, 0), 
                                                         (0, 0, 0, 0, 0, 0, 1)], ['x_3_5', 'x_4_1', 'x_4_2', 'x_4_3', 'x_4_4', 'x_4_5', 'x_4_6'], csp.BINARY, name = 'c_prec'))
myCsp.add_constraint(csp.Constraint.from_configurations([(1, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0, 0), (0, 1, 0, 0, 0, 0, 0, 0), (0, 0, 1, 0, 0, 0, 0, 0), 
                                                         (0, 0, 0, 1, 0, 0, 0, 0), (0, 0, 0, 0, 1, 0, 0, 0), (0, 0, 0, 0, 0, 1, 0, 0), (0, 0, 0, 0, 0, 0, 1, 0), (0, 0, 0, 0, 0, 0, 0, 1)], 
                                                         ['x_3_6', 'x_4_1', 'x_4_2', 'x_4_3', 'x_4_4', 'x_4_5', 'x_4_6', 'x_4_7'], csp.BINARY, name = 'c_prec'))

'''
myCsp.add_constraint(csp.Constraint.from_configurations([(1, 0, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0, 0, 0), (0, 1, 0, 0, 0, 0, 0, 0, 0), (0, 0, 1, 0, 0, 0, 0, 0, 0), 
                                                         (0, 0, 0, 1, 0, 0, 0, 0, 0), (0, 0, 0, 0, 1, 0, 0, 0, 0), (0, 0, 0, 0, 0, 1, 0, 0, 0), (0, 0, 0, 0, 0, 0, 1, 0, 0), 
                                                         (0, 0, 0, 0, 0, 0, 0, 1, 0), (0, 0, 0, 0, 0, 0, 0, 0, 1)],['x_3_7', 'x_4_1', 'x_4_2', 'x_4_3', 'x_4_4', 'x_4_5', 'x_4_6', 'x_4_7', 'x_4_8'], 
                                                         csp.BINARY, name = 'c_prec'))
myCsp.add_constraint(csp.Constraint.from_configurations([(1, 0, 0, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0, 0, 0, 0), (0, 1, 0, 0, 0, 0, 0, 0, 0, 0), 
                                                         (0, 0, 1, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 1, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 1, 0, 0, 0, 0, 0), 
                                                         (0, 0, 0, 0, 0, 1, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 1, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0, 1, 0, 0), 
                                                         (0, 0, 0, 0, 0, 0, 0, 0, 1, 0), (0, 0, 0, 0, 0, 0, 0, 0, 0, 1)],
                                                         ['x_3_8', 'x_4_1', 'x_4_2', 'x_4_3', 'x_4_4', 'x_4_5', 'x_4_6', 'x_4_7', 'x_4_8', 'x_4_9'], csp.BINARY, name = 'c_prec'))
myCsp.add_constraint(csp.Constraint.from_configurations([(1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), (0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0), 
                                                         (0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0), 
                                                         (0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0), 
                                                         (0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0), (0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0), (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1)], 
                                                         ['x_3_9', 'x_4_1', 'x_4_2', 'x_4_3', 'x_4_4', 'x_4_5', 'x_4_6', 'x_4_7', 'x_4_8', 'x_4_9', 'x_4_10'], csp.BINARY, name = 'c_prec'))
'''

'''
#for i in range(beginTimes_op1.size):
#    if i < beginTimes_op1.size: 
#        constr = csp.Constraint.from_func(c_precedence(beginTimes_op1[i], beginTimes_op2[i], beginTimes_op2[i+1]))
#        myCsp.add_constraint(constr) 
#        print('precedence constraint added: ', beginTimes_op1[i], beginTimes_op2[i], beginTimes_op2[i+1])   

'''
# capacity constraints for machine 1, assigned to op1, op3, both with process time = 2
myCsp.add_constraint(csp.Constraint.from_configurations([(1, 0, 0), (0, 0, 0), (0, 0, 1), (0, 1, 0)],['x_1_1', 'x_3_1', 'x_3_2'], csp.BINARY, name = 'c_mach'))
myCsp.add_constraint(csp.Constraint.from_configurations([(1, 0, 0), (0, 0, 0), (0, 0, 1), (0, 1, 0)],['x_1_2', 'x_3_2', 'x_3_3'], csp.BINARY, name = 'c_mach'))
myCsp.add_constraint(csp.Constraint.from_configurations([(1, 0, 0), (0, 0, 0), (0, 0, 1), (0, 1, 0)],['x_1_3', 'x_3_3', 'x_3_4'], csp.BINARY, name = 'c_mach'))
myCsp.add_constraint(csp.Constraint.from_configurations([(1, 0, 0), (0, 0, 0), (0, 0, 1), (0, 1, 0)],['x_1_4', 'x_3_4', 'x_3_5'], csp.BINARY, name = 'c_mach'))
myCsp.add_constraint(csp.Constraint.from_configurations([(1, 0, 0), (0, 0, 0), (0, 0, 1), (0, 1, 0)],['x_1_5', 'x_3_5', 'x_3_6'], csp.BINARY, name = 'c_mach'))
myCsp.add_constraint(csp.Constraint.from_configurations([(1, 0, 0), (0, 0, 0), (0, 0, 1), (0, 1, 0)],['x_1_6', 'x_3_6', 'x_3_7'], csp.BINARY, name = 'c_mach'))
myCsp.add_constraint(csp.Constraint.from_configurations([(1, 0, 0), (0, 0, 0), (0, 0, 1), (0, 1, 0)],['x_1_7', 'x_3_7', 'x_3_8'], csp.BINARY, name = 'c_mach'))
myCsp.add_constraint(csp.Constraint.from_configurations([(1, 0, 0), (0, 0, 0), (0, 0, 1), (0, 1, 0)],['x_1_8', 'x_3_8', 'x_3_9'], csp.BINARY, name = 'c_mach'))
myCsp.add_constraint(csp.Constraint.from_configurations([(1, 0, 0), (0, 0, 0), (0, 0, 1), (0, 1, 0)],['x_1_9', 'x_3_9', 'x_3_10'], csp.BINARY, name = 'c_mach'))

myCsp.add_constraint(csp.Constraint.from_configurations([(1, 0, 0), (0, 0, 0), (0, 0, 1), (0, 1, 0)],['x_3_1', 'x_1_1', 'x_1_2'], csp.BINARY, name = 'c_mach'))
myCsp.add_constraint(csp.Constraint.from_configurations([(1, 0, 0), (0, 0, 0), (0, 0, 1), (0, 1, 0)],['x_3_2', 'x_1_2', 'x_1_3'], csp.BINARY, name = 'c_mach'))
myCsp.add_constraint(csp.Constraint.from_configurations([(1, 0, 0), (0, 0, 0), (0, 0, 1), (0, 1, 0)],['x_3_3', 'x_1_3', 'x_1_4'], csp.BINARY, name = 'c_mach'))
myCsp.add_constraint(csp.Constraint.from_configurations([(1, 0, 0), (0, 0, 0), (0, 0, 1), (0, 1, 0)],['x_3_4', 'x_1_4', 'x_1_5'], csp.BINARY, name = 'c_mach'))
myCsp.add_constraint(csp.Constraint.from_configurations([(1, 0, 0), (0, 0, 0), (0, 0, 1), (0, 1, 0)],['x_3_5', 'x_1_5', 'x_1_6'], csp.BINARY, name = 'c_mach'))
myCsp.add_constraint(csp.Constraint.from_configurations([(1, 0, 0), (0, 0, 0), (0, 0, 1), (0, 1, 0)],['x_3_6', 'x_1_6', 'x_1_7'], csp.BINARY, name = 'c_mach'))
myCsp.add_constraint(csp.Constraint.from_configurations([(1, 0, 0), (0, 0, 0), (0, 0, 1), (0, 1, 0)],['x_3_7', 'x_1_7', 'x_1_8'], csp.BINARY, name = 'c_mach'))
myCsp.add_constraint(csp.Constraint.from_configurations([(1, 0, 0), (0, 0, 0), (0, 0, 1), (0, 1, 0)],['x_3_8', 'x_1_8', 'x_1_9'], csp.BINARY, name = 'c_mach'))
myCsp.add_constraint(csp.Constraint.from_configurations([(1, 0, 0), (0, 0, 0), (0, 0, 1), (0, 1, 0)],['x_3_9', 'x_1_9', 'x_1_10'], csp.BINARY, name = 'c_mach'))


# capacity constraints for machine 2, assigned to op2 (process time = 3), op4 (process time = 3)
myCsp.add_constraint(csp.Constraint.from_configurations([(1, 0, 0, 0), (0, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1)],['x_2_1', 'x_4_1', 'x_4_2', 'x_4_3'], csp.BINARY, name = 'c_mach'))
myCsp.add_constraint(csp.Constraint.from_configurations([(1, 0, 0, 0), (0, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1)],['x_2_2', 'x_4_2', 'x_4_3', 'x_4_4'], csp.BINARY, name = 'c_mach'))
myCsp.add_constraint(csp.Constraint.from_configurations([(1, 0, 0, 0), (0, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1)],['x_2_3', 'x_4_3', 'x_4_4', 'x_4_5'], csp.BINARY, name = 'c_mach'))
myCsp.add_constraint(csp.Constraint.from_configurations([(1, 0, 0, 0), (0, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1)],['x_2_4', 'x_4_4', 'x_4_5', 'x_4_6'], csp.BINARY, name = 'c_mach'))
myCsp.add_constraint(csp.Constraint.from_configurations([(1, 0, 0, 0), (0, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1)],['x_2_5', 'x_4_5', 'x_4_6', 'x_4_7'], csp.BINARY, name = 'c_mach'))
myCsp.add_constraint(csp.Constraint.from_configurations([(1, 0, 0, 0), (0, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1)],['x_2_6', 'x_4_6', 'x_4_7', 'x_4_8'], csp.BINARY, name = 'c_mach'))
myCsp.add_constraint(csp.Constraint.from_configurations([(1, 0, 0, 0), (0, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1)],['x_2_7', 'x_4_7', 'x_4_8', 'x_4_9'], csp.BINARY, name = 'c_mach'))
myCsp.add_constraint(csp.Constraint.from_configurations([(1, 0, 0, 0), (0, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1)],['x_2_8', 'x_4_8', 'x_4_9', 'x_4_10'], csp.BINARY, name = 'c_mach'))

myCsp.add_constraint(csp.Constraint.from_configurations([(1, 0, 0, 0), (0, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1)],['x_4_1', 'x_2_1', 'x_2_2', 'x_2_3'], csp.BINARY, name = 'c_mach'))
myCsp.add_constraint(csp.Constraint.from_configurations([(1, 0, 0, 0), (0, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1)],['x_4_2', 'x_2_2', 'x_2_3', 'x_2_4'], csp.BINARY, name = 'c_mach'))
myCsp.add_constraint(csp.Constraint.from_configurations([(1, 0, 0, 0), (0, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1)],['x_4_3', 'x_2_3', 'x_2_4', 'x_2_5'], csp.BINARY, name = 'c_mach'))
myCsp.add_constraint(csp.Constraint.from_configurations([(1, 0, 0, 0), (0, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1)],['x_4_4', 'x_2_4', 'x_2_5', 'x_2_6'], csp.BINARY, name = 'c_mach'))
myCsp.add_constraint(csp.Constraint.from_configurations([(1, 0, 0, 0), (0, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1)],['x_4_5', 'x_2_5', 'x_2_6', 'x_2_7'], csp.BINARY, name = 'c_mach'))
myCsp.add_constraint(csp.Constraint.from_configurations([(1, 0, 0, 0), (0, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1)],['x_4_6', 'x_2_6', 'x_2_7', 'x_2_8'], csp.BINARY, name = 'c_mach'))
myCsp.add_constraint(csp.Constraint.from_configurations([(1, 0, 0, 0), (0, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1)],['x_4_7', 'x_2_7', 'x_2_8', 'x_2_9'], csp.BINARY, name = 'c_mach'))
myCsp.add_constraint(csp.Constraint.from_configurations([(1, 0, 0, 0), (0, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1)],['x_4_8', 'x_2_8', 'x_2_9', 'x_2_10'], csp.BINARY, name = 'c_mach'))


bb = myCsp.check({'x_1_1':1, 'x_1_2':0, 'x_1_3':0, 'x_1_4':0, 'x_1_5':0, 'x_1_6':0, 'x_1_7':0, 'x_1_8':0, 'x_1_9':0, 'x_1_10':0, 
                  'x_2_1':0, 'x_2_2':0, 'x_2_3':1, 'x_2_4':0, 'x_2_5':0, 'x_2_6':0, 'x_2_7':0, 'x_2_8':0, 'x_2_9':0, 'x_2_10':0, 
                  'x_3_1':0, 'x_3_2':0, 'x_3_3':1, 'x_3_4':0, 'x_3_5':0, 'x_3_6':0, 'x_3_7':0, 'x_3_8':0, 'x_3_9':0, 'x_3_10':0, 
                  'x_4_1':0, 'x_4_2':0, 'x_4_3':0, 'x_4_4':0, 'x_4_5':0, 'x_4_6':1, 'x_4_7':0, 'x_4_8':0, 'x_4_9':0, 'x_4_10':0})

print('myCsp check: ', bb)

bqm = csp.stitch(myCsp, 2, 10)
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

optimize = False

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

sampler = SimulatedAnnealingSampler()
response = sampler.sample(bqm,num_reads=5,num_sweeps=1000)
for datum in response.data(['sample', 'energy']):
    print(datum.sample, datum.energy)


