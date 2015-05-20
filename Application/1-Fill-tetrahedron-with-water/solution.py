def fill_tetrahedron(num):
    """ determine the amount of water that can be filled in a regular
        tetrahedron with side num
        fill_tetrahedron(Integer) -> Float
    """

    from math import sqrt
    
    volume=(num**3)/(6*sqrt(2)) # volume of tetrahedron in cubic cm

    return volume*0.001 #convert to liters
