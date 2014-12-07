import random
from scipy.optimize import minimize
import numpy as np


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


def normalize_vector(vector):
    norm = 0.0
    for i in xrange(len(vector)):
        norm += (vector[i] ** 2)
    norm = norm ** 0.5
    for i in xrange(len(vector)):
        vector[i] /= norm


def normalize_vectors(vectors):
    for vector in vectors:
        normalize_vector(vector)


def compute_dp(vector1, vector2):
    dp = 0.0
    for i in xrange(len(vector1)):
        dp += (vector1[i] * vector2[i])
    return dp


def compute_epsilon(vectors):
    max_dp = 0.0
    for i in xrange(len(vectors)):
        for j in xrange(i+1, len(vectors)):
            dp = compute_dp(vectors[i], vectors[j])
            if max_dp < abs(dp):
                max_dp = abs(dp)
    return max_dp ** 2


def compute_epsilon_random(n, N):
    # random_vectors = get_random_vectors(n, N)
    # a = 0.85
    # b = 0.53
    a = 0.53
    b = 0.85
    random_vectors = [[a, b, 0.0], [a, -b, 0], [b, 0, a], [b, 0.0, -a], [0, a, b], [0, -a, b]]
    epsilon = compute_epsilon(random_vectors)
    return epsilon, random_vectors

# Here assume we're given 6 vectors of dimension 3
def obj(x):
    x1 = x[0:3]
    x2 = x[3:6]
    x3 = x[6:9]
    x4 = x[9:12]
    x5 = x[12:15]
    x6 = x[15:]
    return compute_epsilon([x1, x2, x3, x4, x5, x6])


def jac(x, start, end, n, N):
    jac = []
    for i in xrange(n*N):
        if (i >= start and i < end):
            jac.append(2 * x[i])
        else:
            jac.append(0.0)
    return np.array(jac)


def construct_constraints(n, N):
    constraints = []
    start = 0
    for i in xrange(N):
        end = start + n
        constraints.append({'type':'eq',
            'fun': lambda x: compute_dp(x[start:end], x[start:end]) - 1,
            'jac': lambda x: jac(x, start, end, n, N)})
        start += n
    return constraints


def find_optimal_vectors(x0):
    constraints = construct_constraints(3, 6)
    res = minimize(obj, x0, method='SLSQP', constraints=constraints)
    return res.x


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


def get_min_epsilon_with_annealing(n, N, num_iter, start_vectors):
    min_epsilon = 1.0
    current_vectors = start_vectors
    i = 0
    while (i < num_iter):
        temperature = 1.0 / float(i + 1)
        
        # Get perturbing vectors
        random_vectors = get_random_vectors(n, N)
        # Now perturb current_vectors
        new_vectors = list()
        for j in xrange(N):
            new_vector = list()
            for k in xrange(n):
                new_vector.append(current_vectors[j][k] + (temperature * random_vectors[j][k]))
            new_vectors.append(new_vector)
        normalize_vectors(new_vectors)
        epsilon = compute_epsilon(new_vectors)
        if epsilon < min_epsilon:
            min_epsilon = epsilon
            current_vectors = new_vectors
            i += 1
    return min_epsilon, current_vectors


if __name__ == '__main__':
    min_epsilon = 1.0
    best_vectors = None
    n, N = 4, 12
    for i in xrange(100):    
        epsilon, vectors = get_min_epsilon_with_annealing(n, N, 21, get_random_vectors(n, N))
        if (epsilon < min_epsilon):
            min_epsilon = epsilon
            best_vectors = vectors
    print
    print "Min epsilon = %.4f..." % min_epsilon
    print "Best vectors:", best_vectors
    print
