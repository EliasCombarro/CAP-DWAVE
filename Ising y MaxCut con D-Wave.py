import numpy as np
import dimod

# Especificar los coeficientes del problema que queremos resolver es muy sencillo
# Empezaremos con un caso muy sencillo

J = {(0,1):1}

h = {}
model = dimod.BinaryQuadraticModel(h, J, 0.0, dimod.SPIN)

print("El modelo que vamos a resolver es")
print(model)
print()

# Podemos resolver el modelo de forma exacta


from dimod.reference.samplers import ExactSolver
sampler = ExactSolver()
solution = sampler.sample(model)
print("La solucion exacta es")
print(solution)


# O con *simulated annealing* (un método heurístico de optimización para ordenadores clásicos)


sampler = dimod.SimulatedAnnealingSampler()
response = sampler.sample(model, num_reads=10)
print("La solucion con simulated annealing es")
print(response)


# Y, por supuesto, con el ordenador cuántico de D-Wave 


from dwave.system.samplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite
sampler = EmbeddingComposite(DWaveSampler())
response = sampler.sample(model, num_reads=5000)
print("La solucion con el quantum annealer de D-Wave es")
print(response)


# Veamos ahora un caso un poco más complicado

J = {(0,1):1,(0,2):1,(1,2):1,(1,3):1,(2,4):1,(3,4):1}
h = {}
print("El modelo que vamos a resolver es")
model = dimod.BinaryQuadraticModel(h, J, 0.0, dimod.SPIN)


# Primero lo resolvemos de forma exacta

sampler = ExactSolver()
solution = sampler.sample(model)
print("La solucion exacta es")
print(solution)


# Ahora, con *simulated annealing*

sampler = dimod.SimulatedAnnealingSampler()
response = sampler.sample(model, num_reads=10)
print("La solucion con simulated annealing es")
print(response)


# Finalmente, lo resolvemos nuevamente con el *quantum annealer*


sampler = EmbeddingComposite(DWaveSampler())
response = sampler.sample(model, num_reads=5000)
print("La solucion con el quantum annealer de D-Wave es")
print(response)

