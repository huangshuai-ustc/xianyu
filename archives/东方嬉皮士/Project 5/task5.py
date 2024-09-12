import numpy as np
from hmmlearn import hmm
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


def viterbi(p, b, pi, obs):
    len_obs = len(obs)
    m = p.shape[0]
    omega = np.zeros((len_obs, m))
    omega[0, :] = np.log(pi * b[:, obs[0] - 1])
    prev = np.zeros((len_obs - 1, m))
    for t in range(1, len_obs):
        for j in range(m):
            probability = omega[t - 1] + np.log(p[:, j]) + np.log(b[j, obs[t] - 1])
            prev[t - 1, j] = np.argmax(probability)
            omega[t, j] = np.max(probability)

    s = np.zeros(len_obs)
    last_state = np.argmax(omega[len_obs - 1, :])
    s[0] = last_state
    backtrack_index = 1
    for _ in range(len_obs - 2, -1, -1):
        s[backtrack_index] = prev[_, int(last_state)]
        last_state = prev[_, int(last_state)]
        backtrack_index += 1
    ss = np.flip(s, axis=0)
    result = []
    for s in ss:
        result.append(int(s + 1))
    return result


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


hmm_model = hmm.CategoricalHMM(n_components=num_states, random_state=10, n_iter=100)
hmm_model.fit(X)
transmission_matrix = hmm_model.transmat_
print('Transmision matrix')
print(transmission_matrix)
print(f'Testing for normalization on p matrix: {np.sum(transmission_matrix, axis=1)}')
emission_prob = hmm_model.emissionprob_
print('Emission probability')
print(emission_prob)
print(f'Testing for normalization on b matrix: {np.sum(emission_prob, axis=1)}')
initial_distribution = hmm_model.startprob_
print('Initial distribution')
print(initial_distribution)
print(f'Testing for normalization on initialization matrix: {np.sum(transmission_matrix, axis=1)}')
