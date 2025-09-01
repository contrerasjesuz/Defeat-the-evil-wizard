from .base import Character
from combat import AttackResolver
from ui import slow_print


class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)
        self.min_damage = 20
        self.max_damage = 30

    def special(self, opponent):
        # Power Strike: chunky single hit
        hit, dmg, crit = AttackResolver.resolve_special(
            self,
            opponent,
            base_min=int(self.attack_power * 1.2),
            base_max=int(self.attack_power * 1.6),
            crit_multiplier=1.5,
        )
        if hit:
            opponent.health -= dmg
            slow_print(f"{self.name} uses Power Strike for {dmg} damage!")
            if opponent.health <= 0:
                slow_print(f"{opponent.name} has been defeated!")
