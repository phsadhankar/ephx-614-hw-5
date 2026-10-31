dev = qp.device("default.qubit", wires=2)

@qp.qnode(dev)
def phase_kickback_X(eigenvector):
    """ Given an eigenvector of X,
    apply the phase kickback circuit to observe
    the probabilities on the control wire

    Args:
        eigenvector(String): A string "plus" or "minus" depicting
        the eigenvector of X

    Returns:
        array[int]: Measurement outcome on the first qubit using qp.probs()
    """
    # Prepare |ψ>
    ##################
    # YOUR CODE HERE #
    ##################
    if eigenvector == "plus": qp.Hadamard(wires=1)
    elif eigenvector == "minus":
        qp.PauliX(wires=1)
        qp.Hadamard(wires=1)

    # Phase kickback
    ##################
    # YOUR CODE HERE #
    ##################
    qp.Hadamard(wires=0)
    qp.CNOT(wires=[0, 1])
    qp.Hadamard(wires=0)

    return qp.probs(wires=[0])

print(phase_kickback_X("plus"))
print(phase_kickback_X("minus"))

# MODIFY EIGENVALUES BELOW
eigenvalue_of_X_plus = 1
eigenvalue_of_X_minus = -1
