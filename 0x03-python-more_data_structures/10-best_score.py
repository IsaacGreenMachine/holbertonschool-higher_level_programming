#!/usr/bin/python3
def best_score(a_dictionary):
    try:
        return max(a_dictionary.values())
    except:
        return None
