import pyglet

from modules.game_state import GameState

def run():
    # print(pyglet.version)

    game_state = GameState()

    # create the game window
    window = pyglet.window.Window(
        width=game_state.viewport_width,
        height=game_state.viewport_height,
        caption="PyWeek42",
        resizable=False,
    )





    pyglet.app.run()