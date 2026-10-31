def nearest_power_of_2(x):
    """Given an integer, return the nearest power of 2.

    Args:
        x (int): a positive integer

    Returns:
        int: the nearest power of 2 of x
    """
    ##################
    # YOUR CODE HERE #
    ##################

    return 2 ** int(np.ceil(np.log2(x)))
