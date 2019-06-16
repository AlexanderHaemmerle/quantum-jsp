'''
create penalty model for the [(1,0), (0,0), (0,1)] constraint between x_i_t, x_j_k;
create penalty models for precedence constraints between op_i, op_i+1, with process time (op_i) = 2,
#time slots = 10

Created on 20.05.2019

@author: ahaemm
'''

import penaltymodel.core as pm
import networkx as nx
import dimod
from penaltymodel.cache.interface import cache_penalty_model

### create penalty model for the [(1,0), (0,0), (0,1)] constraint between x_i_t, x_j_k;
variables = ['i_t', 'j_k']

feasible_configs = {(1, 0), (0, 0), (0, 1)}

graph = nx.Graph()
graph.add_edges_from([('i_t', 'j_k')])
spec = pm.Specification(graph, variables, feasible_configs, dimod.BINARY)
qubo = dimod.BinaryQuadraticModel({'i_t':0., 'j_k':0.},
                               {('i_t', 'j_k'):1.}, 0.0,
                               dimod.BINARY)

ground_energy = qubo.energy({'i_t':1., 'j_k':0.})
print(ground_energy)

pModel = pm.PenaltyModel.from_specification(spec, qubo, 2, 0)
cache_penalty_model(pModel, 'c:\\Users\\ahaemm\\workspace\\dwave\\env\\data\\dwave-penaltymodel-cache\\penaltymodel_cache_v0.4.0.db')



### t = 2, t' = 1,2,3
variables = ['i_2', 'k_1', 'k_2', 'k_3']

# op k may not start earlier than i_2, and not while i_2 is running
feasible_configs = {(1, 0, 0, 0), (0, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1)}

graph = nx.Graph()
graph.add_edges_from([('i_2', 'k_1'), ('i_2', 'k_2'), ('i_2', 'k_3')])
spec = pm.Specification(graph, variables, feasible_configs, dimod.BINARY)
qubo = dimod.BinaryQuadraticModel({'i_2':0., 'k_1':0., 'k_2':0., 'k_3':0.},
                               {('i_2', 'k_1'):1., ('i_2', 'k_2'):1., ('i_2', 'k_3'):1.}, 0.0,
                               dimod.BINARY)

ground_energy = qubo.energy({'i_2':1., 'k_1':0., 'k_2':0., 'k_3':0})
print(ground_energy)

pModel = pm.PenaltyModel.from_specification(spec, qubo, 2, 0)
cache_penalty_model(pModel, 'c:\\Users\\ahaemm\\workspace\\dwave\\env\\data\\dwave-penaltymodel-cache\\penaltymodel_cache_v0.4.0.db')

### t = 3, t' = 1,2,3,4
variables = ['i_3', 'k_1', 'k_2', 'k_3', 'k_4']

feasible_configs = {(1, 0, 0, 0, 0), (0, 0, 0, 0, 0), (0, 1, 0, 0, 0), (0, 0, 1, 0, 0), (0, 0, 0, 1, 0), (0, 0, 0, 0, 1)}

graph = nx.Graph()
graph.add_edges_from([('i_3', 'k_1'), ('i_3', 'k_2'), ('i_3', 'k_3'), ('i_3', 'k_4')])
spec = pm.Specification(graph, variables, feasible_configs, dimod.BINARY)
qubo = dimod.BinaryQuadraticModel({'i_3':0., 'k_1':0., 'k_2':0., 'k_3':0., 'k_4':0.},
                               {('i_3', 'k_1'):1., ('i_3', 'k_2'):1., ('i_3', 'k_3'):1., ('i_3', 'k_4'):1.}, 0.0,
                               dimod.BINARY)

ground_energy = qubo.energy({'i_3':1., 'k_1':0., 'k_2':0., 'k_3':0, 'k_4':0.})
print(ground_energy)

pModel = pm.PenaltyModel.from_specification(spec, qubo, 2, 0)
cache_penalty_model(pModel, 'c:\\Users\\ahaemm\\workspace\\dwave\\env\\data\\dwave-penaltymodel-cache\\penaltymodel_cache_v0.4.0.db')

