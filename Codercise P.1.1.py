dev = qp.device("default.qubit", wires=2)

@qp.qnode(dev)
def guess_the_unitary(unitary):
    """Given a unitary that performs a Z or a -Z operation
    on a qubit, guess which one it is.

    Args:
        U (array[complex]): A unitary matrix, guaranteed to be either Z or -Z.

    Returns:
        array [int]:  Probabilities on  on the first qubit
        using qp.probs()
    """
    ##################
    # YOUR CODE HERE #
    ##################
    qp.Hadamard(0)
    qp.ControlledQubitUnitary(unitary, wires=[0, 1])
    qp.Hadamard(0)
    return qp.probs(0)

# Z gate
U = qp.PauliZ.compute_matrix()

# -Z gate
# U = (-1)*qp.PauliZ.compute_matrix()

print(guess_the_unitary(U))
