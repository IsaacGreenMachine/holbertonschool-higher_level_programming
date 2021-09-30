#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    newA = tupleSetup(tuple_a)
    newB = tupleSetup(tuple_b)
    return((newA[0] + newB[0], newA[1] + newB[1]))


def tupleSetup(tuple_z=()):
    if len(tuple_z) == 0:
        return((0, 0))
    elif len(tuple_z) == 1:
        return(tuple_z[0], 0)
    else:
        return((tuple_z[0], tuple_z[1]))
