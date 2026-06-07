from random import randint
from typing import TypedDict

from graphic_arts.start_game_banner import run_screensaver


class Character(TypedDict):
    name: str
    class_: str
    stamina: int
    attack: int
    defence: int


def attack(character: Character) -> str:
    """Apply an attack action and update character stats."""
    char_name = character['name']
    char_class = character['class_']
    stamina = character['stamina']
    attack_power = character['attack']
    if char_class == 'warrior':
        stamina -= 5
        attack_power += 2
        character['stamina'] = stamina
        character['attack'] = attack_power
        if character['stamina'] <= 20:
            return (f'{char_name} dealt {3 + randint(3, 5)} '
                    'damage to the enemy')
        return (f'{char_name} dealt {character["attack"] + randint(3, 5)} '
                'damage to the enemy')
    elif char_class == 'mage':
        stamina -= 7
        attack_power += 1
        character['stamina'] = stamina
        character['attack'] = attack_power
        if character['stamina'] <= 20:
            return (f'{char_name} dealt {3 + randint(5, 10)} '
                    'damage to the enemy')
        return (f'{char_name} dealt {character["attack"] + randint(5, 10)} '
                'damage to the enemy')
    elif char_class == 'healer':
        stamina -= 2
        attack_power += 3
        character['stamina'] = stamina
        character['attack'] = attack_power
        if character['stamina'] <= 20:
            return (f'{char_name} dealt {3 + randint(-3, -1)} '
                    'damage to the enemy')
        return (f'{char_name} dealt {character["attack"] + randint(-3, -1)} '
                'damage to the enemy')
    else:
        return 'Unknown hero class'


def defence(character: Character) -> str:
    """Apply a defence action and update character stats."""
    char_name = character['name']
    char_class = character['class_']
    stamina = character['stamina']
    defence_power = character['defence']
    if char_class == 'warrior':
        stamina += 10
        defence_power += 10
        character['stamina'] = stamina
        character['defence'] = defence_power
        if character['stamina'] < 80:
            return (f'{char_name} blocked {2 + randint(5, 10)} damage')
        return (f'{char_name} blocked '
                f'{character["defence"] + randint(5, 10)} damage')
    elif char_class == 'mage':
        stamina += 15
        defence_power += 5
        character['stamina'] = stamina
        character['defence'] = defence_power
        if character['stamina'] < 80:
            return (f'{char_name} blocked {2 + randint(5, 10)} damage')
        return (f'{char_name} '
                f'blocked {character["defence"] + randint(-2, 2)} damage')
    elif char_class == 'healer':
        stamina += 5
        defence_power += 15
        character['stamina'] = stamina
        character['defence'] = defence_power
        if character['stamina'] < 80:
            return (f'{char_name} blocked {2 + randint(5, 10)} damage')
        return (f'{char_name} '
                f'blocked {character["defence"] + randint(2, 5)} damage')
    else:
        return 'Unknown hero class'


def special(character: Character) -> str:
    """Apply a special action and update character stats."""
    char_name = character['name']
    char_class = character['class_']
    stamina = character['stamina']
    defence_power = character['defence']
    attack_power = character['attack']
    if char_class == 'warrior':
        stamina += 25
        character['stamina'] = stamina
        return (f'{char_name} used the special skill '
                f'«Endurance {character["stamina"]}»')
    elif char_class == 'mage':
        attack_power += 40
        character['attack'] = attack_power
        return (f'{char_name} used the special skill '
                f'«Attack {character["attack"]}»')
    elif char_class == 'healer':
        defence_power += 30
        character['defence'] = defence_power
        return (f'{char_name} used the special skill '
                f'«Protection {character["defence"]}»')
    else:
        return ('Unknown hero class')


def start_training(character: Character) -> None:
    """Run the hero training session."""
    char_name = character['name']
    char_class = character['class_']
    if char_class == "warrior":
        print(f'{char_name}, you are a Warrior - a great melee fighter.')
    elif char_class == "mage":
        print(f'{char_name}, you are a Mage - '
              'an excellent tamer of the elements.')
    else:
        print(f'{char_name}, you are a Healer - a wizard who can heal wounds.')
    print('Practice using your skills.\n'
          'Enter one of the commands:\n'
          '1 — attack the enemy,\n'
          '2 — block the enemy\'s attack,\n'
          '3 — use your special skill.\n'
          '4 — view character stats\n'
          'Press 0 to stop training.')
    while True:
        cmd = input('Enter the command:\n')
        if cmd == '0':
            break
        elif cmd == '1':
            print(attack(character))
        elif cmd == '2':
            print(defence(character))
        elif cmd == '3':
            print(special(character))
        elif cmd == '4':
            show_character(character)
        else:
            print('Unknown command')


def choice_char_class() -> str:
    """Ask the user to choose a hero class."""
    approve_choice = None
    char_class = ''
    classes: dict[str, str] = {
        '1': "warrior",
        '2': "mage",
        '3': "healer",
    }
    class_descriptions: dict[str, str] = {
        'warrior': (
            "The Warrior is a daring melee warrior. "
            "He is strong, tough, and brave."
            ),
        'mage': (
            "The Mage is a resourceful ranged warrior. "
            "He has high intelligence."
            ),
        'healer': (
            "The Healer is a powerful caster. "
            "He draws strength from nature, faith, and spirits."
            ),
    }
    while approve_choice != 'y':
        user_choice = input('Choose the class you want to play:\n')
        if user_choice in classes:
            char_class = classes[user_choice]
            print(class_descriptions[char_class])
            approve_choice = input('Press (Y) to confirm your choice, '
                                   'or any other button to select another '
                                   'character.\n').lower()
        else:
            print("Unknown hero class")
    return char_class


def show_character(character: Character) -> None:
    '''Print the current character stats.'''
    stamina_ = character['stamina']
    defence_ = character['defence']
    attack_ = character['attack']
    print(f'stamina: {stamina_}\n'
          f'defence: {defence_}\n'
          f'attack: {attack_}')


def main() -> None:
    """Start the game, choose a class, and run the training session."""
    run_screensaver()
    print('Greetings, adventurer!\n'
          'Before you start the game, enter your name:')
    char_name = input()
    print(f'Hi, {char_name}!\n'
          'Your current stats are: stamina - 80, attack - 5, defence - 10\n'
          'You can choose one of the three paths of power:\n'
          'Warrior (1), Mage (2), or Healer (3)')
    char_class = choice_char_class()
    character: Character = {
        'name': char_name,
        'class_': char_class,
        'stamina': 80,
        'attack': 5,
        'defence': 10,
    }
    start_training(character)


if __name__ == '__main__':
    main()
