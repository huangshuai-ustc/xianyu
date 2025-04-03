from comprpg_data import all_characters, all_items
from comprpg_classes import Player, Game


def validate_comprpg_actions(game, actions, player_id):
    player = game.players[player_id]
    active_characters = player.active_characters
    electricity_available = player.electricity
    money = player.money
    for action in actions:
        if action[1] not in ['attack', 'defend', 'item', 'swap']:
            return False
        if action[1] == 'attack':
            if len(action) != 7:
                return False
            else:
                character_name, action_type, move_name, damage, num_targets, electricity_cost, target_list = action
                character = next((char for char in all_characters if char['name'] == character_name), None)
                if not character:
                    return False
                attack_move = next((move for move in character['attack_moves'] if move['name'] == move_name), None)
                if not attack_move:
                    return False
                if attack_move['damage'] != damage or attack_move['target'] != num_targets or attack_move['cost'] != electricity_cost:
                    return False
                if electricity_cost > electricity_available:
                    return False
                opponent_active_characters = [char for char in game.players[1 - player_id].active_characters]
                if len(target_list) != num_targets or not all(target in opponent_active_characters for target in target_list):
                    return False
        elif action[1] == 'defend':
            if len(action) != 5:
                return False
            else:
                character_name, action_type, move_name, protect_value, electricity_cost = action
                character = next((char for char in all_characters if char['name'] == character_name), None)
                if not character:
                    return False
                defend_move = next((move for move in character['defend_moves'] if move['name'] == move_name), None)
                if not defend_move:
                    return False
                if defend_move['protect'] != protect_value or defend_move['cost'] != electricity_cost:
                    return False
                if electricity_cost > electricity_available:
                    return False
        elif action[1] == 'item':
            if len(action) != 4:
                return False
            else:
                character_name, action_type, item_name, electricity_cost = action
                item = next((itm for itm in all_items if itm['name'] == item_name), None)
                if not item:
                    return False
                if electricity_cost > electricity_available:
                    return False
        elif action[1] == 'swap':
            if len(action) != 3:
                return False
            else:
                character_name, action_type, character_in_name = action
                if character_in_name not in [char['name'] for char in player.characters]:
                    return False
                if character_in_name == character_name:
                    return False

    return True


