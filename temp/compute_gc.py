def compute_gc(seq): # seq should be a string 
    """Calculate the GC content in the sequence input."""
    num_GC = list(seq).count('g')+list(seq).count('c')+list(seq).count('G')+list(seq).count('C')
    amount_GC = num_GC/len(seq)
    return amount_GC
