import sys

verbose = False


def get_sequence(first_term, num, k):
    terms = [first_term]
    for i in xrange(num):
        if k == 1:
            next_term = get_next_term_one(terms)
        else:
            next_term = get_next_term(terms, k)
        terms.append(next_term)
    return terms


def get_next_term(terms, k):
    possible_term = terms[-1] + 1
    while not does_term_work(possible_term, terms, k):
        possible_term += 1
    return possible_term


def does_term_work(possible_term, terms, k):
    term_set = set([k * term for term in terms])
    for term in terms:
        if ((term + possible_term) in term_set and
                (possible_term != (k - 1) * term)):
            if verbose:
                print possible_term, list_not_working_pairs(
                    possible_term, terms, k)
            return False
    return True


def get_next_term_one(terms):
    possible_term = terms[-1] + 1
    while not does_term_work_one(possible_term, terms):
        possible_term += 1
    return possible_term


def does_term_work_one(possible_term, terms):
    term_set = set(terms)
    for term in terms:
        if (possible_term - term) in term_set and (possible_term != (2 * term)):
            return False
    return True


def list_not_working_pairs(possible_term, terms, k):
    term_set = set([k * term for term in terms])
    not_working_pairs = list()
    for term in terms:
        if ((term + possible_term) in term_set):
            not_working_pairs.append((term, (possible_term + term) / k))
    return not_working_pairs


if __name__ == '__main__':
    k = int(sys.argv[1])
    num_terms = int(sys.argv[2])
    terms = get_sequence(0, num_terms, k)
    print terms
