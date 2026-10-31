dev = qp.device('default.qubit', wires=4)

def qft_recursive_rotations(n_qubits, wire=0):
    """A circuit that performs the QFT rotations on the specified qubits
        recursively.

    Args:
        n_qubits (int): An integer value identifying the number of qubits.
        wire (int): An integer identifying the wire
                    (or the qubit) to apply rotations on.
    """

    ##################
    # YOUR CODE HERE #
    ##################
    if wire >= n_qubits: return

    qp.Hadamard(wire)
    for sub_wire in range(wire+1,n_qubits):
        qp.ControlledPhaseShift(np.pi/2**(sub_wire-wire),[sub_wire,wire])
    return qft_recursive_rotations(n_qubits,wire=wire+1)

@qp.qnode(dev)
def qft_node(basis_id, n_qubits):
    # Prepare the basis state |basis_id>
    bits = [int(x) for x in np.binary_repr(basis_id, width=n_qubits)]
    qp.BasisState(bits, wires=range(n_qubits))
    qft_recursive_rotations(n_qubits)
    swap_bits(n_qubits)
    return qp.state()
