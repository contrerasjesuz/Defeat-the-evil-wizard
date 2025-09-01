import random
from ui import slow_print


class AttackResolver:
    # static method makes it so i don't have to call the object to use it
    @staticmethod
    def resolve_attack(attacker, defender):
        """Rolls dice for attacker and defender to see if attack hits.
        Returns (hit: bool, damage: int, critical: bool)
        """
        attack_roll = random.randint(1, 20)
        defense_roll = random.randint(1, 20)

        slow_print(f"{attacker.name} rolls {attack_roll} to attack!")
        slow_print(f"{defender.name} rolls {defense_roll} to defend!")

        # Critical hit check
        if attack_roll == 20:
            damage = int(attacker.attack_power * 1.5)
            slow_print("Critical hit!")
            return True, damage, True

        # Normal hit check
        if attack_roll > defense_roll:
            # Normal attack (can still use attacker’s damage range if you want)
            damage = random.randint(
                getattr(attacker, "min_damage", attacker.attack_power),
                getattr(attacker, "max_damage", attacker.attack_power),
            )
            return True, damage, False

        # Missed attack
        slow_print(f"{attacker.name}'s attack misses!")
        return False, 0, False
        # returns tuple to make modular and reusable for use and also expandable for "future features"

    # special ability resolver
    @staticmethod
    def resolve_special(attacker, defender, base_min, base_max, crit_multiplier=1.5):
        """Special ability: same roll-off + crit rules, but caller supplies damage range."""
        attack_roll = random.randint(1, 20)
        defense_roll = random.randint(1, 20)

        slow_print(f"{attacker.name} rolls {attack_roll} to use a special!")
        slow_print(f"{defender.name} rolls {defense_roll} to defend!")

        if attack_roll == 20:
            dmg = random.randint(base_min, base_max)
            dmg = int(dmg * crit_multiplier)
            slow_print("Critical special!")
            return True, dmg, True

        if attack_roll > defense_roll:
            dmg = random.randint(base_min, base_max)
            return True, dmg, False

        slow_print(f"{attacker.name}'s special fails!")
        return False, 0, False
