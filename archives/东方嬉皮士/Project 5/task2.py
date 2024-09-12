import numpy as np


def generate_p_matrix(num_states):
    p = np.zeros([num_states, num_states])
    for i in range(num_states):
        row_sum = 0
        for j in range(num_states):
            p[i][j] = np.random.rand(1)[0]
            row_sum += p[i][j]
        p[i, :] = p[i, :] / row_sum
    return p


def generate_b_matrix(num_states, num_objects):
    b = np.zeros([num_states, num_objects])
    for i in range(num_states):
        row_sum = 0
        for j in range(num_objects):
            b[i][j] = np.random.rand(1)[0]
            row_sum += b[i][j]
        b[i, :] = b[i, :] / row_sum
    return b


np.random.seed(200476024)
num_states = 4
num_objects = 3
S = (1, 2, 3, 4)
V = (1, 2, 3)
initial_distribution = np.array((1, 0, 0, 0))

one_step_transition_matrix = generate_p_matrix(num_states)
print('Transition matrix')
print(one_step_transition_matrix)
print(f'Testing normalization for p matrix. Sum of p matrix rows: {np.sum(one_step_transition_matrix, axis=1)}')

event_matrix = generate_b_matrix(4, 3)
print('Event matrix')
print(event_matrix)
print(f'Testing normalization for b matrix. Sum of b matrix rows: {np.sum(event_matrix, axis=1)}')
