def U_power_2k(unitary, k):
    """ Computes U at a power of 2k (U^2^k)

    Args:
        unitary (array[complex]): A unitary matrix

    Returns:
        array[complex]: the unitary raised to the power of 2^k
    """
    ##################
    # YOUR CODE HERE #
    ##################
    return np.linalg.matrix_power(unitary, 2**k)


# Try out a higher power of U
U = qp.T.compute_matrix()
print(U)

U_power_2k(U, 2)
