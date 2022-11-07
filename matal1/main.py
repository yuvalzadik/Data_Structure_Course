# מגישים:
# יובל צדיק , תז: 208996231
# ניר תשובה, תז: 318636891

def main():
    # before running please type: pip install numpy
    import numpy as np

    def define_2d_array(m):

        arr = np.random.randint(0, 2, size=(m, m))
        return arr

    def BigCross1(M, m):
        wings_size = 0
        x = 0
        y = 0
        max_wings = 0
        # iterating over the matrix
        for i in range(m):
            for j in range(m):
                if M[i][j] == 1:
                    wings_size = 1
                    # if cell is not in border and surronding cells are 1
                    while (i - wings_size >= 0 and j - wings_size >= 0 and i + wings_size < m and j + wings_size <m and
                            M[i - wings_size][j] == 1 and M[i][j - wings_size] == 1 and
                           M[i + wings_size][j] == 1 and M[i][j + wings_size] == 1):
                        # if current size is bigger than max, update max wing size and coordinates
                        if max_wings < wings_size:
                            max_wings = wings_size
                            x = i
                            y = j
                        wings_size += 1
        return x, y, max_wings

    def BigCross2(M,m):
        #each matrix contains the maximum number of 1s to the left/right/top/bottom of current place
        left = [[0 for x in range(m)] for y in range(m)]
        right = [[0 for x in range(m)] for y in range(m)]
        top = [[0 for x in range(m)] for y in range(m)]
        bottom = [[0 for x in range(m)] for y in range(m)]

        # initialize the border cells of the matrices
        for i in range(m):
            top[0][i] = M[0][i]
            bottom[m - 1][i] = M[m - 1][i]
            left[i][0] = M[i][0]
            right[i][m - 1] = M[i][m - 1]

        # fill all cells according to the given matrix
        for i in range(m):
            for j in range(1, m):
                # left matrix
                if M[i][j] == 1:
                    left[i][j] = left[i][j - 1] + 1

                # top matrix
                if M[j][i] == 1:
                    top[j][i] = top[j - 1][i] + 1

                # bottom matrix
                if M[m - 1 - j][i] == 1:
                    bottom[m - 1 - j][i] = bottom[m - j][i] + 1

                # right matrix
                if M[i][m - 1 - j] == 1:
                    right[i][m - 1 - j] = right[i][m - j] + 1

        maxWing = 0
        x = 0
        y = 0
        # find longest wing
        for i in range(m):
            for j in range(m):
                # find the suitable wing size
                wingSize = min(top[i][j], bottom[i][j], left[i][j], right[i][j])

                # if current size bigger than max, replace max
                if wingSize - 1 > maxWing:
                    maxWing = wingSize - 1
                    x = i
                    y = j

        return x, y, maxWing

    matrix15 = [
        [1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0],
        [1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0],
        [1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
        [0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
        [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1],
        [1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0],
        [1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0],
        [1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
        [1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1],
        [1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0],
        [1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0],
        [1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0]
    ]
    print("Using firs method:")
    m: int = 50
    binary_2d_array = define_2d_array(m)
    print("The random array:")
    print(binary_2d_array)
    x, y, max_wings = BigCross1(binary_2d_array, m)
    print("middle point: [", x, ",", y, "]")
    print("max wings size:", max_wings)

    print("The preset array:")
    print(matrix15)
    x, y, max_wings = BigCross1(matrix15, 15)
    print("middle point: [", x, ",", y, "]")
    print("max wings size:", max_wings)

    print("Using second method:")
    print("random array:")
    x, y, max_wings = BigCross2(binary_2d_array, m)
    print("middle point: [", x, ",", y, "]")
    print("max wings size:", max_wings)
    print("preset array:")
    x, y, max_wings = BigCross2(matrix15, 15)
    print("middle point: [", x, ",", y, "]")
    print("max wings size:", max_wings)



if __name__ == '__main__':
    main()
