
from sample_players import DataPlayer
import random
import math

class CustomPlayer(DataPlayer):
    """ Implement your own agent to play knight's Isolation

    The get_action() method is the only required method for this project.
    You can modify the interface for get_action by adding named parameters
    with default values, but the function MUST remain compatible with the
    default interface.

    **********************************************************************
    NOTES:
    - The test cases will NOT be run on a machine with GPU access, nor be
      suitable for using any other machine learning techniques.

    - You can pass state forward to your agent on the next turn by assigning
      any pickleable object to the self.context attribute.
    **********************************************************************
    """
    def pvs_min_max(self,state,depth,alpha,beta,color):
        if depth <=0 or state.terminal_test():
            return color*self.score(state)
        explored = []
        
        for a in state.actions():
            if a not in explored:
                explored.append(a)
                score = self.pvs_min_max(state.result(a),depth-1,alpha,beta,-color)
                #score = -score
            else:
                score = self.pvs_min_max(state.result(a),depth-1,alpha,alpha+1,-color)
               # score = -score
                if alpha<score and beta>score:
                    score = self.pvs_min_max(state.result(a),depth-1,alpha,beta,-color)
                    #score = -score
            if alpha<score:
                alpha = score
            if alpha>=beta:
                break
        return alpha
    def pvt(self,state,depth):
        alpha = -math.inf
        beta = math.inf
        actions = state.actions()
        if actions:
            best_move = actions[0]
        else:
            best_move = None
        maximizingplayer = 1
        v = -math.inf
        for i, action in enumerate(actions):
            new_state = state.result(action)
            if i==0:
                v = max(v,self.pvs_min_max(new_state,depth-1,alpha,beta,maximizingplayer))
            else:
                v = max(v,self.pvs_min_max(new_state,depth-1,alpha,alpha+1,maximizingplayer))
                if v>alpha:
                    v = max(v,self.pvs_min_max(new_state,depth-1,alpha,beta,maximizingplayer))
            if v>alpha:
                alpha=v
                best_move=action
        return best_move
    def score(self, state):
        own_loc = state.locs[self.player_id]
        opp_loc = state.locs[1 - self.player_id]
        own_liberties = state.liberties(own_loc)
        opp_liberties = state.liberties(opp_loc)
        return len(own_liberties) - len(opp_liberties)     
    def get_action(self, state):
        """ Employ an adversarial search technique to choose an action
        available in the current state calls self.queue.put(ACTION) at least

        This method must call self.queue.put(ACTION) at least once, and may
        call it as many times as you want; the caller will be responsible
        for cutting off the function after the search time limit has expired.

        See RandomPlayer and GreedyPlayer in sample_players for more examples.

        **********************************************************************
        NOTE: 
        - The caller is responsible for cutting off search, so calling
          get_action() from your own code will create an infinite loop!
          Refer to (and use!) the Isolation.play() function to run games.
        **********************************************************************
        """
        # TODO: Replace the example implementation below with your own search
        #       method by combining techniques from lecture
        #
        # EXAMPLE: choose a random move without any search--this function MUST
        #          call self.queue.put(ACTION) at least once before time expires
        #          (the timer is automatically managed for you)
        
        
        if state.ply_count < 2:
            self.queue.put(random.choice(state.actions()))
        else:
            
            a = self.pvt(state,3)
                
            self.queue.put(a)
        
        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        