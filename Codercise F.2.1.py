num_wires = 1
dev = qp.device("default.qubit", wires=num_wires)

@qp.qnode(dev)
def one_qubit_QFT(basis_id):
    """A circuit that computes the QFT on a single qubit.

    Args:
        basis_id (int): An integer value identifying
            the basis state to construct.

    Returns:
        array[complex]: The state of the qubit after applying QFT.
    """
    # Prepare the basis state |basis_id>
    bits = [int(x) for x in np.binary_repr(basis_id, width=num_wires)]
    qp.BasisState(bits, wires=[0])

    ##################
    # YOUR CODE HERE #
    ##################
    qp.Hadamard(wires = 0)
    return qp.state()
