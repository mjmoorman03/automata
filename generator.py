import numpy as np

GRID_WIDTH = 191
GRID_HEIGHT = 85

BOX_SIZE = 7

# we let the three boxes above be represented by integers according to which are filled (binary)

rules = {
    (0, 0, 0): 0,
    (0, 0, 1): 1,
    (0, 1, 0): 1,
    (0, 1, 1): 0,
    (1, 0, 0): 1,
    (1, 0, 1): 1,
    (1, 1, 0): 0,
    (1, 1, 1): 1
    }



class Board:
    def __init__(self, height, width):
        self.height = height 
        self.width = width
        self.state = self._generate_initial_state()
        self.stable = False
        self.iterations = 0


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
        # note that we only require previous line for new line
        if self.stable:
            return
    
        # get the state of the three boxes above
        for j in range(self.width):
            box2 = self.state[self.iterations][j]
            box1 = self.state[self.iterations][j-1] if j > 0 else 0
            box3 = self.state[self.iterations][j+1] if j < GRID_WIDTH - 1 else 0
            ruleInput = (box1, box2, box3)
            self.state[self.iterations+1][j] = rules[ruleInput]

        if self.iterations == self.height - 2:
            self.stable = True
            return

        self.iterations += 1


    def step(self, steps=1):
        for _ in range(steps):
            self._next_state()
        return self.state
        