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


def is_sorted(sequence):
    for i in xrange(len(sequence) - 1):
        if sequence[i] > sequence[i+1]:
            return False
    return True


def process_subsets(subsets):
    processed_subsets = list()
    for subset in subsets:
        subset_copy = list(subset)
        subset_copy.sort()
        processed_subset = [1 + subset_copy.index(subset[i]) for i in xrange(len(subset))]
        processed_subsets.append(tuple(processed_subset))
    return processed_subsets


def is_order_in_permutation(permutation, order):
    all_subsets = get_subsets(permutation, len(order))
    all_subsets = set(process_subsets(all_subsets))
    if tuple(order) in all_subsets:
        return True
    return False


def does_permutation_satisfy_constraint(permutation):
    prev_odd_ele = -1
    i = 0
    for ele in permutation:
        if ele % 2 == 1:
            if ele < prev_odd_ele:
                return False
            if (ele + 1) not in set(permutation[i+1:]):
                return False
            prev_odd_ele = ele
        i += 1
    return True


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


def compute_tn(n, order):
    all_permutations = compute_all_permutations(range(1, n+1))
    tot_count = 0
    for permutation in all_permutations:
        if does_permutation_satisfy_constraint(permutation):
            if not is_order_in_permutation(permutation, order):
                print " ".join([str(ele) for ele in permutation])
                tot_count += 1
    return tot_count


if __name__ == '__main__':
    n = int(sys.argv[1])
    order = [3,2,1]
    for i in xrange(n):
        if (2*i < len(order)):
            continue
        print compute_tn(2*i, order)
