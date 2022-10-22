from constants import *
from game.scripting.action import Action


class ControlRacketAction(Action):

    def __init__(self, keyboard_service):
        self._keyboard_service = keyboard_service
        
    def execute(self, cast, script, callback):
        rackets = []
        rackets = cast.get_actors(RACKET_GROUP)
        for i, racket in enumerate(rackets):
            if i == 0:
                if self._keyboard_service.is_key_down('z'): 
                    racket.move_up()
                elif self._keyboard_service.is_key_down('x'): 
                    racket.move_down()  
                else: 
                    racket.stop_moving()
            else:
                if self._keyboard_service.is_key_down('n'): 
                    racket.move_up()
                elif self._keyboard_service.is_key_down('m'): 
                    racket.move_down()  
                else: 
                    racket.stop_moving()
