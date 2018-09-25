
from enum import Enum



class State(object):
    
    state_id = 0
    next_state = 0
    
    class program_states(Enum):
        STATE_NULL = 0
        STATE_INIT = 1
        STATE_INTRO = 2
        STATE_MENU = 3
        STATE_GAME = 4
        STATE_EDIT = 5
        STATE_EXIT = 6
    
    def get_next_state(self):
        return self.next_state
    
    def set_next_state(self,new_state):
        
        self.next_state=new_state
        
    def get_state_id(self):
        
        return self.state_id
    
