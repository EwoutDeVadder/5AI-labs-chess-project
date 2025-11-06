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
        # print('option name Debug Log File type string default')
        # print('option name Contempt type spin default 0 min -100 max 100')
        # print('option name Threads type spin default 1 min 1 max 128')
        # print('option name Hash type spin default 16 min 1 max 1048576')
        # print('option name Clear Hash type button')
        # print('option name Ponder type check default false')
        # print('option name MultiPV type spin default 1 min 1 max 500')
        # print('option name Skill Level type spin default 20 min 0 max 20')
        # print('option name Move Overhead type spin default 30 min 0 max 5000')
        # print('option name Minimum Thinking Time type spin default 20 min 0 max 5000')
        # print('option name Slow Mover type spin default 89 min 10 max 1000')
        # print('option name nodestime type spin default 0 min 0 max 10000')
        # print('option name UCI_Chess960 type check default false')
        # print('option name SyzygyPath type string default <empty>')
        # print('option name SyzygyProbeDepth type spin default 1 min 1 max 100')
        # print('option name Syzygy50MoveRule type check default true')
        # print('option name SyzygyProbeLimit type spin default 6 min 0 max 6')
        print('uciok')