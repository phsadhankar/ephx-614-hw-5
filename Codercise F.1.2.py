def values_to_coefficients(values):
    """Returns the coefficient representation of a polynomial

    Args:
        values (array[complex]): a 1-D complex array with
            the value representation of a polynomial

    Returns:
        array[complex]: a 1-D complex array of coefficients
    """

    ##################
    # YOUR CODE HERE #
    ##################
    return np.fft.ifft(values)


A = [10.+0.j,  2.-2.j,  2.+0.j,  2.+2.j]
print(values_to_coefficients(A))
