import random


def get_random_vectors(n, N):
    random_vectors = list()
    for i in xrange(N):
        random_vector = list()
        norm = 0.0
        for i in xrange(n):
            random_vector.append(random.random() - 0.5)
            norm += (random_vector[-1] ** 2)
        norm = norm ** 0.5
        for i in xrange(n):
            random_vector[i] = random_vector[i] / norm
        random_vectors.append(random_vector)
    return random_vectors


def compute_dp(vector1, vector2):
    dp = 0.0
    for i in xrange(len(vector1)):
        dp += (vector1[i] * vector2[i])
    return dp


def compute_epsilon_random(n, N):
     # random_vectors = get_random_vectors(n, N)
     # a = 0.85
     # b = 0.53
     a = 0.53
     b = 0.85
     random_vectors = [[a, b, 0.0], [a, -b, 0], [b, 0, a], [b, 0.0, -a], [0, a, b], [0, -a, b]]
     max_dp = 0.0
     for i in xrange(len(random_vectors)):
         for j in xrange(i+1, len(random_vectors)):
             dp = compute_dp(random_vectors[i], random_vectors[j])
             if max_dp < abs(dp):
                 max_dp = abs(dp)
     return max_dp, random_vectors


def get_min_epsilon(n, N, num_iter):
    min_epsilon = 1.0
    best_vectors = None
    for i in xrange(num_iter):
        if i % 10 == 0:
            print "Done with iteration %d..." % i
            print "Minimum epsilon seen so far %.2f..." % min_epsilon ** 2
            print "Best vectors so far:", best_vectors
            print
        epsilon, random_vectors = compute_epsilon_random(n, N)
        if epsilon < min_epsilon:
            min_epsilon = epsilon
            best_vectors = random_vectors
    print min_epsilon ** 2


if __name__ == '__main__':
    get_min_epsilon(3, 6, 100)
 
