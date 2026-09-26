import pyglet
from pyglet.window import key
from pyglet.window import mouse
from pyglet import shapes

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


    # spawners
    # card_spawner = CardSpawner(assets, game_state, main_batch, groups[5])

    # meters
    health_label = None
    money_label = None
    mood_label = None
    skill_label = None
    time_label = None

    # change mouse cursor
    cursor = window.get_system_mouse_cursor(window.CURSOR_HAND)
    window.set_mouse_cursor(cursor)


    # drawing items on screen
    @window.event
    def on_draw():
        window.clear()
        main_batch.draw()


    # handle mouse inputs
    @window.event
    def on_mouse_press(x, y, button, modifiers):
        if button == mouse.LEFT:
            pass

    # load the main stage
    def load_stage_1():
        pass

    # TODO: why doesnt this not show up?
    def draw_health_bar():
        print("Drawing health bar...")
        health_bar_width = 200
        health_bar_height = 50
        health_bar_color = (55, 55, 255, 255)

        health = game_state.health
        health_percentage = max(0, min(1, health / 100))
        health_bar_width = int(health_bar_width * health_percentage)

        health_bar = shapes.Rectangle(
            x= 100,
            y= 100,
            width=health_bar_width,
            height=health_bar_height,
            color=health_bar_color,
            batch=main_batch,
            group=groups[9]
        )

    # TODO: change these to numbers and meters
    def update_meters():
        nonlocal health_label, money_label, mood_label, skill_label

        health_label = pyglet.text.Label(
            "Health: " + str(game_state.health),
            font_name="Arial",
            font_size=20,
            x=10,
            y=game_state.viewport_height - 10,
            anchor_x="left",
            anchor_y="top",
            batch=main_batch,
            group=groups[9],
        )

        money_label = pyglet.text.Label(
            "Money: " + str(game_state.money),
            font_name="Arial",
            font_size=20,
            x=10,
            y=game_state.viewport_height - 40,
            anchor_x="left",
            anchor_y="top",
            batch=main_batch,
            group=groups[9],
        )

        mood_label = pyglet.text.Label(
            "Mood: " + str(game_state.mood),
            font_name="Arial",
            font_size=20,
            x=10,
            y=game_state.viewport_height - 70,
            anchor_x="left",
            anchor_y="top",
            batch=main_batch,
            group=groups[9],
        )

        skill_label = pyglet.text.Label(
            "Skill: " + str(game_state.skill),
            font_name="Arial",
            font_size=20,
            x=10,
            y=game_state.viewport_height - 100,
            anchor_x="left",
            anchor_y="top",
            batch=main_batch,
            group=groups[9],
        )
        

    def update_timer():
        nonlocal time_label
        
        time_label = pyglet.text.Label(
            "Time: " + str(game_state.time_remaining),
            font_name="Arial",
            font_size=20,
            x=game_state.viewport_width - 10,
            y=game_state.viewport_height - 10,
            anchor_x="right",
            anchor_y="top",
            batch=main_batch,
            group=groups[9],
        )


    # TODO: handle transitions between levels
    def handle_level_change():
        pass
    
    # update loop
    def update(dt):
        handle_level_change()
        # draw_health_bar()
        update_timer()
        update_meters()

        

    pyglet.clock.schedule_interval(update, 1 / 120.0)
    pyglet.app.run()