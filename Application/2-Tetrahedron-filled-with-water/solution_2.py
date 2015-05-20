def fill_tetrahedron(num):
    """ determine the amount of water that can be filled in a regular
        tetrahedron with side num
        fill_tetrahedron(Integer) -> Float
    """

    from math import sqrt
    
    volume=(num**3)/(6*sqrt(2)) # volume of tetrahedron in cubic cm

    return volume*0.001 #convert to liters

def tetrahedron_filled(tetrahedrons, water):
    """ return the maximum number of tetrahedrons that can be field
        with "water" liters of water
        tetrahedrons - list of edge sizes
        tetrahedron_filled(list of integers, integer) -> integer
    """
    tetrahedrons.sort()
    liters=map(fill_tetrahedron,tetrahedrons)
    filled=0
    for tetrh in liters:
        if water>=tetrh:
            filled+=1
            water-=tetrh

    return filled
