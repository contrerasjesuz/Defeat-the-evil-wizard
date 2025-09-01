from characters import Warrior, Mage, EvilWizard, Archer, Paladin
from ui import slow_print


def create_character():
    slow_print("Choose your character class:")
    slow_print("1. Warrior")
    slow_print("2. Mage")
    slow_print("3. Archer")
    slow_print("4. Paladin")

    class_choice = input("Enter the number of your class choice: ")
    name = input("Enter your character's name: ")

    if class_choice == "1":
        return Warrior(name)
    elif class_choice == "2":
        return Mage(name)
    elif class_choice == "3":
        return Archer(name)
    elif class_choice == "4":
        return Paladin(name)
    else:
        slow_print("Invalid choice. Defaulting to Warrior.")
        return Warrior(name)


def battle(player, wizard):
    while wizard.health > 0 and player.health > 0:
        slow_print("\n--- Your Turn ---")
        slow_print("1. Attack")
        slow_print("2. Use Special Ability")
        slow_print("3. Heal")
        slow_print("4. View Stats")

        choice = input("Choose an action: ")

        if choice == "1":
            player.attack(wizard)
        elif choice == "2":
            player.special(wizard)
        elif choice == "3":
            player.heal()
        elif choice == "4":
            player.display_stats()
            continue
        else:
            slow_print("Invalid choice. Try again.")
            continue

        if wizard.health > 0:
            wizard.regenerate()
            wizard.attack(player)

        if player.health <= 0:
            slow_print(f"{player.name} has been defeated!")
            break

    if wizard.health <= 0:
        slow_print(f"The wizard {wizard.name} has been defeated by {player.name}!")
