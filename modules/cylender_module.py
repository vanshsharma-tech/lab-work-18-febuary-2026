def cylender_volume(radius, height):
    return 3.14 * radius**2 * height


def cylender_curved_surface_area(radius, height):
    return 2 * 3.14 * radius * height


def cylender_total_surface_area(radius, height):
    return 2 * 3.14 * radius*(radius + height)
