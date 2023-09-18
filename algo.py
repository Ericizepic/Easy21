from environment import Easy21 
from agent import MC_Agent
from itertools import product
from mpl_toolkits.mplot3d import Axes3D  
import matplotlib.pyplot as plt
from array import array
import numpy as np

if __name__ == '__main__':
    player = MC_Agent()
    for k in range(1,10000000):
        game = Easy21()
        player.state_history = []
        s, r = game.get_state_and_reward()

        while (not game.game_over):
            action = player.epsilon_greedy_action(s)
            player.save_interval(s, action)
            s, r = game.step(action)

        player.learn(r)

    states = list(product(range(1,22), range(1,11)))
    pi = [[0 for i in range(10)] for j in range(21)]
    for s in states:
        if (player.Q[(s, 'hit')] > player.Q[(s, 'stick')]):
            pi[s[0]-1][s[1]-1] = 1 + player.Q[(s, 'hit')]
        elif (player.Q[(s, 'hit')] < player.Q[(s, 'stick')]):
            pi[s[0]-1][s[1]-1] = -1 - player.Q[(s, 'stick')]                                                                                                                                                                                                                                                                                                                                                             
        else:
            pi[s[0]-1][s[1]-1] = 0
    
    plt.imshow(pi, cmap='RdBu', vmin=-2, vmax=2)
    plt.colorbar()
    plt.show()

    x = np.array(list(map(lambda s: s[0], states)))
    y = np.array(list(map(lambda s: s[1], states)))
    z = np.array(list(map(lambda s: max(player.Q[(s, 'hit')], player.Q[(s, 'stick')]), states)))

    fig = plt.figure(figsize=(8,8))
    ax = plt.axes(projection='3d')
    surf1 = ax.plot_trisurf(x, y, z, antialiased=True)

    plt.show()





