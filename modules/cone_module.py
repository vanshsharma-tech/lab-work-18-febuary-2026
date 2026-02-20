import math   


#  Slant Height Function
def slant_height(r, h):
    return math.sqrt(r**2 + h**2)


#  Volume Function
def volume_cone(r, h):
    return (1/3) * math.pi * r**2 * h


#  Curved Surface Area Function
def cone_curved_surface_area(r, h):
    l = slant_height(r, h)
    return math.pi * r * l


# Total Surface Area Function
def total_surface_area(r, h):
    l = slant_height(r, h)
    return math.pi * r * (l + r)