### t = 4, t' = 1,2,3,4,5
variables = ['i_3', 'k_1', 'k_2', 'k_3', 'k_4', 'k_5']

feasible_configs = {(1, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0), (0, 1, 0, 0, 0, 0), (0, 0, 1, 0, 0, 0), (0, 0, 0, 1, 0, 0), (0, 0, 0, 0, 1, 0), (0, 0, 0, 0, 0, 1)}

graph = nx.Graph()
graph.add_edges_from([('i_3', 'k_1'), ('i_3', 'k_2'), ('i_3', 'k_3'), ('i_3', 'k_4'), ('i_3', 'k_5')])
spec = pm.Specification(graph, variables, feasible_configs, dimod.BINARY)
qubo = dimod.BinaryQuadraticModel({'i_3':0., 'k_1':0., 'k_2':0., 'k_3':0., 'k_4':0., 'k_5':0.},
                               {('i_3', 'k_1'):1., ('i_3', 'k_2'):1., ('i_3', 'k_3'):1., ('i_3', 'k_4'):1., ('i_3', 'k_5'):1.}, 0.0,
                               dimod.BINARY)

ground_energy = qubo.energy({'i_3':1., 'k_1':0., 'k_2':0., 'k_3':0, 'k_4':0., 'k_5':0.})
print(ground_energy)

pModel = pm.PenaltyModel.from_specification(spec, qubo, 2, 0)
cache_penalty_model(pModel, 'c:\\Users\\ahaemm\\workspace\\dwave\\env\\data\\dwave-penaltymodel-cache\\penaltymodel_cache_v0.4.0.db')

### t = 5, t' = 1,2,3,4,5,6
variables = ['i_3', 'k_1', 'k_2', 'k_3', 'k_4', 'k_5', 'k_6']

feasible_configs = {(1, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0), (0, 1, 0, 0, 0, 0, 0), (0, 0, 1, 0, 0, 0, 0), (0, 0, 0, 1, 0, 0, 0), (0, 0, 0, 0, 1, 0, 0), (0, 0, 0, 0, 0, 1, 0), (0, 0, 0, 0, 0, 0, 1)}

graph = nx.Graph()
graph.add_edges_from([('i_3', 'k_1'), ('i_3', 'k_2'), ('i_3', 'k_3'), ('i_3', 'k_4'), ('i_3', 'k_5'), ('i_3', 'k_6')])
spec = pm.Specification(graph, variables, feasible_configs, dimod.BINARY)
qubo = dimod.BinaryQuadraticModel({'i_3':0., 'k_1':0., 'k_2':0., 'k_3':0., 'k_4':0., 'k_5':0., 'k_6':0.},
                               {('i_3', 'k_1'):1., ('i_3', 'k_2'):1., ('i_3', 'k_3'):1., ('i_3', 'k_4'):1., ('i_3', 'k_5'):1., ('i_3', 'k_6'):1.}, 0.0,
                               dimod.BINARY)

ground_energy = qubo.energy({'i_3':1., 'k_1':0., 'k_2':0., 'k_3':0, 'k_4':0., 'k_5':0., 'k_6':0.})
print(ground_energy)

pModel = pm.PenaltyModel.from_specification(spec, qubo, 2, 0)
cache_penalty_model(pModel, 'c:\\Users\\ahaemm\\workspace\\dwave\\env\\data\\dwave-penaltymodel-cache\\penaltymodel_cache_v0.4.0.db')

### t = 6, t' = 1,2,3,4,5,6,7
variables = ['i_3', 'k_1', 'k_2', 'k_3', 'k_4', 'k_5', 'k_6', 'k_7']

feasible_configs = {(1, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0, 0), (0, 1, 0, 0, 0, 0, 0, 0), (0, 0, 1, 0, 0, 0, 0, 0), 
                    (0, 0, 0, 1, 0, 0, 0, 0), (0, 0, 0, 0, 1, 0, 0, 0), (0, 0, 0, 0, 0, 1, 0, 0), (0, 0, 0, 0, 0, 0, 1, 0), (0, 0, 0, 0, 0, 0, 0, 1)}

