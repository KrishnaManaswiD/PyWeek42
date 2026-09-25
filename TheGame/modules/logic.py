# a single file to test the logic before making it into Pyglet objects

from dataclasses import dataclass
import random

@dataclass(frozen=True)
class MeterEffect:
    meter: str
    amount: int

@dataclass
class Card():
    name: str = "Blank"
    success_effect: MeterEffect = None
    success_chance: float = 0.0
    failure_effect: MeterEffect = None
    time_cost: int = 0

deck = []
hand = []
table = []
health = 100
time = 30*24

def populate_deck():
    global deck
    for i in range(1,10):
        card = Card(
            name=f"Card {i}",
            success_effect=MeterEffect(meter="health", amount=10*(i)),
            success_chance=random.uniform(0.1, 0.9),
            failure_effect=MeterEffect(meter="health", amount=5*(i)),
            time_cost=random.randint(5, 10)
        )
        deck.append(card)


def shuffle_deck():
    global deck
    import random
    random.shuffle(deck)


def draw_card():
    global deck, hand
    if deck:
        card = deck.pop(0)
        hand.append(card)
    else:
        print("Deck is empty!")

def show_hand():
    global hand
    print("Current hand:")
    for card in hand:
        print(f"- {card.name} (Success: {card.success_chance*100}%, Time Cost: {card.time_cost}) success: {card.success_effect.meter}: {card.success_effect.amount}, failure: {card.failure_effect.meter}: {card.failure_effect.amount}")

def show_table():
    global table
    print("Cards on the table:")
    for card in table:
        print(f"- {card.name} (Success: {card.success_chance*100}%, Time Cost: {card.time_cost}) success: {card.success_effect.meter}: {card.success_effect.amount}, failure: {card.failure_effect.meter}: {card.failure_effect.amount}")

def play_card(card_index):
    global hand, table
    if 0 <= card_index < len(hand):
        card = hand.pop(card_index)
        table.append(card)
    else:
        print("Invalid card index!")

def clear_table():
    global table
    table.clear()


def apply_card_effects(card):
    import random
    if random.random() < card.success_chance:
        print(f"Card {card.name} succeeded! Applying success effect: {card.success_effect}")
        if card.success_effect:
            if card.success_effect.meter == "health":
                increase_health(card.success_effect.amount)
        # Here you would apply the success effect to the game state
    else:
        print(f"Card {card.name} failed! Applying failure effect: {card.failure_effect}")
        if card.failure_effect:
            if card.failure_effect.meter == "health":
                decrease_health(card.failure_effect.amount)
        # Here you would apply the failure effect to the game state
    decrease_time(card.time_cost)

def increase_health(amount):
    global health
    health += amount
    print(f"Health increased by {amount}. Current health: {health}")

def decrease_health(amount):
    global health
    health -= amount
    print(f"Health decreased by {amount}. Current health: {health}")

def decrease_time(amount):
    global time
    time -= amount
    print(f"Time decreased by {amount}. Current time: {time}")

def start_game():
    populate_deck()
    shuffle_deck()
    draw_card()
    draw_card()
    draw_card()
    show_hand()
    show_table()

def main():
    start_game()
    while health > 0 and time > 0:
        ask = input("choose a card to play (1, 2, 3): ")
        try:
            card_index = int(ask)-1
            play_card(card_index)
            show_hand()
            show_table()
            # Apply effects of the played card
            apply_card_effects(table[-1])  # Apply effects of the last played card
        except ValueError:
            print("Invalid input! Please enter a number.")
        except IndexError:
            print("Invalid card index! Please choose a valid card.")
        finally:
            clear_table()
            print(f"Final health: {health}")
            print(f"Final time: {time}")
            print()
            draw_card()
            show_hand()

if __name__ == "__main__":
    main()