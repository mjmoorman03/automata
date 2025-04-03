import numpy as np

GRID_WIDTH = 1001
GRID_HEIGHT = 1000

# we let the three boxes above be represented by integers according to which are filled (binary)

rules = {
    0: 0,
    1: 1,
    2: 1,
    3: 0,
    4: 1,
    5: 0,
    6: 1,
    7: 0
    }



class Board:
    def __init__(self, height, width):
        self.height = height 
        self.width = width
        self.state = self._generate_initial_state()


    def getState(self):
        return self.state


    def _generate_initial_state(self):
        # one single box in the first row
        initial_state = np.zeros((self.height, self.width), dtype=int)
        initial_state[0][self.width // 2] = 1
        return initial_state
    

    def _next_state(self):
        # state is a numpy array of GRID_WIDTH x GRID_HEIGHT
        # we will use the rules to determine the next state
        new_state = self.state.copy()
        for i in range(1, self.height):
            for j in range(self.width):
                # get the state of the three boxes above
                box1 = self.state[i-1][j]
                box2 = self.state[i-1][j-1] if j > 0 else 0
                box3 = self.state[i-1][j+1] if j < GRID_WIDTH - 1 else 0
                ruleInput = (box1 << 2) | (box2 << 1) | box3
                new_state[i][j] = rules[ruleInput]
        self.state = new_state