graph = nx.Graph()
graph.add_edges_from([('i_3', 'k_1'), ('i_3', 'k_2'), ('i_3', 'k_3'), ('i_3', 'k_4'), ('i_3', 'k_5'), ('i_3', 'k_6'), ('i_3', 'k_7')])
spec = pm.Specification(graph, variables, feasible_configs, dimod.BINARY)
qubo = dimod.BinaryQuadraticModel({'i_3':0., 'k_1':0., 'k_2':0., 'k_3':0., 'k_4':0., 'k_5':0., 'k_6':0., 'k_7':0.},
                               {('i_3', 'k_1'):1., ('i_3', 'k_2'):1., ('i_3', 'k_3'):1., ('i_3', 'k_4'):1., ('i_3', 'k_5'):1., ('i_3', 'k_6'):1., 
                                ('i_3', 'k_7'):1.}, 0.0,
                               dimod.BINARY)

ground_energy = qubo.energy({'i_3':1., 'k_1':0., 'k_2':0., 'k_3':0, 'k_4':0., 'k_5':0., 'k_6':0., 'k_7':0.})
print(ground_energy)

pModel = pm.PenaltyModel.from_specification(spec, qubo, 2, 0)
cache_penalty_model(pModel, 'c:\\Users\\ahaemm\\workspace\\dwave\\env\\data\\dwave-penaltymodel-cache\\penaltymodel_cache_v0.4.0.db')

### t = 7, t' = 1,2,3,4,5,6,7,8
variables = ['i_3', 'k_1', 'k_2', 'k_3', 'k_4', 'k_5', 'k_6', 'k_7', 'k_8']

feasible_configs = {(1, 0, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0, 0, 0), (0, 1, 0, 0, 0, 0, 0, 0, 0), (0, 0, 1, 0, 0, 0, 0, 0, 0), 
                    (0, 0, 0, 1, 0, 0, 0, 0, 0), (0, 0, 0, 0, 1, 0, 0, 0, 0), (0, 0, 0, 0, 0, 1, 0, 0, 0), (0, 0, 0, 0, 0, 0, 1, 0, 0), 
                    (0, 0, 0, 0, 0, 0, 0, 1, 0), (0, 0, 0, 0, 0, 0, 0, 0, 1)}

graph = nx.Graph()
graph.add_edges_from([('i_3', 'k_1'), ('i_3', 'k_2'), ('i_3', 'k_3'), ('i_3', 'k_4'), ('i_3', 'k_5'), ('i_3', 'k_6'), ('i_3', 'k_7'), ('i_3', 'k_8')])
spec = pm.Specification(graph, variables, feasible_configs, dimod.BINARY)
qubo = dimod.BinaryQuadraticModel({'i_3':0., 'k_1':0., 'k_2':0., 'k_3':0., 'k_4':0., 'k_5':0., 'k_6':0., 'k_7':0., 'k_8':0.},
                               {('i_3', 'k_1'):1., ('i_3', 'k_2'):1., ('i_3', 'k_3'):1., ('i_3', 'k_4'):1., ('i_3', 'k_5'):1., ('i_3', 'k_6'):1., 
                                ('i_3', 'k_7'):1., ('i_3', 'k_8'):1.}, 0.0,
                               dimod.BINARY)

ground_energy = qubo.energy({'i_3':1., 'k_1':0., 'k_2':0., 'k_3':0, 'k_4':0., 'k_5':0., 'k_6':0., 'k_7':0., 'k_8':0.})
print(ground_energy)

pModel = pm.PenaltyModel.from_specification(spec, qubo, 2, 0)
cache_penalty_model(pModel, 'c:\\Users\\ahaemm\\workspace\\dwave\\env\\data\\dwave-penaltymodel-cache\\penaltymodel_cache_v0.4.0.db')

### t = 8, t' = 1,2,3,4,5,6,7,8,9
variables = ['i_3', 'k_1', 'k_2', 'k_3', 'k_4', 'k_5', 'k_6', 'k_7', 'k_8', 'k_9']

