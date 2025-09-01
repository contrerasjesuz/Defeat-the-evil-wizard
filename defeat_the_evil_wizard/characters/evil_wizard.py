from .base import Character
from ui import slow_print


class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15)
        self.min_damage = 12
        self.max_damage = 18

    def regenerate(self):
        # Wizard heals for 5 each turn, capped at max_health
        old_health = self.health
        self.health = min(self.max_health, self.health + 5)
        restored = self.health - old_health
        if restored > 0:
            slow_print(
                f"{self.name} regenerates {restored} health! "
                f"(Health: {self.health}/{self.max_health})"
            )
        else:
            slow_print(f"{self.name} is already at full health!")
