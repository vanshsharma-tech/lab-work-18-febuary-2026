def cuboid_volume(length, breadth, height):
    return length * breadth * height


def cuboid_total_surface_area(length, breadth, height):
    return 2 * (length * breadth + breadth * height + height * length)


def cuboid_lateral_surface_area(length, breadth, height):
    return 2 * height * (length + breadth)
