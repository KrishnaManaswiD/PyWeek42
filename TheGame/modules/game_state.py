class GameState(object):
    """
    Class to store the current state of the game
    """

    def __init__(self) -> None:

        # viewport size - this is the size of the window that we see
        self.viewport_width = 1600
        self.viewport_height = 800

        # these are the meters when the game starts
        self.health = 100
        self.money = 50
        self.mood = 30
        self.skill = 10

        self.level = 0
        self.level_change = False

        self.game_over = False
        self.game_won = False

