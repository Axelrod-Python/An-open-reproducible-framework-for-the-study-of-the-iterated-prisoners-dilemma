"""
A script to write the number of available strategies in the library to a data
file. This is used in conjunction with scrape_repo.py to obtain the number of
strategies at any given commit.

A big thanks must go to Mario Wenzel for the discussion about this here:
http://vknight.org/unpeudemath/code/2015/12/05/I-think-this-is-the-way-to-crawl-a-git-repository/
"""
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
