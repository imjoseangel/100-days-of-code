import cProfile
from particlesim import benchmark

pr = cProfile.Profile()
pr.enable()
benchmark()
pr.disable()
pr.print_stats()