game = Game(
    [
        Player(
            0,
            [
                {'name': 'Java Judger', 'health': 14, 'defence': 0, 'effects': [], 'defeated': False},
                {'name': 'Python Pal', 'health': 0, 'defence': 0, 'effects': [], 'defeated': True},
                {'name': 'Haskell Heroine', 'health': 13, 'defence': 0, 'effects': [], 'defeated': False},
                {'name': 'Binary Bot', 'health': 20, 'defence': 0, 'effects': [], 'defeated': False},
                {'name': 'HTML Hero', 'health': 11, 'defence': 0, 'effects': [], 'defeated': False}],
            17,
            17,
            ['Java Judger'],
            [],
            1),
        Player(
            1,
            [
                {'name': 'Python Pal', 'health': 22, 'defence': 0, 'effects': [], 'defeated': False},
                {'name': 'C Charmer', 'health': 13, 'defence': 0, 'effects': [], 'defeated': False},
                {'name': 'Linux Legend', 'health': 4, 'defence': 0, 'effects': [], 'defeated': False},
                {'name': 'Binary Bot', 'health': 12, 'defence': 0, 'effects': [], 'defeated': False},
                {'name': 'Network Ninja', 'health': 0, 'defence': 0, 'effects': [], 'defeated': True}],
            11,
            1,
            ['Python Pal'],
            [],
            1)],
    38,
    [
        [('Haskell Heroine', 'defend', 'Recursion Rebuff', 2, 0), ('Python Pal', 'item', 'Screen Repair Kit')],
        [('Linux Legend', 'attack', 'Root Reckoning', 4, 2, 5, ['Haskell Heroine', 'Python Pal']),
         ('Binary Bot', 'item', 'Debugging Tool')],
        [('Haskell Heroine', 'attack', 'Lambda Lunge', 3, 1, 0, ['Linux Legend']), ('Python Pal', 'item', 'RAM Boost')],
        [('Linux Legend', 'attack', 'Kernel Kick', 4, 1, 3, ['Python Pal']), ('Binary Bot', 'swap', 'Network Ninja')],
        [('Haskell Heroine', 'swap', 'Java Judger')],
        [('Linux Legend', 'defend', 'Firewall', 2, 0), ('Network Ninja', 'attack', 'DDoS', 3, 1, 1, ['Python Pal'])],
        [('Java Judger', 'swap', 'HTML Hero')],
        [('Linux Legend', 'defend', 'Firewall', 2, 0), ('Network Ninja', 'attack', 'DDoS', 3, 1, 1, ['HTML Hero'])],
        [('HTML Hero', 'attack', 'CSS Crusade', 3, 1, 2, ['Linux Legend']),
         ('Python Pal', 'attack', 'Indentation Impact', 3, 1, 2, ['Network Ninja'])],
        [('Linux Legend', 'defend', 'Firewall', 2, 0), ('Network Ninja', 'attack', 'DDoS', 3, 1, 1, ['Python Pal'])],
        [('HTML Hero', 'attack', 'Entity Eruption', 2, 2, 2, ['Linux Legend', 'Network Ninja']),
         ('Python Pal', 'swap', 'Java Judger')],
        [('Linux Legend', 'defend', 'Firewall', 2, 0),
         ('Network Ninja', 'attack', 'Packet Sniffer', 1, 2, 0, ['HTML Hero', 'Java Judger'])],
        [('HTML Hero', 'attack', 'Entity Eruption', 2, 2, 2, ['Linux Legend', 'Network Ninja']),
         ('Java Judger', 'swap', 'Binary Bot')],
        [('Linux Legend', 'swap', 'Python Pal')],
        [('HTML Hero', 'attack', 'CSS Crusade', 3, 1, 2, ['Network Ninja']), ('Binary Bot', 'swap', 'Python Pal')],
        [('Python Pal', 'defend', 'Try-except Tactics', 5, 3),
         ('Network Ninja', 'attack', 'Code Injection', 10, 1, 15, ['Python Pal'])],
        [('HTML Hero', 'swap', 'Java Judger')],
        [('Python Pal', 'attack', 'Syntax Strike', 4, 1, 3, ['Python Pal']), ('Network Ninja', 'swap', 'C Charmer')],
        [('Java Judger', 'swap', 'Haskell Heroine')],
        [('Python Pal', 'defend', 'Try-except Tactics', 5, 3),
         ('C Charmer', 'attack', 'Pointer Pinch', 1, 2, 0, ['Haskell Heroine', 'Python Pal'])],
        [('Haskell Heroine', 'swap', 'HTML Hero')],
        [('Python Pal', 'attack', 'Syntax Strike', 4, 1, 3, ['HTML Hero']), ('C Charmer', 'swap', 'Linux Legend')],
        [('HTML Hero', 'defend', 'Firewall', 2, 0), ('Python Pal', 'defend', 'Duck Type Dodge', 1, 0)],
        [('Python Pal', 'swap', 'Binary Bot')], [('HTML Hero', 'swap', 'Haskell Heroine')],
        [('Binary Bot', 'attack', 'Binary Blast', 5, 1, 5, ['Python Pal']), ('Linux Legend', 'swap', 'Network Ninja')],
        [('Haskell Heroine', 'attack', 'Monadic Might', 5, 1, 2, ['Network Ninja'])],
        [('Binary Bot', 'defend', 'Firewall', 2, 0)],
        [('Haskell Heroine', 'defend', 'Recursion Rebuff', 2, 0)],
        [('Binary Bot', 'defend', 'Firewall', 2, 0)],
        [('Haskell Heroine', 'swap', 'Java Judger')],
        [('Binary Bot', 'swap', 'Linux Legend')],
        [('Java Judger', 'swap', 'Binary Bot')],
        [('Linux Legend', 'swap', 'Binary Bot')],
        [('Binary Bot', 'swap', 'Haskell Heroine')],
        [('Binary Bot', 'swap', 'Linux Legend')],
        [('Haskell Heroine', 'swap', 'HTML Hero')],
        [('Linux Legend', 'attack', 'Kernel Kick', 4, 1, 3, ['HTML Hero'])],
        [('HTML Hero', 'attack', 'CSS Crusade', 3, 1, 2, ['Linux Legend'])],
        [('Linux Legend', 'swap', 'C Charmer')],
        [('HTML Hero', 'defend', 'Firewall', 2, 0)],
        [('C Charmer', 'swap', 'Binary Bot')],
        [('HTML Hero', 'attack', 'CSS Crusade', 3, 1, 2, ['Binary Bot'])],
        [('Binary Bot', 'swap', 'C Charmer')],
        [('HTML Hero', 'attack', 'CSS Crusade', 3, 1, 2, ['C Charmer'])],
        [('C Charmer', 'swap', 'Binary Bot')],
        [('HTML Hero', 'attack', 'CSS Crusade', 3, 1, 2, ['Binary Bot'])],
        [('Binary Bot', 'swap', 'C Charmer')],
        [('HTML Hero', 'attack', 'JavaScript Jab', 1, 1, 0, ['C Charmer'])],
        [('C Charmer', 'swap', 'Linux Legend')],
        [('HTML Hero', 'defend', 'Firewall', 2, 0)],
        [('Linux Legend', 'swap', 'C Charmer')],
        [('HTML Hero', 'attack', 'CSS Crusade', 3, 1, 2, ['C Charmer'])],
        [('C Charmer', 'swap', 'Binary Bot')],
        [('HTML Hero', 'attack', 'JavaScript Jab', 1, 1, 0, ['Binary Bot'])],
        [('Binary Bot', 'swap', 'C Charmer')],
        [('HTML Hero', 'defend', 'Websafe Wand', 5, 5)],
        [('C Charmer', 'swap', 'Linux Legend')],
        [('HTML Hero', 'attack', 'CSS Crusade', 3, 1, 2, ['Linux Legend'])],
        [('Linux Legend', 'swap', 'Binary Bot')],
        [('HTML Hero', 'attack', 'JavaScript Jab', 1, 1, 0, ['Binary Bot'])],
        [('Binary Bot', 'swap', 'Linux Legend')],
        [('HTML Hero', 'swap', 'Java Judger')],
        [('Linux Legend', 'swap', 'C Charmer')],
        [('Java Judger', 'swap', 'HTML Hero')],
        [('C Charmer', 'swap', 'Linux Legend')],
        [('HTML Hero', 'defend', 'Firewall', 2, 0)],
        [('Linux Legend', 'attack', 'Bash Bonk', 2, 1, 0, ['HTML Hero'])],
        [('HTML Hero', 'defend', 'Firewall', 2, 0)],
        [('Linux Legend', 'swap', 'Binary Bot')],
        [('HTML Hero', 'defend', 'Firewall', 2, 0)],
        [('Binary Bot', 'swap', 'Linux Legend')],
        [('HTML Hero', 'swap', 'Java Judger')],
        [('Linux Legend', 'swap', 'Python Pal')]])
actions = [('Java Judger', 'swap', 'HTML Hero')]
player_id = 0
print(validate_comprpg_actions(game, actions, player_id))  # Expected output: True
actions = [('HTML Hero', 'swap', 'HTML Hero')]
print(validate_comprpg_actions(game, actions, player_id))
actions = [('Java Judger', 'attack', 'Object Oriented Obliteration', 6, 1, 6, ['Python Pal'])]
print(validate_comprpg_actions(game, actions, player_id))
