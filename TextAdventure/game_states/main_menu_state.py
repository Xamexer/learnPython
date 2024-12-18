from game_states.base_state import BaseState, BaseSubState
from dictionaries.state_enums import MainMenuSubState
from dictionaries.input import input

class MainMenuDefaultSubState(BaseSubState):
    def handle_input(self,key):
        pass

    def update(self):
        pass

    def render(self):
        pass

class MainMenuState(BaseState):
    def __init__(self, game):
        super().__init__(game, MainMenuSubState.DEFAULT)
        self.substates = {
            MainMenuSubState.DEFAULT: MainMenuDefaultSubState(game)
        }
