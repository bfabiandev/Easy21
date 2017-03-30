from env import *


def montecarlo(N, Q):
    N0 = 250.0

    states = []
    reward = None
    dealer = get_card(black=True)
    player = get_card(black=True)
    while reward is None:
        eps = N0 / (N0 + np.sum(N[dealer - 1, player, :]))
        if np.random.rand() < eps:
            action = np.random.randint(0, 2)
        else:
            action = np.argmax(Q[dealer - 1, player, :])
        states.append((dealer, player, action))
        dealer, player, reward = step(dealer, player, action)

    for state in states:
        dealer, player, action = state
        N[dealer - 1, player, action] += 1
        Q[dealer - 1, player, action] += 1.0 / N[dealer - 1, player, action] * (reward - Q[dealer - 1, player, action])

    return N, Q
