from combat import AttackResolver
from ui import slow_print


class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health
        # Default damage range for basic attacks; subclasses can override.
        self.min_damage = attack_power
        self.max_damage = attack_power

    def attack(self, opponent):
        success, damage, crit = AttackResolver.resolve_attack(self, opponent)
        if success:
            opponent.health -= damage
            slow_print(f"{self.name} hits {opponent.name} for {damage} damage!")
            if opponent.health <= 0:
                slow_print(f"{opponent.name} has been defeated!")

    def heal(self, amount=20):
        # Restore health but never above max_health.
        old_health = self.health
        self.health = min(self.max_health, self.health + amount)
        restored = self.health - old_health
        if restored > 0:
            slow_print(
                f"{self.name} heals for {restored} HP! "
                f"(Health: {self.health}/{self.max_health})"
            )
        else:
            slow_print(f"{self.name} is already at full health!")

    def display_stats(self):
        slow_print(
            f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}"
        )

    # Subclasses override this to call AttackResolver.resolve_special()
    def special(self, opponent):
        slow_print(f"{self.name} doesn't have a special move yet.")
