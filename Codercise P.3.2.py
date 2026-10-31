dev = qp.device("default.qubit", wires=10)

def estimates_array(unitary):
    """ Given a unitary, return a list of its phase windows

    Args:
        unitary (array[complex]): A unitary matrix.

    Returns:
        [(float, float)]: a list of phase windows for 2 to 9
        estimation wires
    """

    estimates = []
    target_wires = [9]

    ##################
    # YOUR CODE HERE #
    ##################
    for i in range(1,9):
        estimation_wires= [j for j in range(i+1)]
        probs = qpe(unitary, estimation_wires, target_wires)
        b1= phase_window(probs, estimation_wires)
        estimates.append(b1)

    return estimates

# Define the unitary
U = np.array([[1, 0], [0, np.exp((2*np.pi*1j/7))]])

estimates_array(U)

###################
# SUBMIT FOR PLOT #
###################
