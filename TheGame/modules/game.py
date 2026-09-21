import pyglet
from pyglet.window import key
from pyglet.window import mouse

from modules.game_state import GameState
from modules.game_assets import GameAssets

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

    # Store objects in a batch to load them efficiently
    main_batch = pyglet.graphics.Batch()

    # groups - 0 drawn first, 10 drawn last
    groups = []
    for i in range(10):
        # groups.append(pyglet.graphics.OrderedGroup(i))  # used in older version
        groups.append(pyglet.graphics.Group(i))


    # load required assets
    assets = GameAssets()

    # background music score
    background_music = assets.sound_assets["snd_default_bkg"]

    p = pyglet.media.Player()
    p.queue(background_music)
    p.loop = True
    p.play()

    # list of all interactive objects in the simulation
    game_objects = []

    # list of health bar objects
    health_bars = []

    # spawners
    # card_spawner = CardSpawner(assets, game_state, main_batch, groups[5])

    # score
    score_label = None
    score = 0

    # change mouse cursor
    cursor = window.get_system_mouse_cursor(window.CURSOR_HAND)
    window.set_mouse_cursor(cursor)

    def window_to_world(x, y):
        return (
            x + game_state.viewport_x - game_state.viewport_width // 2,
            y + game_state.viewport_y - game_state.viewport_height // 2,
        )

    def world_to_window(x, y):
        return (
            x - game_state.viewport_x + game_state.viewport_width // 2,
            y - game_state.viewport_y + game_state.viewport_height // 2,
        )

    # drawing items on screen
    @window.event
    def on_draw():
        window.clear()
        main_batch.draw()


    # handle mouse inputs
    @window.event
    def on_mouse_press(x, y, button, modifiers):
        # Note: x and y are in window coordinate frame
        # convert to world coordinate frame
        x, y = window_to_world(x, y)
        if button == mouse.LEFT:
            for obj in game_objects:
                # if obj.type == "player":
                #     obj.fire_bullet(x, y)
                pass
    
    # update loop
    def update(dt):
        pass

    pyglet.clock.schedule_interval(update, 1 / 120.0)
    pyglet.app.run()