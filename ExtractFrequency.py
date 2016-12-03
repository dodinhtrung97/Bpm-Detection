# Calculate position of a sample maxima given nearby samples
# Use quadratic interpolation


def findMaxima(vector, index):

    # Input type: vector, index of said vector

    curVector = vector[index]  # Current vector
    preVector = vector[index - 1]  # Element 1 index before input vector
    postVector = vector[index + 1]  # Element 1 index after input vector

    # Process Output as coordinates

    posX = 1/2. * (preVector - postVector) / (preVector - 2 * curVector + postVector) + index
    posY = curVector - 1/4. * (preVector - postVector) * (posX - index)

    # Return position of the vertex of the parabola that goes through x and its neighbors

    return posX, posY
