dev = qp.device('default.qubit', wires=4)

@qp.qnode(dev)
def pennylane_qft(basis_id, n_qubits):
    """A that circuit performs the QFT using PennyLane's QFT template.

    Args:
        basis_id (int): An integer value identifying
            the basis state to construct.
        n_qubits (int): An integer identifying the
            number of qubits.

    Returns:
        array[complex]: The state after applying the QFT to the qubits.
    """
    # Prepare the basis state |basis_id>
    bits = [int(x) for x in np.binary_repr(basis_id, width=n_qubits)]
    qp.BasisState(bits, wires=range(n_qubits))

    ##################
    # YOUR CODE HERE #
    ##################
    qp.QFT(range(n_qubits))
    return qp.state()
