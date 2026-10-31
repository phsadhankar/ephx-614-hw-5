num_wires = 2
dev = qp.device("default.qubit", wires=num_wires)

@qp.qnode(dev)
def two_qubit_QFT(basis_id):
    """A circuit that computes the QFT on two qubits using qp.QubitUnitary.

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

    U_QFT = 0.5 * np.array([
        [np.exp(0.5j * np.pi * i * j) for j in range(4)]
        for i in range(4)
    ])

    #Apply it to the state
    qp.QubitUnitary(U_QFT, wires = [0,1])
    return qp.state()
