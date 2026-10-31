estimation_wires = [0, 1, 2]
target_wires = [3]

def estimate_phase(probs):
    """Estimate the value of a phase given measurement outcome probabilities
    of the QPE routine.

    Args:
        probs (array[float]): Probabilities on the estimation wires.

    Returns:
        float: the estimated phase
    """
    ##################
    # YOUR CODE HERE #
    ##################
    most_likely_index = np.argmax(probs)
    num_estimation_wires = len(estimation_wires)
    theta = most_likely_index / (2 ** num_estimation_wires)

    return theta

U = qp.T.compute_matrix()

probs = qpe(U)


estimated_phase = estimate_phase(probs)
print(estimated_phase)
