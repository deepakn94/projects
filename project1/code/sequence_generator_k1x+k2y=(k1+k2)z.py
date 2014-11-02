import sys

verbose = False


def get_sequence_linear_equation(first_term, num, k1, k2):
    terms = [first_term]
    for i in xrange(num):
        next_term = get_next_term_linear_equation(terms, k1, k2)
        terms.append(next_term)
    return terms


def get_next_term_linear_equation(terms, k1, k2):
    possible_term = terms[-1] + 1
    while not does_term_work_linear_equation(possible_term, terms, k1, k2):
        possible_term += 1
    return possible_term


def does_term_work_linear_equation(possible_term, terms, k1, k2):
    term_set_k1 = set([term * k1 for term in terms])
    term_set_k2 = set([term * k2 for term in terms])
    for term in terms:
        if ((((k1 + k2) * term - (k2 * possible_term)) in term_set_k1) or
            (((k1 + k2) * term - (k1 * possible_term)) in term_set_k2)):
            return False
    return True


if __name__ == '__main__':
    k1 = int(sys.argv[1])
    k2 = int(sys.argv[2])
    num_terms = int(sys.argv[3])
    terms = get_sequence_linear_equation(0, num_terms, k1, k2)
    print ", ".join([str(term) for term in terms])
