#!/usr/bin/env python
# coding: utf-8

# # Resolviendo el modelo de Ising y el problema del corte máximo con un ordenador de D-Wave
# 
# En este notebook, vamos a utilizar un ordenador cuántico de D-Wave para resolver casos del modelo de Ising que se corresponden con instancias del problema del corte máximo en grafos. 
# 
# El hamiltoniano del modelo de Ising es $$H = \sum_{i,j=1}^n J_{i,j}Z_iZ_j + \sum_{i=1}^n h_iZ_i$$ 
# 
# En el caso particular del problema del corte máximo, se tiene $J_{i,j}=1$ y $h_i=0$ para todos los valores $i,j$.
# 
# 

# Definir el modelo con el que vamos a trabajar es muy sencillo: se reduce a especificar los valores de las conexiones entre pares de qubits y los coeficientes $h_i$. Por ejemplo:

# In[1]:


import numpy as np
import dimod

J = {(0,1):1}

h = {}
model = dimod.BinaryQuadraticModel(h, J, 0.0, dimod.SPIN)

print(model)


# Podemos resolver el modelo de forma exacta

# In[2]:


from dimod.reference.samplers import ExactSolver
sampler = ExactSolver()
solution = sampler.sample(model)
print(solution)


# O con *simulated annealing* (un método heurístico de optimización para ordenadores clásicos)

# In[3]:


sampler = dimod.SimulatedAnnealingSampler()
response = sampler.sample(model, num_reads=10)
print(response)


# Y, por supuesto, con el ordenador cuántico de D-Wave (requiere registro online en https://cloud.dwavesys.com/leap/)

# In[4]:


from dwave.system.samplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite
sampler = EmbeddingComposite(DWaveSampler())
response = sampler.sample(model, num_reads=5000)
print(response)


# Veamos ahora un caso un poco más complicado, que se corresponde con encontrar un corte máximo en el grafo de la figura
# 
# <img src="max-cut.png" width="60%">

# In[5]:


J = {(0,1):1,(0,2):1,(1,2):1,(1,3):1,(2,4):1,(3,4):1}
h = {}
model = dimod.BinaryQuadraticModel(h, J, 0.0, dimod.SPIN)


# Primero lo resolvemos de forma exacta

# In[6]:


sampler = ExactSolver()
solution = sampler.sample(model)
print(solution)


# Ahora, con *simulated annealing*

# In[7]:


sampler = dimod.SimulatedAnnealingSampler()
response = sampler.sample(model, num_reads=10)
print(response)


# Finalmente, lo resolvemos nuevamente con el *quantum annealer*

# In[8]:


sampler = EmbeddingComposite(DWaveSampler())
response = sampler.sample(model, num_reads=5000)
print(response)

