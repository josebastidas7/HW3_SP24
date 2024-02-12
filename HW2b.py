# region imports
from hw2a import Simpson
#endregion

# region functions
def tPDF(m, u):
    """
    T-distribution Probability Density Function.
    :param m: degrees of freedom
    :param u: value at which to calculate the PDF
    :return: PDF value
    """
    numerator = gamma((m + 1) / 2)
    denominator = sqrt(m * pi) * gamma(m / 2) * (1 + u**2 / m)**((m + 1) / 2)
    return numerator / denominator

def gamma(x):
    """
    Gamma function.
    :param x: input value
    :return: gamma(x)
    """
    if x == 1:
        return 1
    elif x == 0.5:
        return sqrt(pi)
    else:
        return (x - 1) * gamma(x - 1)

def main():
    """
    Main function for testing tPDF and gamma functions.
    """
    # Example usage:
    degrees_of_freedom = int(input("Enter degrees of freedom: "))
    z_value = float(input("Enter z value: "))

    probability = Simpson(tPDF, degrees_of_freedom, -z_value, z_value, npoints=100)
    print(f'Probability for {degrees_of_freedom} degrees of freedom and z={z_value}: {probability}')

# endregion

# region function call(s)
if __name__ == "__main__":
    main()
# endregion
# I used help from CHATGPT
# I used help from the GITHUB repository from Dr. Smay.
