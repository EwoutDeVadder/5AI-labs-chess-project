import chess

from fiveaichess.agents.agent import Agent


class UCIEngine():
    
    def __init__(self, agent: Agent) -> None:
        self.agent = agent
        
    def run(self):
        board = chess.Board()

        # continuously receive commands and process them
        while True:
            input_val = input().split(' ')

            match input_val:

                case ['uci']:
                    self.__uci()

                case ['isready']:
                    print('readyok')

                case ['ucinewgame']:
                    board = chess.Board()

                case ['position', 'startpos']:
                    board = chess.Board()
                
                case ['position', 'startpos', 'moves', *moves]:
                    board = chess.Board()
                    for move in moves:
                        board.push_uci(move)

                case ['go', *args]:
                    it = iter(args)
                    known_keys = {'wtime', 'btime', 'winc', 'binc', 'movestogo', 'depth', 'nodes', 'mate', 'movetime'}
                    constraints = {key: int(next(it)) for key in it if key in known_keys}
                    print(f'bestmove {self.agent.calculate_move(board, constraints)}')

                case ['quit']:
                    break


                    
    def __uci(self):
        print(f'id name {self.agent.name}')
        print(f'id author {self.agent.author}')
        print('uciok')