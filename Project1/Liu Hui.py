from math import pi


# liu hui algorithm for finding pi to the epsilon-th level
# comments for calculations inside
def pi_LiuHui(epsilon):
    # initializes pi to be the area of a hexagon
    n = 6
    r = 1
    m = r
    # area = number of sides * radius * side length / 2
    pin = n * r * m / 2
    # calculates pi from a polygon of side 2n
    while True:
        # calculates the new side length given from the formula Liu Hui created
        m = ((m / 2) ** 2 + (r - (r ** 2 - m ** 2 / 4) ** (1 / 2)) ** 2) ** (1 / 2)
        # multiplies side length by 2
        n *= 2
        # evaluates the new area of pi with a polygon of double the side length
        pi2n = n * r * m / 2
        # if A2n - An is greater than epsilon, return A2n (i.e. eval pi to the epsilon-th digit)
        if (pi2n - pin) < epsilon:
            break
        # else, set pi_n to pi_2n and calculate a new pi_2n
        pin = pi2n
    return pi2n


# tests for epsilon = 0.0000000001 (first 11 digits of pi) and prints math.pi to compare to
def main():
    print(pi_LiuHui(0.001))
    print(pi)


# runs main function
if __name__ == '__main__':
    main()
