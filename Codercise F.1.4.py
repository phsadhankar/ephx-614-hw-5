def fft_multiplication(poly_a, poly_b):
    """Returns the result of multiplying two polynomials

    Args:
        poly_a (array[complex]): 1-D array of coefficients
        poly_b (array[complex]): 1-D array of coefficients

    Returns:
        array[complex]: complex coefficients of the product
            of the polynomials, with length equal to the
            nearest power of 2 (as returned by
            values_to_coefficients, including trailing zeros)
    """
    ##################
    # YOUR CODE HERE #
    ##################

    # Calculate the number of values required
    x = len(poly_a) + len(poly_b) -1
    # Figure out the nearest power of 2
    m = nearest_power_of_2(x)
    # Pad zeros to the polynomial
    poly_a = np.pad(poly_a, pad_width = (0, m - len(poly_a)), mode = 'constant')
    poly_b = np.pad(poly_b, pad_width = (0, m - len(poly_b)), mode = 'constant')
    # Convert the polynomials to value representation
    val_a = coefficients_to_values(poly_a)
    val_b = coefficients_to_values(poly_b)
    # Multiply
    val_c = np.multiply(val_a, val_b)
    # Convert back to coefficient representation
    c = values_to_coefficients(val_c)

    return c
