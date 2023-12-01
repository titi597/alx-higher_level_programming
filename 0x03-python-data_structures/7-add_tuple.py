def add_tuple(tuple_a=(), tuple_b=()):
    # Extend tuples to have at least 2 elements
    tuple_a += (0, 0)
    tuple_b += (0, 0)

    # Create a new tuple with the sum of corresponding elements
    result_tuple = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    
    return result_tuple
