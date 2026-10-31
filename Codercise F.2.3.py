num_wires = 2
dev = qp.device("default.qubit", wires=num_wires)

@qp.qnode(dev)
def decompose_two_qubit_QFT(basis_id):
    """A circuit that computes the QFT on two qubits using elementary gates.

    Args:
        basis_id (int): An integer value identifying the basis state to construct.

    Returns:
        array[complex]: The state of the qubits after the QFT operation.
    """
    # Prepare the basis state |basis_id>
    bits = [int(x) for x in np.binary_repr(basis_id, width=num_wires)]
    qp.BasisState(bits, wires=[0, 1])

    ##################
    # YOUR CODE HERE #
    ##################

    qp.Hadamard(wires = 0)
    qp.ctrl(qp.S(wires=0), control = 1)
    qp.Hadamard(wires = 1)
    qp.SWAP(wires = [0,1])
    return qp.state()
