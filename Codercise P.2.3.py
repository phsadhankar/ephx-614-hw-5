dev = qp.device("default.qubit", wires=4)

estimation_wires = [0, 1, 2]
target_wires = [3]

def prepare_eigenvector():
    qp.PauliX(wires=target_wires)

@qp.qnode(dev)
def qpe(unitary):
    """ Estimate the phase for a given unitary.

    Args:
        unitary (array[complex]): A unitary matrix.

    Returns:
        array[float]: Measurement outcome probabilities on the estimation wires.
    """
    ##################
    # YOUR CODE HERE #
    ##################
    prepare_eigenvector()
    for wire in estimation_wires:
        qp.Hadamard(wires=wire)
    apply_controlled_powers_of_U(unitary)
    qp.adjoint(qp.QFT)(wires=estimation_wires)
    return qp.probs(wires=estimation_wires)

U = qp.T.compute_matrix()
print(qpe(U))
