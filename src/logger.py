# noinspection PyPep8
banner = """
=============================================================================================================
d8888b. db    db d8b   db  .d8b.  .88b  d88. d888888b  .o88b.      d8b   db d888888b  .o88b. db   dD .d8888. 
88  `8D `8b  d8' 888o  88 d8' `8b 88'YbdP`88   `88'   d8P  Y8      888o  88   `88'   d8P  Y8 88 ,8P' 88'  YP 
88   88  `8bd8'  88V8o 88 88ooo88 88  88  88    88    8P           88V8o 88    88    8P      88,8P   `8bo.   
88   88    88    88 V8o88 88~~~88 88  88  88    88    8b           88 V8o88    88    8b      88`8b     `Y8b. 
88  .8D    88    88  V888 88   88 88  88  88   .88.   Y8b  d8      88  V888   .88.   Y8b  d8 88 `88. db   8D 
Y8888D'    YP    VP   V8P YP   YP YP  YP  YP Y888888P  `Y88P'      VP   V8P Y888888P  `Y88P' YP   YD `8888Y'                                                                                                              
=============================================================================================================
"""


class Logger:
    @staticmethod
    def banner():
        print(banner)

    @staticmethod
    def emoji_parsing():
        print('Parsing emoji sequence...')

    @staticmethod
    def tg_client_initiating():
        print('Initiating telegram client...')

    @staticmethod
    def nickname_generator_initiating():
        print('Initiating nickname generator...')

    @classmethod
    def nickname(cls, nickname):
        # noinspection PyPep8
        print(f'Nickname changing... ({nickname})')