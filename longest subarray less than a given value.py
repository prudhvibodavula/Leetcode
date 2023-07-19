def bestSumAnyTreePath(parent, values):
    # Helper function to perform the recursive traversal
    def traverse(node):
        nonlocal parent, values
        # If the node is None, return 0 as the sum
        if node is None:
            return 0

        # Calculate the sum including the current node's value
        sum_including = values[node]
        for child in tree[node]:
            sum_including = max(sum_including, values[node] + traverse(child))

        # Return the sum including the current node's value
        return sum_including

    # Build the tree representation using the parent array
    tree = [[] for _ in parent]
    for i, p in enumerate(parent):
        if p != -1:
            tree[p].append(i)

    # Start the traversal from the root node (node 0)
    return traverse(0)


parent = [-1, 0, 1, 2, 0]
values = [-2, 10, 10, -3, 10]
print(bestSumAnyTreePath(parent, values))
