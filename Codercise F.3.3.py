dev = qp.device('default.qubit', wires=4)

def qft_rotations(n_qubits):
    """A circuit performs the QFT rotations on the specified qubits.

    Args:
        n_qubits (int): An integer value identifying the number of qubits.
    """

    ##################
    # YOUR CODE HERE #
    ##################
    for w in range(n_qubits):
        qp.Hadamard(w)
        for s in range(w+1,n_qubits):
            qp.ControlledPhaseShift(np.pi/2**(s-w),[s,w])

@qp.qnode(dev)
def qft_node(basis_id, n_qubits):
    # Prepare the basis state |basis_id>
    bits = [int(x) for x in np.binary_repr(basis_id, width=n_qubits)]
    qp.BasisState(bits, wires=range(n_qubits))
    qft_rotations(n_qubits)
    swap_bits(n_qubits)
    return qp.state()
