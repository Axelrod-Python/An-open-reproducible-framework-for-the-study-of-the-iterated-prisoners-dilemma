import axelrod
from sys import argv

try:
    if type(len(axelrod.strategies)) is int:
        print argv[1], len(axelrod.strategies), argv[2]
except:
    pass
