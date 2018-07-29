# Char RNN model of Andrej Karpathy functionized 
# https://gist.githubusercontent.com/karpathy/d4dee566867f8291f086/raw/119a6930b670bced5800b6b03ec4b8cb6b8ff4ec/min-char-rnn.py

import numpy as np

def lossFun(inputs, targets, hprev):
    """
    inputs,targets are both list of integers.
    hprev is Hx1 array of initial hidden state
    returns the loss, gradients on model parameters, and last hidden state
    """
    xs, hs, ys, ps = {}, {}, {}, {}
    hs[-1] = np.copy(hprev)
    loss = 0
    # forward pass
    for t in range(len(inputs)):
        xs[t] = np.zeros((vocab_size, 1))  # encode in 1-of-k representation
        xs[t][inputs[t]] = 1
        hs[t] = np.tanh(np.dot(Wxh, xs[t]) +
                        np.dot(Whh, hs[t-1]) + bh)  # hidden state
        # unnormalized log probabilities for next chars
        ys[t] = np.dot(Why, hs[t]) + by
        # probabilities for next chars
        ps[t] = np.exp(ys[t]) / np.sum(np.exp(ys[t]))
        loss += -np.log(ps[t][targets[t], 0])  # softmax (cross-entropy loss)
    # backward pass: compute gradients going backwards
    dWxh, dWhh, dWhy = np.zeros_like(
        Wxh), np.zeros_like(Whh), np.zeros_like(Why)
    dbh, dby = np.zeros_like(bh), np.zeros_like(by)
    dhnext = np.zeros_like(hs[0])
    for t in reversed(range(len(inputs))):
        dy = np.copy(ps[t])
        # backprop into y. see http://cs231n.github.io/neural-networks-case-study/#grad if confused here
        dy[targets[t]] -= 1
        dWhy += np.dot(dy, hs[t].T)
        dby += dy
        dh = np.dot(Why.T, dy) + dhnext  # backprop into h
        dhraw = (1 - hs[t] * hs[t]) * dh  # backprop through tanh nonlinearity
        dbh += dhraw
        dWxh += np.dot(dhraw, xs[t].T)
        dWhh += np.dot(dhraw, hs[t-1].T)
        dhnext = np.dot(Whh.T, dhraw)
    for dparam in [dWxh, dWhh, dWhy, dbh, dby]:
        # clip to mitigate exploding gradients
        np.clip(dparam, -5, 5, out=dparam)
    return loss, dWxh, dWhh, dWhy, dbh, dby, hs[len(inputs)-1]


def sample(h, seed_ix, n):
    """ 
    sample a sequence of integers from the model 
    h is memory state, seed_ix is seed letter for first time step
    """
    x = np.zeros((vocab_size, 1))
    x[seed_ix] = 1
    ixes = []
    for t in range(n):
        h = np.tanh(np.dot(Wxh, x) + np.dot(Whh, h) + bh)
        y = np.dot(Why, h) + by
        p = np.exp(y) / np.sum(np.exp(y))
        # ix = np.random.choice(range(vocab_size), p=p.ravel())
        ix = p.argmax()
        x = np.zeros((vocab_size, 1))
        x[ix] = 1
        ixes.append(ix)
    return ixes

# model parameters

def model(hidden_size, vocab_size):
    Wxh = np.random.randn(hidden_size, vocab_size)*0.01  # input to hidden
    Whh = np.random.randn(hidden_size, hidden_size)*0.01  # hidden to hidden
    Why = np.random.randn(vocab_size, hidden_size)*0.01  # hidden to output
    bh = np.zeros((hidden_size, 1))  # hidden bias
    by = np.zeros((vocab_size, 1))  # output bias
    return Wxh, Whh, Why, bh, by

# data I/O

def read_data(data):
    chars = list(set(data))
    data_size, vocab_size = len(data), len(chars)
    print('data has {} characters, {} unique.'.format(data_size, vocab_size))
    char_to_ix = {ch: i for i, ch in enumerate(chars)}
    ix_to_char = {i: ch for i, ch in enumerate(chars)}
    return data_size, vocab_size, char_to_ix, ix_to_char


if __name__ == "__main__":
    # hyperparameters
    hidden_size = 100  # size of hidden layer of neurons
    seq_length = 25  # number of steps to unroll the RNN for
    learning_rate = 1e-1
    n, p = 0, 0

    data_size, vocab_size, char_to_ix, ix_to_char = read_data(data)
    Wxh, Whh, Why, bh, by = model(hidden_size, vocab_size)
    mWxh, mWhh, mWhy = np.zeros_like(
        Wxh), np.zeros_like(Whh), np.zeros_like(Why)
    mbh, mby = np.zeros_like(bh), np.zeros_like(
        by)  # memory variables for Adagrad
    smooth_loss = -np.log(1.0/vocab_size)*seq_length  # loss at iteration 0

    # foe plotting the loss-iteration graph
    loss_list = {}
    while n < 500000:
        # prepare inputs (we're sweeping from left to right in steps seq_length long)
        if p+seq_length+1 >= data_size or n == 0:
            hprev = np.zeros((hidden_size, 1))  # reset RNN memory
            p = 0  # go from start of data
        inputs = [char_to_ix[ch] for ch in data[p:p+seq_length]]
        targets = [char_to_ix[ch] for ch in data[p+1:p+seq_length+1]]

        # sample from the model now and then
        if n % 10000 == 0:
            sample_ix = sample(hprev, inputs[0], 200)
            txt = ''.join(ix_to_char[ix] for ix in sample_ix)
            print('----\n {} \n----'.format(txt))

        # forward seq_length characters through the net and fetch gradient
        loss, dWxh, dWhh, dWhy, dbh, dby, hprev = lossFun(
            inputs, targets, hprev)
        smooth_loss = smooth_loss * 0.999 + loss * 0.001
        if n % 10000 == 0:
            print('iter {}, loss: {}'.format(n, smooth_loss))  # print progress

        if n % 1000 == 0:
            loss_list[n] = smooth_loss
        # perform parameter update wit h Adagrad
        for param, dparam, mem in zip([Wxh, Whh, Why, bh, by], [dWxh, dWhh, dWhy, dbh, dby], [mWxh, mWhh, mWhy, mbh, mby]):
            mem += dparam * dparam
            param += -learning_rate * dparam / \
                np.sqrt(mem + 1e-8)  # adagrad update

        p += seq_length  # move data pointer
        n += 1  # iteration counter
