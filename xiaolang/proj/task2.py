from comprpg_classes import Player, Game
from ast import literal_eval
from typing import Union


def load_comprpg_game(filename: str) -> Union[Game, None]:
    with open(filename, 'r') as file:
        players = []
        history = []
        lines = file.readlines()
        if lines[0].strip() != "comprpg save file":
            return None
        turn = int(lines[2].split(":")[1].strip())
        player1 = lines[4:36]
        player2 = lines[37:69]
        player1_id = int(player1[0].split(":")[1].strip())
        player1_money = int(player1[1].split(":")[1].strip())
        player1_electricity = int(player1[2].split(":")[1].strip())
        player1_n_active = int(player1[3].split(":")[1].strip())
        player1_active = literal_eval(player1[4].split(":")[1].strip())
        player1_item = literal_eval(player1[5].split("items: ")[1])
        player1_characters = []
        characters = player1[7:]
        dic = {
            "name": "",
            "health": 0,
            "defence": 0,
            "effects": [],
            "defeated": False
        }
        for i in range(len(characters)):
            key = characters[i].strip().split(": ", 1)[0].strip()
            value = characters[i].strip().split(": ", 1)[1].strip()
            try:
                dic[key] = literal_eval(value)
            except:
                dic[key] = value
            if i in [4, 9, 14, 19, 24]:
                player1_characters.append(dic)
                dic = {
                    "name": "",
                    "health": 0,
                    "defence": 0,
                    "effects": [],
                    "defeated": False
                }
        player11 = Player(
            player1_id,
            player1_characters,
            player1_money,
            player1_electricity,
            player1_active,
            player1_item,
            player1_n_active)
        player2_id = int(player2[0].split(":")[1].strip())
        player2_money = int(player2[1].split(":")[1].strip())
        player2_electricity = int(player2[2].split(":")[1].strip())
        player2_n_active = int(player2[3].split(":")[1].strip())
        player2_active = literal_eval(player2[4].split(":")[1].strip())
        player2_item = literal_eval(player2[5].split("items: ")[1])
        player2_characters = []
        characters = player2[7:]
        dic = {
            "name": "",
            "health": 0,
            "defence": 0,
            "effects": [],
            "defeated": False
        }
        for i in range(len(characters)):
            key = characters[i].strip().split(": ", 1)[0].strip()
            value = characters[i].strip().split(": ", 1)[1].strip()
            try:
                dic[key] = literal_eval(value)
            except:
                dic[key] = value
            if i in [4, 9, 14, 19, 24]:
                player2_characters.append(dic)
                dic = {
                    "name": "",
                    "health": 0,
                    "defence": 0,
                    "effects": [],
                    "defeated": False
                }
        player22 = Player(
            player2_id,
            player2_characters,
            player2_money,
            player2_electricity,
            player2_active,
            player2_item,
            player2_n_active)
        players.append(player11)
        players.append(player22)
        histories = lines[71:]
        for i in range(len(histories)):
            history.append(literal_eval(histories[i].strip()))

        # Create Game object
        game = Game(players, turn, history)

        return game


game = load_comprpg_game('example_game_2.txt')
print(game)

