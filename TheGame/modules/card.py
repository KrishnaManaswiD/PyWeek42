from dataclasses import dataclass

@dataclass(frozen=True)
class MeterEffect:
    meter: str
    amount: int


@dataclass(frozen=True)
class Card:
    name: str = "Blank"
    success_effect: MeterEffect = None
    success_chance: float = 0.0
    failure_effect: MeterEffect = None
    time_cost: int = 0
    # for now, a card has a single success effec and failure effect

    def __post_init__(self):
        if not 0 <= self.success_chance <= 1:
            raise ValueError("increase_chance must be between 0 and 1")
