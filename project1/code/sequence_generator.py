import sys


def get_sequence(first_term, num):
    terms = [first_term]
    for i in xrange(num):
        next_term = get_next_term(terms)
        terms.append(next_term)
    return terms


def get_differences(terms):
    differences = list()
    for i in xrange(1, len(terms)):
        differences.append(terms[i] - terms[i-1])
    return differences


def get_next_term(terms):
    possible_term = terms[-1] + 1
    while not does_term_work(possible_term, terms):
        possible_term += 1
    return possible_term


def does_term_work(possible_term, terms):
    term_set = set([2 * term for term in terms])
    for term in terms:
        if (term + possible_term) in term_set:
            print possible_term, list_not_working_pairs(possible_term, terms)
            return False
    return True


def list_not_working_pairs(possible_term, terms):
    term_set = set([2 * term for term in terms])
    not_working_pairs = list()
    for term in terms:
        if (term + possible_term) in term_set:
            not_working_pairs.append((term, (possible_term + term) / 2))
    return not_working_pairs


if __name__ == '__main__':
    num = int(sys.argv[1])
    terms = get_sequence(0, num)
    print ", ".join([str(ele) for ele in terms])
    differences = get_differences(terms)
    print ", ".join([str(ele) for ele in differences])