Game([
    Player(
        0,
        [{'name': 'Python Pal', 'health': 19, 'defence': 0, 'effects': [], 'defeated': False},
         {'name': 'C Charmer', 'health': 20, 'defence': 0, 'effects': [], 'defeated': False},
         {'name': 'HTML Hero', 'health': 19, 'defence': 0, 'effects': [], 'defeated': False},
         {'name': 'Java Judger', 'health': 15, 'defence': 0, 'effects': [], 'defeated': False},
         {'name': 'Binary Bot', 'health': 7, 'defence': 0, 'effects': [], 'defeated': False}],
        8,
        29,
        ['HTML Hero', 'Python Pal'],
        [{'name': 'Backup Battery', 'description': 'Recharges 10 electricity', 'electricity': 10, 'price': 20},
         {'name': 'RAM Boost', 'description': 'Increases damage by 2 when attacking. Lasts 3 turns.', 'damage': 2,
          'turns': 3, 'price': 10}],
        2),
    Player(
        1,
        [{'name': 'Network Ninja', 'health': 16, 'defence': 0, 'effects': [], 'defeated': False},
         {'name': 'Python Pal', 'health': 22, 'defence': 0, 'effects': [], 'defeated': False},
         {'name': 'Binary Bot', 'health': 20, 'defence': 0, 'effects': [], 'defeated': False},
         {'name': 'HTML Hero', 'health': 11, 'defence': 0, 'effects': [{'damage': 2, 'turns': 2}], 'defeated': False},
         {'name': 'Haskell Heroine', 'health': 18, 'defence': 0, 'effects': [], 'defeated': False}],
        12,
        20,
        ['HTML Hero', 'Binary Bot'],
        [],
        2)],
    10,
    [[('Java Judger', 'swap', 'HTML Hero')], [('Binary Bot', 'attack', 'Keyboard Bash', 2, 1, 0, ['HTML Hero']),
                                              ('Network Ninja', 'item', 'Screen Repair Kit')],
     [('HTML Hero', 'attack', 'JavaScript Jab', 1, 1, 0, ['Network Ninja']), ('C Charmer', 'swap', 'Binary Bot')],
     [('Binary Bot', 'defend', 'Firewall', 2, 0),
      ('Network Ninja', 'attack', 'Code Injection', 10, 1, 15, ['Binary Bot'])],
     [('HTML Hero', 'defend', 'Firewall', 2, 0), ('Binary Bot', 'attack', 'Binary Blast', 5, 1, 5, ['Network Ninja'])],
     [('Binary Bot', 'swap', 'HTML Hero')],
     [('HTML Hero', 'attack', 'CSS Crusade', 3, 1, 2, ['HTML Hero']), ('Binary Bot', 'swap', 'Python Pal')],
     [('HTML Hero', 'attack', 'JavaScript Jab', 1, 1, 0, ['HTML Hero']), ('Network Ninja', 'swap', 'Haskell Heroine')],
     [('HTML Hero', 'item', 'Reboot in Safe Mode'), ('Python Pal', 'defend', 'Duck Type Dodge', 1, 0)],
     [('HTML Hero', 'attack', 'CSS Crusade', 3, 1, 2, ['HTML Hero']), ('Haskell Heroine', 'swap', 'Network Ninja')],
     [('HTML Hero', 'swap', 'Binary Bot')], [('HTML Hero', 'attack', 'JavaScript Jab', 1, 1, 0, ['Python Pal']),
                                             ('Network Ninja', 'defend', 'VPN Tunnel', 5, 5)],
     [('Binary Bot', 'attack', 'Binary Blast', 5, 1, 5, ['HTML Hero']),
      ('Python Pal', 'attack', 'Indentation Impact', 3, 1, 2, ['Network Ninja'])],
     [('HTML Hero', 'attack', 'CSS Crusade', 3, 1, 2, ['Binary Bot']), ('Network Ninja', 'swap', 'Binary Bot')],
     [('Binary Bot', 'swap', 'HTML Hero')], [('HTML Hero', 'attack', 'CSS Crusade', 3, 1, 2, ['HTML Hero']), (
        'Binary Bot', 'attack', 'Assembly Attack', 2, 2, 1, ['HTML Hero', 'Python Pal'])],
     [('HTML Hero', 'attack', 'CSS Crusade', 3, 1, 2, ['HTML Hero']),
      ('Python Pal', 'attack', 'Indentation Impact', 3, 1, 2, ['HTML Hero'])],
     [('HTML Hero', 'item', 'RAM Boost'), ('Binary Bot', 'defend', 'Firewall', 2, 0)]])

Game([
    Player(0,
           [
               {'name': 'Hardware Hacker', 'health': 25, 'defence': 0, 'effects': [], 'defeated': False},
               {'name': 'Python Pal', 'health': 1, 'defence': 0, 'effects': [{'damage': 2, 'turns': 1}],
                'defeated': False},
               {'name': 'C Charmer', 'health': 20, 'defence': 0, 'effects': [], 'defeated': False},
               {'name': 'Linux Legend', 'health': 20, 'defence': 0, 'effects': [], 'defeated': False},
               {'name': 'HTML Hero', 'health': 16, 'defence': 0, 'effects': [], 'defeated': False}],
           22,
           55,
           ['Python Pal', 'HTML Hero'],
           [],
           2),
    Player(
        1,
        [
            {'name': 'Haskell Heroine', 'health': 18, 'defence': 0, 'effects': [], 'defeated': False},
            {'name': 'HTML Hero', 'health': 25, 'defence': 0, 'effects': [], 'defeated': False},
            {'name': 'Binary Bot', 'health': 20, 'defence': 0, 'effects': [], 'defeated': False},
            {'name': 'Hardware Hacker', 'health': 25, 'defence': 0, 'effects': [], 'defeated': False},
            {'name': 'Network Ninja', 'health': 6, 'defence': 2, 'effects': [], 'defeated': False}],
        25,
        9,
        ['Network Ninja', 'Haskell Heroine'],
        [],
        2)],
    5,
    [[('Hardware Hacker', 'swap', 'Linux Legend')],
     [('Network Ninja', 'defend', 'VPN Tunnel', 5, 5), ('Hardware Hacker', 'swap', 'HTML Hero')],
     [('Linux Legend', 'swap', 'Python Pal')],
     [('Network Ninja', 'attack', 'Packet Sniffer', 1, 2, 0, ['HTML Hero', 'Python Pal']),
      ('HTML Hero', 'swap', 'Haskell Heroine')],
     [('Python Pal', 'item', 'RAM Boost'), ('HTML Hero', 'attack', 'CSS Crusade', 3, 1, 2, ['Network Ninja'])],
     [('Network Ninja', 'attack', 'Code Injection', 10, 1, 15, ['Python Pal']),
      ('Haskell Heroine', 'attack', 'Monadic Might', 5, 1, 2, ['HTML Hero'])],
     [('Python Pal', 'attack', 'Syntax Strike', 4, 1, 3, ['Network Ninja']), ('HTML Hero', 'item', 'Backup Battery')],
     [('Network Ninja', 'attack', 'Code Injection', 10, 1, 15, ['Python Pal']),
      ('Haskell Heroine', 'attack', 'Lambda Lunge', 3, 1, 0, ['HTML Hero'])]])
