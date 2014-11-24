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
     random_vectors = get_random_vectors(n, N)
     max_dp = 0.0
     for i in xrange(len(random_vectors)):
         for j in xrange(i+1, len(random_vectors)):
             dp = compute_dp(random_vectors[i], random_vectors[j])
             if max_dp < abs(dp):
                 max_dp = abs(dp)
     return max_dp


def get_min_epsilon(n, N, num_iter):
    min_epsilon = 1.0
    for i in xrange(num_iter):
        epsilon = compute_epsilon_random(n, N)
        if epsilon < min_epsilon:
            min_epsilon = epsilon
    print min_epsilon ** 2


if __name__ == '__main__':
    get_min_epsilon(4, 5, 1000000)
        
