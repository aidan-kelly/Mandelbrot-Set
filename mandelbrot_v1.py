import numpy
import matplotlib.pyplot as plt

MAX_X = 2.0
MAX_Y = 2.0
MIN_X = -2.0
MIN_Y = -2.0
SCALE = 1000.0
WIDTH = int((SCALE * MAX_X) * 2) + 1
HEIGHT = int((SCALE * MAX_Y) * 2) + 1

#z^2+c
#c is complex tuple.
#z is the previous iteration.
def ZCalc(startingTup):
    IsOutOfRange = False

    workingComplex = complex(startingTup[0], startingTup[1])
    result = workingComplex
    count = 0
    #first iteration
    while not IsOutOfRange:
        z = result * result
        c = workingComplex
        result = z + c

        count += 1
        
        if(result.real > MAX_X or result.real < MIN_X):
            IsOutOfRange = True

        if(result.imag > MAX_Y or result.imag < MIN_Y):
            IsOutOfRange = True

        if((result.real == z.real and result.imag == z.imag) or count >= 50):
            break

    return count

# Displays the passed in array.
def DisplaySet(matrix):
    matrix = numpy.rot90(matrix)
    plt.imshow(matrix)
    plt.show()

# Takes in a numpy array.
# Computes the ZCalc for each entry in the array.
def CalculateSet(matrix):
    outputArray = numpy.empty([WIDTH, HEIGHT])

    for x in range(WIDTH):
        for y in range(HEIGHT):
            outputArray[x][y] = ZCalc(matrix[x][y])
    
    return outputArray

    


def main():
    array = numpy.empty([WIDTH, HEIGHT], tuple)

    for x in range(WIDTH):
        xCoord = MIN_X + (x / SCALE)

        for y in range(HEIGHT):
            yCoord = MIN_Y + (y / SCALE)
            array[x][y] = (xCoord, yCoord)

    outputArray = CalculateSet(array)
    DisplaySet(outputArray)

main()