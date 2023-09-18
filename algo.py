from env import Easy21 
from agent import MCAgent
from itertools import product
import matplotlib.pyplot as plt

if __name__ == '__main__':
    player = MCAgent()
    rewards = []
    for k in range(1,1000000):
        game = Easy21()
        player.state_history = []
        s, r = game.get_state_and_reward()

        while (not game.game_over):
            action = player.epsilon_greedy_action(s, k)
            player.save_interval(s, action)
            s, r = game.step(action)

        player.learn(r)
        rewards.append(r)

    states = list(product(range(1,22), range(1,11)))

    for st in states:
        if (player.Q[(st, 'hit')] > player.Q[(st, 'stick')]):
            print(st, player.visit_count[(st, 'hit')] + player.visit_count[(st, 'stick')], 'hit', player.Q[(st, 'hit')], player.Q[(st, 'stick')])
        elif (player.Q[(st, 'hit')] < player.Q[(st, 'stick')]):
            print(st, player.visit_count[(st, 'hit')] + player.visit_count[(st, 'stick')], 'stick', player.Q[(st, 'hit')], player.Q[(st, 'stick')])
        else:
            print(st, player.visit_count[(st, 'hit')] + player.visit_count[(st, 'stick')], 'tie', player.Q[(st, 'hit')], player.Q[(st, 'stick')])
    print("\n")

    # for st in states:
    #     print(st, player.visit_count[(st, 'hit')] + player.visit_count[(st, 'stick')], sep=" ")
    
    # plt.plot(rewards)
    # plt.show()



