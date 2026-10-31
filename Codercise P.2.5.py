dev = qp.device("default.qubit", wires=4)

estimation_wires = [0, 1, 2]
target_wires = [3]

def prepare_eigenvector():
    qp.PauliX(wires=target_wires)

@qp.qnode(dev)
def qpe(unitary):
    """Estimate the phase for a given unitary.

    Args:
        unitary (array[complex]): A unitary matrix.

    Returns:
        array[float]: Probabilities on the estimation wires.
    """

    prepare_eigenvector()

    ##################
    # YOUR CODE HERE #
    ##################
    qp.QuantumPhaseEstimation(unitary, target_wires,estimation_wires)
    return qp.probs(wires=estimation_wires)


U = qp.T.compute_matrix()
probs = qpe(U)
print(estimate_phase(probs))
