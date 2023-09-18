import random

class Easy21(object):
    # give each player their initial cards 
    def __init__(self):
        self.dealer_sum = random.randint(1, 10)
        self.player_sum = random.randint(1, 10)
        self.game_over = False

    # update each players sum
    def hit_player(self):
        new_card = random.randint(1, 10)
        self.player_sum += new_card if random.random() > 1/3 else -1 * new_card
    
    def hit_dealer(self):
        new_card = random.randint(1, 10)
        self.dealer_sum += new_card if random.random() > 1/3 else -1 * new_card

    def give_reward(self, do_compare):
        #first check if either player busts
        if (self.player_sum > 21 or self.player_sum < 1):
            self.game_over = True
            return -1

        if (self.dealer_sum > 21 or self.dealer_sum < 1):
            self.game_over = True
            return 1

        if (do_compare):
            self.game_over = True
            if (self.dealer_sum > self.player_sum):
                return -1
            elif (self.dealer_sum < self.player_sum):
                return 1
            else:
                return 0
        
        return 0
    
    def get_state_and_reward(self, do_compare = False):
        return (self.player_sum, self.dealer_sum), self.give_reward(do_compare)

    # takes as input a state s (dealer’s first card 1–10 and the player’s sum 1–21), and an action a (hit or stick), and returns
    # a sample of the next state s' (which may be terminal if the game is finished) and reward r
    def step(self, a):
        if a == 'hit':
            self.hit_player()
            return self.get_state_and_reward()
        else: 
            # dealer's turn to play
            while (self.dealer_sum < 17 and self.dealer_sum > 0):
                self.hit_dealer()
            return self.get_state_and_reward(True)

        
