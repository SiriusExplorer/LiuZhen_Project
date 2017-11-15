def add_even_nums(a, b):    # a, b should be integers
    """Compute the sum of all even integers between a and b, inclusively and return it."""
    if a > b:
        tmp = a
        a = b
        b = tmp
    if a <= b:
        all_num = list(range(a, b)) + [b]
        even_num = []
        for i in all_num:
            if i % 2 == 0:
                even_num.append(i)
        print('the sum of all even integers between a and b (include a and b) is:', sum(even_num))

