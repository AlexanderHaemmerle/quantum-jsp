'''
Created on 19.05.2019
creates a penalty model for the "begin times overlap" constraint between two 
operations with reference process time = 1

@author: ahaemm
'''
import penaltymodel.core as pm
import networkx as nx
import dimod
from penaltymodel.cache.interface import cache_penalty_model

variables = ['i_1', 'k_1']

feasible_configs = {(1, 0), (0, 0), (0, 1)}

graph = nx.Graph()
graph.add_edges_from([('i_1', 'k_1')])
spec = pm.Specification(graph, variables, feasible_configs, dimod.BINARY)
qubo = dimod.BinaryQuadraticModel({'i_1':0., 'k_1':0.,},
                               {('i_1', 'k_1'):1.,}, 0.0,
                               dimod.BINARY)

ground_energy = qubo.energy({'i_1':1., 'k_1':0.})
print(ground_energy)


pModel = pm.PenaltyModel.from_specification(spec, qubo, 2., 0.)
cache_penalty_model(pModel, 'c:\\Users\\ahaemm\\workspace\\dwave\\env\\data\\dwave-penaltymodel-cache\\penaltymodel_cache_v0.4.0.db')


#pm_tmp = get_penalty_model(spec_sumBeginTimes_op4, 'c:\\Users\\ahaemm\\workspace\\dwave\\env\\data\\dwave-penaltymodel-cache\\penaltymodel_cache_v0.4.0.db')
