num_wires = 3
dev = qp.device("default.qubit", wires=num_wires)

@qp.qnode(dev)
def three_qubit_QFT(basis_id):
    """A circuit that computes the QFT on three qubits.

    Args:
        basis_id (int): An integer value identifying the basis state to construct.

    Returns:
        array[complex]: The state of the qubits after the QFT operation.
    """
    # Prepare the basis state |basis_id>
    bits = [int(x) for x in np.binary_repr(basis_id, width=num_wires)]
    qp.BasisState(bits, wires=[0, 1, 2])

    ##################
    # YOUR CODE HERE #
    ##################

    qp.Hadamard(wires=0)
    qp.ctrl(qp.S(wires=0), control=1)
    qp.ctrl(qp.T(wires=0), control=2)
    qp.Hadamard(wires=1)
    qp.ctrl(qp.S(wires=1), control=2)
    qp.Hadamard(wires=2)
    qp.SWAP(wires=[0,2])

    return qp.state()
