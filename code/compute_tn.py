import sys


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


def compute_tn(n):
    all_permutations = compute_all_permutations(range(1, n+1))
    tot_count = 0
    for permutation in all_permutations:
        if does_permutation_satisfy_constraint(permutation):
            tot_count += 1
    return tot_count


if __name__ == '__main__':
    n = int(sys.argv[1])
    for i in xrange(n):
        print compute_tn(2*i)
