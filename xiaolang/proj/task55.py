from comprpg_classes import Game, Player
from comprpg_data import all_characters, all_items


def get_character_by_name(characters, name):
    """通过角色的名字返回角色字典"""
    for char in characters:
        if char['name'] == name:
            return char
    return None


def play_comprpg(player, turn, active_opponents, history):
    if turn == 0:
        # first turn choose active characters and items
        active_characters = []
        for char in player.characters:
            if len(active_characters) < 2 and not char['defeated']:
                active_characters.append(char['name'])

        # chose item we can get with money
        chosen_items = []
        remaining_money = player.money
        for item in all_items:
            if item['price'] <= remaining_money:
                chosen_items.append(item['name'])
                remaining_money -= item['price']

        return [(player.active_characters[0], "item", chosen_items[0])]

    else:
        # not first turn choose actions
        actions = []
        for char_name in player.active_characters:
            char = get_character_by_name(player.characters, char_name)
            if char and not char['defeated']:
                character = next((char for char in all_characters if char['name'] == char_name), None)
                # if enough electricity attack, else defend
                action = None
                if player.electricity > 0:
                    # attack active character[0]
                    target = active_opponents[0]
                    attack = character['attack_moves'][1]['name']
                    damage = character['attack_moves'][1]['damage']
                    tar = character['attack_moves'][1]['target']
                    cost = character['attack_moves'][1]['cost']
                    action = (char_name, 'attack', attack, damage, tar, cost, [target])
                else:
                    # defend if electricity is not enough
                    defend = character['defend_moves'][0]['name']
                    protect = character['defend_moves'][0]['protect']
                    cost = character['defend_moves'][0]['cost']
                    action = (char_name, 'defend', defend, protect, cost)
                actions.append(action)
        return actions

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

# 之前的game对象和player对象
player = game.players[0]  # 假设玩家0
active_opponents = game.players[1].active_characters  # 对手的活跃角色
history = game.history
# 测试函数：初始回合
turn = 0
print(play_comprpg(player, turn, active_opponents, history))

# 测试函数：非初始回合
turn = 1
print(play_comprpg(player, turn, active_opponents, history))
