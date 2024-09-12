<h1 align='center'>Project 5 - Machine Learning Algorithms</h1>

Using dataset same as Project 2

## Task 1. Configuration of Neural Networks  

### 1.1 & 1.2 Re-run multiple regression model  in Project 3

Do same things of project 3 except dataset size.

For this project, there are 2000 samples need to fit.

### 1.3 Discuss results

The result of multiple regression model for 2000 samples is
$$
y = 0.175x_1+0.034x_2-0.007x_3-0.872x_4+1.191x_5
$$
Its p-value, $r^2$, adjust $r^2$分别为:  3.255e-228, 0.955,0.955, which is a very fitting model about dataset.

## Task 2. Generation of Parameter Sets for HMM 

The one-step transition matrix and testing normalization for p-matrix which the code generate by using random seed `200476024` show in following pictures. 

![image-20240426135145689](https://raw.githubusercontent.com/huangshuai-ustc/images/main/pic/image-20240426135145689.png)

![image-20240426135416751](https://raw.githubusercontent.com/huangshuai-ustc/images/main/pic/image-20240426135416751.png)

From the p matrix results we can make the following conclusions:

1. When in state 1, the highest state probability is that the next state is state 2. The low probability that it remains in the same state.

2. When in state 2, the next most probable state is 1. Staying in the same state 2 is lowly probable.

3. The most probable next state when in state 3 is state 2. This time, there is low probability that the state remains the same.

4. When in state 4, the most probable next state is state 2. The probability that is remains in the same state.

The most probable next states are 2.

All the rows add-up to 1. Indicating that the probabilities are normalized.

The event matrix  and normalization for b-matrix  which the code generate by using seed student ID number: `200476024` show in following pictures. 

![image-20240426135759274](https://raw.githubusercontent.com/huangshuai-ustc/images/main/pic/image-20240426135759274.png)

![image-20240426135913071](https://raw.githubusercontent.com/huangshuai-ustc/images/main/pic/image-20240426135913071.png)

1. If in state 1, the most probable observation is V = 1

2. If in state 2, the most probable observation is V = 2

3. If in state 3, the most probable observation is V = 1

4. If in state 4, the most probable observation is V = 2

## Task 3: Estimate p(O|λ) for HMM.  

Using the following code to calculate the probability that a given observation came from a given HMM model.  

```python
seq_obs = [1, 2, 3, 3, 1, 2, 3, 3, 1, 2, 3, 3]
X = [[obs] for obs in LabelEncoder().fit_transform(observations)]
X_test = [[obs] for obs in LabelEncoder().fit_transform(seq_obs)]
seq_prob = forward(one_step_transition_matrix, event_matrix, initial_distribution, seq_obs)
```

![image-20240426140731517](https://raw.githubusercontent.com/huangshuai-ustc/images/main/pic/image-20240426140731517.png)

The probability that the sequence 1,2,3,3,1,2,3,3,1,2,3,3 was generated from the given HMM is very low (1.7e-06), almost 0.  

As a sanity check,  checking if the given sequence ever occurred in the 1000 observations that we generated.  

```python
flag = False
for i in range(len(observations) - 12):
    if seq_obs == observations[i:i + 12]:
        flag = True
        print('The sequence exists in the generated observation')
if not flag:
    print('The sequence does not occur in the generated observation')
```

![image-20240426142144444](https://raw.githubusercontent.com/huangshuai-ustc/images/main/pic/image-20240426142144444.png)

The sequence does not appear in the observations that we generated. This justifies the very low probability that we get for the sequence.  

## Task 4: Estimate the Most probable Sequence Q.  

Using the Viterbi algorithm to generate the most probable state sequence for the given set of observation.  

![image-20240426142748206](https://raw.githubusercontent.com/huangshuai-ustc/images/main/pic/image-20240426142748206.png)

The initial distribution is (1,0,0,0) so it makes sense that the first state is 1. When in state 1, the next most probable state is 2, but code choose 4. When in state 4 the next most probable state is 2 and that is what we observe. When in state 2 it is highly likely that the next state is 1. This is what we observe as the next 1 states are 3. When in state 3, the most likely observation is 2. In state 2 the most likely observation is V = 2. Looking at the p and the b matrices we can see that the probable states sequence generated using Viterbi is correct.

## Task 5: Train the HMM  

Estimated parameters:

![image-20240426143724500](https://raw.githubusercontent.com/huangshuai-ustc/images/main/pic/image-20240426143724500.png)

![image-20240426143738855](https://raw.githubusercontent.com/huangshuai-ustc/images/main/pic/image-20240426143738855.png)

![image-20240426143749105](https://raw.githubusercontent.com/huangshuai-ustc/images/main/pic/image-20240426143749105.png)

The initial distribution is similar to the initial distribution that forwarding generation. 

The transmission matrix is different from the p-matrix that forwarding defined. It is more evenly distributed than the pre-defined p-matrix.

1. When in state 1, the highest state probability is that the next state is state 3. The probability of state1 is similar to state 3.
2. When in state 2, the next most probable state is again 1. Staying in state 2 is lowly probable.
3. The most probable next state when in state 3 is itself.
4. When in state 4, the most probable next state is state 4. Different from the pregenerated p-matirx. The emission matrix is also different from the b-matrix we generated in task 1.
5. If in state 1, the most probable observation is V = 1
6. If in state 2, the most probable observation is V = 1
7. If in state 3, the most probable observation is V = 2
8. If in state 4, the most probable observation is V = 1

V=1 and V=2 are the two most probable observations according to the estimated parameters.

The hmmlearn api does not provide us with the p-values. From the estimated parameters, we can conclude that the estimation may not be a good fit for the generated observations.



