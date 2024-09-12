import numpy as np
from sklearn.preprocessing import LabelEncoder


def generate_p_matrix(num_states):
    p = np.zeros([num_states, num_states])
    for _ in range(num_states):
        row_sum = 0
        for j in range(num_states):
            p[_][j] = np.random.rand(1)[0]
            row_sum += p[_][j]
        p[_, :] = p[_, :] / row_sum
    return p


def generate_b_matrix(num_states, num_objects):
    b = np.zeros([num_states, num_objects])
    for _ in range(num_states):
        row_sum = 0
        for j in range(num_objects):
            b[_][j] = np.random.rand(1)[0]
            row_sum += b[_][j]
        b[_, :] = b[_, :] / row_sum
    return b


def next_state(p, cur_state):
    r = np.random.rand(1)
    state_transition_prob = p[cur_state - 1]
    for _ in range(len(state_transition_prob)):
        if r <= sum(state_transition_prob[:_ + 1]):
            return _ + 1
    return len(state_transition_prob)


def current_observation(b, cur_state):
    r = np.random.rand(1)
    event_prob = b[cur_state - 1]
    for _ in range(len(event_prob)):
        if r <= sum(event_prob[:_ + 1]):
            return _ + 1
    return len(event_prob)


def forward(p, b, pi, obs):
    alpha = np.zeros((len(obs), p.shape[0]))
    alpha[0, :] = pi * b[:, V[0] - 1]
    for t in range(1, len(obs)):
        for j in range(p.shape[0]):
            alpha[t, j] = alpha[t - 1].dot(p[:, j]) * b[j, obs[t] - 1]
    return alpha


np.random.seed(200476024)
num_states = 4
num_objects = 3
S = (1, 2, 3, 4)
V = (1, 2, 3)
initial_distribution = np.array((1, 0, 0, 0))

one_step_transition_matrix = generate_p_matrix(num_states)
event_matrix = generate_b_matrix(4, 3)

num_observations = 1000
observations = []
states = []
states.append(1)

while len(observations) < num_observations:
    observations.append(current_observation(event_matrix, states[-1]))
    states.append(next_state(one_step_transition_matrix, states[-1]))

states = states[:-1]

seq_obs = [1, 2, 3, 3, 1, 2, 3, 3, 1, 2, 3, 3]
X = [[obs] for obs in LabelEncoder().fit_transform(observations)]
X_test = [[obs] for obs in LabelEncoder().fit_transform(seq_obs)]
seq_prob = forward(one_step_transition_matrix, event_matrix, initial_distribution, seq_obs)
print(f'Probability that the sequence {seq_obs} came from the HMM: {sum(seq_prob[-1])}')

flag = False
for i in range(len(observations) - 12):
    if seq_obs == observations[i:i + 12]:
        flag = True
        print('The sequence exists in the generated observation')
if not flag:
    print('The sequence does not occur in the generated observation')
