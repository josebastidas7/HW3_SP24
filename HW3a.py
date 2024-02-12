import DoolittleMethod as dm
import copy

def Transpose(A):
    """
    This function finds the transpose of a square matrix.
    :param A: an nxn matrix
    :return: the transpose of A
    """
    n = len(A)
    return [[A[j][i] for j in range(n)] for i in range(n)]

def Cholesky(Aaug):
    """
    This function finds the solution to a matrix equation Ax=b by the Cholesky method.
    :param Aaug: An augmented matrix
    :return: the solution vector x, L, and Ltrans as a tuple
    """
    A, b = dm.separateAugmented(Aaug)
    n = len(A)

    # Step 1: Check if A is symmetric and positive definite
    if not SymPosDef(A):
        print("Matrix is not symmetric and positive definite. Using Doolittle method.")
        return dm.Doolittle(Aaug)

    # Step 2: Factor into L and Ltrans using Cholesky formula
    L = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1):
            s = sum(L[i][k] * L[j][k] for k in range(j))
            if i == j:
                L[i][j] = (A[i][i] - s) ** 0.5
            else:
                L[i][j] = (1.0 / L[j][j] * (A[i][j] - s))

    # Step 3: Use backsolving to find x
    LT = Transpose(L)
    y = dm.BackSolve(L, b, UT=False)
    x = dm.BackSolve(LT, y, UT=True)

    return x, L, LT

def main():
    # Define matrices A1 and A2
    A1 = [[1, -1, 3, 2],
          [-1, 5, -5, -2],
          [3, -5, 19, 3],
          [2, -2, 3, 21]]

    A2 = [[4, 2, 4, 0],
          [2, 2, 3, 2],
          [4, 3, 6, 3],
          [0, 2, 3, 9]]

    # Test Cholesky method for A1
    print("Problem 1:")
    print("Matrix A1:")
    for row in A1:
        print(row)

    result1 = Cholesky(A1)
    print("\nSolution using Cholesky method:")
    print("x =", result1[0])
    print("L:")
    for row in result1[1]:
        print(row)
    print("\nLT:")
    for row in result1[2]:
        print(row)

    # Test Cholesky method for A2
    print("\nProblem 2:")
    print("Matrix A2:")
    for row in A2:
        print(row)

    result2 = Cholesky(A2)
    print("\nSolution using Cholesky method:")
    print("x =", result2[0])
    print("L:")
    for row in result2[1]:
        print(row)
    print("\nLT:")
    for row in result2[2]:
        print(row)

if __name__ == "__main__":
    main()
# I used the help from CHATGPT
# I used the help from DR. Smay's github repository 
