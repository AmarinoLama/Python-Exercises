def modify_multiply(st, loc, num):
    tuple = st.split()
    output = tuple[loc]
    return ((output + "-")*num)[:-1]