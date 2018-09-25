
from state import State

class Init(State):

    def draw(self):
        print("Nothign to draw here sir")
        
    def update(self):
        self.next_state=3