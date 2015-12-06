from sys import argv
import csv


try:
    import axelrod

    strategies = []

    try:
        if type(axelrod.strategies) is list:
            strategies += axelrod.strategies
    except (AttributeError, TypeError):
        pass

    try:
        if type(axelrod.ordinary_strategies) is list:
            strategies += axelrod.ordinary_strategies
    except (AttributeError, TypeError):
        pass

    try:
        if type(axelrod.basic_strategies) is list:
            strategies += axelrod.basic_strategies
    except (AttributeError, TypeError):
        pass

    try:
        if type(axelrod.cheating_strategies) is list:
            strategies += axelrod.cheating_strategies
    except (AttributeError, TypeError):
        pass

    count = len(set(strategies))

    f = open('data', 'a')
    csvwrtr = csv.writer(f)
    csvwrtr.writerow([argv[1], count, argv[2]])
    f.close()

except:
    pass
