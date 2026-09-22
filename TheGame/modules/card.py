from dataclasses import dataclass

from pyglet.window import key, mouse

from modules.game_object import GameObject


@dataclass(frozen=True)
class MeterEffect:
    meter: str
    amount: int


class Card(GameObject):
    def __init__(self, game_assets, game_state, *args, **kwargs):
        self.default_sprite = game_assets.image_assets["img_card_blank"]
        super(Card, self).__init__(img=self.default_sprite, *args, **kwargs)

        self.assets = game_assets
        self.game_state = game_state
        self.type = "card"

        self.name: str = "Blank"
        # for now, a card has a single success effec and failure effect
        self.success_effect: MeterEffect = None
        self.success_chance: float = 0.0
        self.failure_effect: MeterEffect = None
        self.time_cost: int = 0

        # Tell the game handler about any event handlers
        self.key_handler = key.KeyStateHandler()
        self.mouse_handler = mouse.MouseStateHandler()
        self.event_handlers = [self, self.key_handler, self.mouse_handler]
        
