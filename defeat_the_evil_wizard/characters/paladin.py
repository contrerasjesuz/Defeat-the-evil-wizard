from .base import Character
from combat import AttackResolver
from ui import slow_print


class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=20)
        self.min_damage = 16
        self.max_damage = 24

    def special(self, opponent):
        # Smite & Mend: solid hit + heal on successful hit
        hit, dmg, crit = AttackResolver.resolve_special(
            self, opponent, base_min=28, base_max=36, crit_multiplier=1.5
        )
        if hit:
            opponent.health -= dmg
            heal = 10
            self.health = min(self.max_health, self.health + heal)
            slow_print(f"{self.name} uses Smite for {dmg} damage and mends {heal} HP!")
            if opponent.health <= 0:
                slow_print(f"{opponent.name} has been defeated!")
