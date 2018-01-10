def dist(seq_1, seq_2):
    """Take two DNA sequences of the same length and returns the Hamming distance between them"""
    dis = 0	
    for a, b in zip(seq_1.casefold(), seq_2.casefold()):
        if a != b:
            dis += 1
    print('The hamming distance between the sequences is:', dis)
    return dis
