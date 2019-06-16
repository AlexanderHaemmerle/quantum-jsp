'''
creates a penalty model for the precedence constraint between op_1, op_i+1 
with length 2, i.e. the process time of op_1 = 2; this penalty model can also be 
used for capacity constraints with reference process time = 2 

Created on 18.05.2019

@author: ahaemm
'''
import penaltymodel.core as pm
import networkx as nx
import dimod
from penaltymodel.cache.interface import cache_penalty_model

variables = ['i_1', 'i+1_1', 'i+1_2']

feasible_configs = {(1, 0, 0), (0, 0, 0), (0, 0, 1), (0, 1, 0)}

graph = nx.Graph()
graph.add_edges_from([('i_1', 'i+1_1'), ('i_1', 'i+1_2')])
spec = pm.Specification(graph, variables, feasible_configs, dimod.BINARY)
qubo = dimod.BinaryQuadraticModel({'i_1':0., 'i+1_1':0., 'i+1_2':0.,},
                               {('i_1', 'i+1_1'):1., ('i_1', 'i+1_2'):1.,}, 0.0,
                               dimod.BINARY)

ground_energy = qubo.energy({'i_1':1., 'i+1_1':0., 'i+1_2':0.})
print(ground_energy)


pModel = pm.PenaltyModel.from_specification(spec, qubo, 2, 0)
cache_penalty_model(pModel, 'c:\\Users\\ahaemm\\workspace\\dwave\\env\\data\\dwave-penaltymodel-cache\\penaltymodel_cache_v0.4.0.db')


#pm_tmp = get_penalty_model(spec_sumBeginTimes_op4, 'c:\\Users\\ahaemm\\workspace\\dwave\\env\\data\\dwave-penaltymodel-cache\\penaltymodel_cache_v0.4.0.db')
