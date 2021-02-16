"""
Three functions applying basic image processing techniques to a list of h3 hexs.
"""
from h3 import h3


def erosion(hexs, diameter):
    """
    Given a list of h3 hexes, apply erosion to the implied black-and-white map.
    https://en.wikipedia.org/wiki/Erosion_(morphology)
    This helps us eliminate isolated hexs in our list / map.
    The diameter parameter is an integer that tells us how many hexs to cut on
    each side of any polygon in the implied map. Values like 1 or 2 are reasonable.
    """
    new_hexs = []
    for a_hex in hexs:
        adjacent_hexs = h3.k_ring(a_hex, diameter)
        covered = all(x in hexs for x in adjacent_hexs)
        if covered:
            new_hexs.append(a_hex)
    return new_hexs


def dilation(hexs, diameter):
    """
    Given a list of h3 hexes, apply dilation to the implied black-and-white map.
    https://en.wikipedia.org/wiki/Dilation_(morphology)
    This helps us fill in gaps in our list / map.
    The diameter parameter is an integer that tells us how many hexs to add on
    each side of any polygon in the implied map. Values like 1 or 2 are reasonable.
    """
    new_hex_set = set(hexs)
    for a_hex in hexs:
        adjacent_hexs = h3.k_ring(a_hex, diameter)
        new_hex_set = new_hex_set.union(adjacent_hexs)
    new_hexs = list(new_hex_set)
    return new_hexs


def apply_closing(hexs, diameter):
    """
    Given a list of h3 hexes, apply closing to the implied black-and-white map.
    https://homepages.inf.ed.ac.uk/rbf/HIPR2/close.htm
    This helps us smooth the map.
    The diameter parameter is an integer that tells us how many hexs to add and cut on
    each side of any polygon in the implied map. Values like 1 or 2 are reasonable.
    """
    old_hexs = hexs
    max_iterations = 10
    for i in range(max_iterations):
        new_hexs = erosion(dilation(old_hexs, diameter), diameter)
        if set(old_hexs) == set(new_hexs):
            break
        old_hexs = new_hexs
    return new_hexs
