from cone_module import *
from cuboid_module import *
from cylender_module import *

radius = float(input("Enter the radius:"))
height = float(input("Enter the height:"))
length = float(input("Enter the length:"))
breadth = float(input("Enter the breadth:"))

# Calculated the volume, curved surface area and total surface area of cone

print(f"The slant height of cone is: {round(slant_height(radius,height),2)}")
print(f"The volume of cone is: {round(volume_cone(radius,height),2)}")
print(
    f"The curved surface area of cone is: {round(cone_curved_surface_area(radius,height),2)}"
)
print(
    f"The total surface area of cone is : {round(total_surface_area(radius,height),2)}"
)

# Calculated the volume, total surface area and lateral surface area of cuboid

print(f"The volume of cuboid is: {round(cuboid_volume(length,breadth,height),2)}")
print(
    f"The Total surface area of cuboid is: {round(cuboid_total_surface_area(length,breadth,height),2)}"
)
print(
    f"The lateral surface area of cuboid is: {round(cuboid_lateral_surface_area(length,breadth,height),2)}"
)

# Calculated the volume, curved surface area and total surface area of cylender

print(f"The volume of cylender is: {round(cylender_volume(radius,height),2)}")
print(
    f"The curved surface area of cylender is: {round(cylender_curved_surface_area(radius,height),2)}"
)
print(
    f"The total surface area of cylender is : {round(cylender_total_surface_area(radius,height),2)}"
)
