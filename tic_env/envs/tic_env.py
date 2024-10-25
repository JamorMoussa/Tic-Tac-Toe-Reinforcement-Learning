from  ..tic_game import TicTacToeGame, Player, State, PlayerId, BoardState


import gymnasium as gym 
import numpy as np


class TicTacToeEnv(gym.Env):

    metadata = {'render_modes': ['human']}

    def __init__(self):
        super(TicTacToeEnv, self).__init__()

        self.game = TicTacToeGame()

        self.action_space = gym.spaces.Discrete(start=1, n=9)
        self.observation_space = gym.spaces.Discrete(start=0, n=2**9-1)

    def sample_action(self):

        allowed_actions = self.game.get_allowed_actions()
        return np.random.choice(
            a= allowed_actions, p= [1/len(allowed_actions)]*len(allowed_actions)
        )
 

    def reset(self, seed=None, options=None):
        super().reset(seed=seed)
        
        self.game.reset()

        return self.game.board_state.get_state().get()
    

    def step(self, action: int):

        self.game.cur_player.move(action=action)
        self.game.change_player()

        reward = self.game.get_reward()

        obv = self.game.board_state.get_state().get()

        terminated = self.game.is_done()

        return obv, reward, terminated, {}

    def render(self):
        self.game.render()