feasible_configs = {(1, 0, 0, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0, 0, 0, 0), (0, 1, 0, 0, 0, 0, 0, 0, 0, 0), (0, 0, 1, 0, 0, 0, 0, 0, 0, 0), 
                    (0, 0, 0, 1, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 1, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 1, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 1, 0, 0, 0), 
                    (0, 0, 0, 0, 0, 0, 0, 1, 0, 0), (0, 0, 0, 0, 0, 0, 0, 0, 1, 0), (0, 0, 0, 0, 0, 0, 0, 0, 0, 1)}

graph = nx.Graph()
graph.add_edges_from([('i_3', 'k_1'), ('i_3', 'k_2'), ('i_3', 'k_3'), ('i_3', 'k_4'), ('i_3', 'k_5'), ('i_3', 'k_6'), ('i_3', 'k_7'), ('i_3', 'k_8'), 
                      ('i_3', 'k_9')])
spec = pm.Specification(graph, variables, feasible_configs, dimod.BINARY)
qubo = dimod.BinaryQuadraticModel({'i_3':0., 'k_1':0., 'k_2':0., 'k_3':0., 'k_4':0., 'k_5':0., 'k_6':0., 'k_7':0., 'k_8':0., 'k_9':0.},
                               {('i_3', 'k_1'):1., ('i_3', 'k_2'):1., ('i_3', 'k_3'):1., ('i_3', 'k_4'):1., ('i_3', 'k_5'):1., ('i_3', 'k_6'):1., 
                                ('i_3', 'k_7'):1., ('i_3', 'k_8'):1., ('i_3', 'k_9'):1.}, 0.0,
                               dimod.BINARY)

ground_energy = qubo.energy({'i_3':1., 'k_1':0., 'k_2':0., 'k_3':0, 'k_4':0., 'k_5':0., 'k_6':0., 'k_7':0., 'k_8':0., 'k_9':0.})
print(ground_energy)

pModel = pm.PenaltyModel.from_specification(spec, qubo, 2, 0)
cache_penalty_model(pModel, 'c:\\Users\\ahaemm\\workspace\\dwave\\env\\data\\dwave-penaltymodel-cache\\penaltymodel_cache_v0.4.0.db')

### t = 9, t' = 1,2,3,4,5,6,7,8,9,10
variables = ['i_3', 'k_1', 'k_2', 'k_3', 'k_4', 'k_5', 'k_6', 'k_7', 'k_8', 'k_9', 'k_10']

feasible_configs = {(1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), (0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0), (0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0), 
                    (0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0), 
                    (0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0), (0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0), (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1)}

graph = nx.Graph()
graph.add_edges_from([('i_3', 'k_1'), ('i_3', 'k_2'), ('i_3', 'k_3'), ('i_3', 'k_4'), ('i_3', 'k_5'), ('i_3', 'k_6'), ('i_3', 'k_7'), ('i_3', 'k_8'), 
                      ('i_3', 'k_9'), ('i_3', 'k_10')])
spec = pm.Specification(graph, variables, feasible_configs, dimod.BINARY)
qubo = dimod.BinaryQuadraticModel({'i_3':0., 'k_1':0., 'k_2':0., 'k_3':0., 'k_4':0., 'k_5':0., 'k_6':0., 'k_7':0., 'k_8':0., 'k_9':0., 'k_10':0.},
                               {('i_3', 'k_1'):1., ('i_3', 'k_2'):1., ('i_3', 'k_3'):1., ('i_3', 'k_4'):1., ('i_3', 'k_5'):1., ('i_3', 'k_6'):1., 
                                ('i_3', 'k_7'):1., ('i_3', 'k_8'):1., ('i_3', 'k_9'):1., ('i_3', 'k_10'):1.}, 0.0,
                               dimod.BINARY)

ground_energy = qubo.energy({'i_3':1., 'k_1':0., 'k_2':0., 'k_3':0, 'k_4':0., 'k_5':0., 'k_6':0., 'k_7':0., 'k_8':0., 'k_9':0., 'k_10':0.})
print(ground_energy)

pModel = pm.PenaltyModel.from_specification(spec, qubo, 2, 0)
cache_penalty_model(pModel, 'c:\\Users\\ahaemm\\workspace\\dwave\\env\\data\\dwave-penaltymodel-cache\\penaltymodel_cache_v0.4.0.db')
