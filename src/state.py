
from enum import Enum

class state(object):
    
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
    
    