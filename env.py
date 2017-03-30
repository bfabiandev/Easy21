import numpy as np


def get_card(black=False):
    n = np.random.randint(1, 11)
    if black:
        return n
    else:
        if np.random.randint(0, 3) == 0:
            return -n
        else:
            return n


def step(dealer, player, action):
    if action == 0:
        player += get_card()
        if player > 21 or player < 0:
            reward = -1
            return dealer, player, reward
        else:
            return dealer, player, None
    elif action == 1:
        while 0 <= dealer <= 21 and not dealer >= 17:
            dealer += get_card()
        if dealer < 1 or dealer > 21:
            return dealer, player, 1
        elif dealer > player:
            return dealer, player, -1
        elif dealer == player:
            return dealer, player, 0
        elif dealer < player:
            return dealer, player, 1
