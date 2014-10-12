import sys


def get_subsets(permutation, length):
    if length == 0:
        return []
    if len(permutation) == length:
        return [list(permutation)]
    subsets = get_subsets(permutation[1:], length)
    smaller_subsets = get_subsets(permutation[1:], length - 1)
    if not smaller_subsets:
        subsets.append([permutation[0]])
    for smaller_subset in smaller_subsets:
        subsets.append([permutation[0]] + smaller_subset)
    return subsets


def process_subsets(subsets):
    processed_subsets = list()
    for subset in subsets:
        processed_subset = range(1, len(subset) + 1)
        processed_subset = sorted(processed_subset, key = lambda x: subset[x-1])
        processed_subsets.append(tuple(processed_subset))
    return processed_subsets


def is_order_in_permutation(permutation, order):
    all_subsets = get_subsets(permutation, len(order))
    all_subsets = set(process_subsets(all_subsets))
    if tuple(order) in all_subsets:
        return True
    return False


def compute_all_permutations(input_list):
    all_permutations = list()
    for i in xrange(len(input_list)):
        ele = input_list[i]
        new_input_list = input_list[:i] + input_list[i+1:]
        smaller_list_permutations = compute_all_permutations(new_input_list)
        if not smaller_list_permutations:
            all_permutations.append([ele])
        for smaller_list_permutation in smaller_list_permutations:
            all_permutations.append([ele] + smaller_list_permutation)
    return all_permutations


def compute_sn(n, order):
    all_permutations = compute_all_permutations(range(1, n+1))
    tot_count = 0
    for permutation in all_permutations:
        if not is_order_in_permutation(permutation, order):
            tot_count += 1
    return tot_count


if __name__ == '__main__':
    n = int(sys.argv[1])
    order = [5, 4, 1, 2, 3]
    k = len(order)
    for i in xrange(k, n):
        print compute_sn(i, order)

