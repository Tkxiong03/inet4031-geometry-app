import math

def surfaceArea(radius):
    return 4 * math.pi * radius ** 2


def volume(radius):
    return (4/3) * math.pi * radius ** 3


def prompt():
    print()
    print("------------------------------------------------------------")
    print("PYTHON PROGRAM TO FIND THE VOLUME OF A SPHERE")
    print("------------------------------------------------------------")
    
    radius = int(input("Please Enter the radius: "))

    vol = volume(radius)

    print("Volume of Sphere is:", vol)


if __name__ == '__main__':
    prompt()