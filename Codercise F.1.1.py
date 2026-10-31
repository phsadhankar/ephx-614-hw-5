def coefficients_to_values(coefficients):
    """Returns the value representation of a polynomial

    Args:
        coefficients (array[complex]): a 1-D array of complex
            coefficients of a polynomial with
            index i representing the i-th degree coefficient

    Returns:
        array[complex]: the value representation of the
            polynomial
    """
    ##################
    # YOUR CODE HERE #
    ##################
    return np.fft.fft(coefficients)

A = [4, 3, 2, 1]
print(coefficients_to_values(A))
