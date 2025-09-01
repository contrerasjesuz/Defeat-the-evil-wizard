from .base import Character
from combat import AttackResolver
from ui import slow_print


class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)
        self.min_damage = 30
        self.max_damage = 40

    def special(self, opponent):
        # Fireball: high damage; small recoil on a successful hit
        hit, dmg, crit = AttackResolver.resolve_special(
            self, opponent, base_min=40, base_max=50, crit_multiplier=1.5
        )
        if hit:
            opponent.health -= dmg
            slow_print(f"{self.name} casts Fireball for {dmg} damage!")
            self.health -= 5
            slow_print(
                f"{self.name} takes 5 recoil damage (now {self.health}/{self.max_health})."
            )
            if opponent.health <= 0:
                slow_print(f"{opponent.name} has been defeated!")
