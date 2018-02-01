import graphviz as gz


def digraph_from_numpy_array(arr, labels=None, edge_fmt='{:.2f}'):
    """
    Returns a graphviz DiGraph from the given 2D numpy array. Shape of the array
    must be (N, N), N >= 1.

    Parameters
    ----------
    arr : numpy array
        NxN numpy array representing the adjacency matrix of the directed graph.
    labels : list
        A list of size N containing the label of i^th node.
    edge_fmt : str
        Format string to be used when formatting the edge values in the
        adjacency matrix.

    Returns
    -------
    digraph : graphviz.Digraph
        A graphviz.Digraph object corresponding to the passed adjacency matrix.
    """
    assert(arr.shape[0] == arr.shape[1])

    G = gz.Digraph()
    num_nodes = len(arr)
    if labels is None:
        labels = list(str(index) for index in range(num_nodes))

    for i in range(num_nodes):
        for j in range(num_nodes):
            if arr[i, j] != 0:
                G.edge(labels[i], labels[j], label=edge_fmt.format(arr[i, j]))

    return G
