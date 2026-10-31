estimation_wires = [0, 1, 2]
target_wires = [3]

def apply_controlled_powers_of_U(unitary):
    """A quantum function that applies the sequence of powers of U^2^k to
    the estimation wires.

    Args:
        unitary (array [complex]): A unitary matrix
    """

    ##################
    # YOUR CODE HERE #
    ##################
    for k, wire in enumerate(reversed(estimation_wires)):
        power = 2**k
        U_power = np.linalg.matrix_power(unitary, power)
        qp.ctrl(qp.QubitUnitary(U_power, wires=target_wires), control=wire)
