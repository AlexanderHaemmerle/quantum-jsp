'''
Created on 10.05.2019

@author: ahaemm
'''
from builtins import str

# import datetime

# kommentar
#a, b = 0, 1
#while b < 10:
#    print(b)
#    a, b = b, a + b

    
def createListOB(n):
    aList = []
    for i in range(n):
         a = False
         aList.append(a);
    return aList
    
l = createListOB(10)
print(l) 


# Represent the map as the nodes and edges of a graph
provinces = ['AB', 'BC', 'MB', 'NB', 'NL', 'NS', 'NT', 'NU', 'ON', 'PE', 'QC', 'SK', 'YT']
neighbors = [('AB', 'BC'), ('AB', 'NT'), ('AB', 'SK'), ('BC', 'NT'), ('BC', 'YT'), ('MB', 'NU'),
             ('MB', 'ON'), ('MB', 'SK'), ('NB', 'NS'), ('NB', 'QC'), ('NL', 'QC'), ('NT', 'NU'),
             ('NT', 'SK'), ('NT', 'YT'), ('ON', 'QC')]

# Function for the constraint that two nodes with a shared edge not both select one color
def not_both_1(v, u):
    return not (v and u)



# Valid configurations for the constraint that each node select a single color
one_color_configurations = {(0, 0, 0, 1), (0, 0, 1, 0), (0, 1, 0, 0), (1, 0, 0, 0)}
colors = len(one_color_configurations)


# Add constraint that each node (province) select a single color
for province in provinces:
    variables = [province+str(i) for i in range(colors)]
    print(variables)

# Add constraint that each pair of nodes with a shared edge not both select one color
for neighbor in neighbors:
    v, u = neighbor
    for i in range(colors):
        variables = [v+str(i), u+str(i)]
        print(variables)


def createBeginTimeVariables(job, nrTimeslots):
    alist = []
    for i in range(nrTimeslots):
        alist.append('B_O' + str(job) + '_' + str(i+1))
    return alist  

def createMachineAssignmentVariables(job, nrMachines):
    alist = []
    for i in range(nrMachines):
        alist.append('M_O' + str(job) + '_' + str(i+1))
    return alist  

 

print(createBeginTimeVariables(1, 10))
print(createBeginTimeVariables(2, 10))
print(createMachineAssignmentVariables(1, 4))
print(createMachineAssignmentVariables(2, 4))
    
    
