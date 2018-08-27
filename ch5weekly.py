import math


def area_of_circle(r):

    return(r**2*math.pi)


def main():

    radius = 10
    a = area_of_circle(radius)
    print(a)


if __name__ == "__main__":
    main()
