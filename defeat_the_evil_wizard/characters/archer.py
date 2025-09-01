from .base import Character
from combat import AttackResolver
from ui import slow_print


class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=110, attack_power=22)
        self.min_damage = 18
        self.max_damage = 28

    def special(self, opponent):
        # Multi-Shot: two arrows, each with its own roll (can crit/miss independently)
        total = 0
        for i in range(2):
            hit, dmg, crit = AttackResolver.resolve_special(
                self, opponent, base_min=12, base_max=20, crit_multiplier=1.5
            )
            if hit:
                opponent.health -= dmg
                total += dmg
                slow_print(f"Arrow {i+1} hits for {dmg}{' (CRIT)' if crit else ''}!")
                if opponent.health <= 0:
                    slow_print(f"{opponent.name} has been defeated!")
                    break
            else:
                slow_print(f"Arrow {i+1} misses.")
        slow_print(f"{self.name} uses Multi-Shot for a total of {total} damage!")
