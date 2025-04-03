# 1. Calculate Game Stats
import csv


def calculate_comprpg_stats(history, filename):
    # Initialize stats for player 0 and player 1
    player_stats = {
        0: {'attacks': 0, 'defends': 0, 'items': 0, 'swaps': 0,
            'attempted_damage': 0, 'attempted_protection': 0,
            'electricity_used': 0, 'turns': 0},
        1: {'attacks': 0, 'defends': 0, 'items': 0, 'swaps': 0,
            'attempted_damage': 0, 'attempted_protection': 0,
            'electricity_used': 0, 'turns': 0}
    }

    # process every piece of information of history
    for i, actions in enumerate(history):
        player = i % 2  # 0 for player 0, 1 for player 1
        # Each entry is a new turn for the player
        player_stats[player]['turns'] += 1

        for action in actions:
            if action[1] == 'attack':
                player_stats[player]['attacks'] += 1
                # Damage is in the 4th position
                player_stats[player]['attempted_damage'] += action[3]
                # Electricity is in the 6th position
                player_stats[player]['electricity_used'] += action[5]
            elif action[1] == 'defend':
                player_stats[player]['defends'] += 1
                # Protection is in the 4th position
                player_stats[player]['attempted_protection'] += action[3]
                # Electricity is in the 5th position
                player_stats[player]['electricity_used'] += action[4]
            elif action[1] == 'item':
                player_stats[player]['items'] += 1
            elif action[1] == 'swap':
                player_stats[player]['swaps'] += 1

    header = ['player', 'attacks', 'defends', 'items', 'swaps',
              'attempted damage', 'attempted protection',
              'electricity used', 'turns taken']
    rows = []
    print(player_stats)
    for player in [0, 1]:
        row = [player]
        row.extend(list(player_stats[player].values()))
        rows.append(row)

    # Write the stats to the CSV file
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(header)
        writer.writerows(rows)


# Example usage history = [[('Haskell Heroine', 'defend', 'Recursion Rebuff', 2, 0), ('Python Pal', 'item',
# 'Screen Repair Kit')], [('Linux Legend', 'attack', 'Root Reckoning', 4, 2, 5, ['Haskell Heroine', 'Python Pal']),
# ('Binary Bot', 'item', 'Debugging Tool')], [('Haskell Heroine', 'attack', 'Lambda Lunge', 3, 1, 0,
# ['Linux Legend']), ('Python Pal', 'item', 'RAM Boost')], [('Linux Legend', 'attack', 'Kernel Kick', 4, 1, 3,
# ['Python Pal']), ('Binary Bot', 'swap', 'Network Ninja')]]
history = [[('C Charmer', 'item', 'RAM Boost'), ('Binary Bot', 'swap', 'Linux Legend')],
           [('Hardware Hacker', 'swap', 'HTML Hero')],
           [('C Charmer', 'attack', 'Segfault Slam', 2, 2, 2, ['HTML Hero', 'Python Pal']),
            ('Linux Legend', 'attack', 'Bash Bonk', 2, 1, 0, ['HTML Hero'])],
           [('HTML Hero', 'attack', 'Entity Eruption', 2, 2, 2, ['C Charmer', 'Linux Legend']),
            ('Python Pal', 'attack', 'Syntax Strike', 4, 1, 3, ['Linux Legend'])],
           [('C Charmer', 'defend', 'Buffer Overflow Block', 7, 5), ('Linux Legend', 'defend', 'Firewall', 2, 0)],
           [('HTML Hero', 'swap', 'Haskell Heroine')], [('C Charmer', 'swap', 'Binary Bot')],
           [('Haskell Heroine', 'attack', 'Lambda Lunge', 3, 1, 0, ['Binary Bot']),
            ('Python Pal', 'swap', 'C Charmer')],
           [('Binary Bot', 'attack', 'Keyboard Bash', 2, 1, 0, ['C Charmer']),
            ('Linux Legend', 'attack', 'Root Reckoning', 4, 2, 5, ['C Charmer', 'Haskell Heroine'])],
           [('Haskell Heroine', 'attack', 'Monadic Might', 5, 1, 2, ['Linux Legend']),
            ('C Charmer', 'defend', 'Compiler Crash', 3, 0)]]

# Call the function to write to CSV

calculate_comprpg_stats(history, "game_stats.csv")

# Example 1: >>> history = [[('Haskell Heroine', 'defend', 'Recursion Rebuff', 2, 0), ('Python Pal', 'item',
# 'Screen Repair Kit')], [('Linux Legend', 'attack', 'Root Reckoning', 4, 2, 5, ['Haskell Heroine', 'Python Pal']),
# ('Binary Bot', 'item', 'Debugging Tool')], [('Haskell Heroine', 'attack', 'Lambda Lunge', 3, 1, 0,
# ['Linux Legend']), ('Python Pal', 'item', 'RAM Boost')], [('Linux Legend', 'attack', 'Kernel Kick', 4, 1, 3,
# ['Python Pal']), ('Binary Bot', 'swap', 'Network Ninja')]] >>> calculate_comprpg_stats(history,
# "example_game1_stats.csv") player,attacks,defends,items,swaps,attempted damage,attempted protection,electricity
# used,turns taken 0,1,1,2,0,3,2,0,2 1,2,0,1,1,8,0,8,2 Example 2: >>> history = [[('C Charmer', 'item', 'RAM Boost'),
# ('Binary Bot', 'swap', 'Linux Legend')], [('Hardware Hacker', 'swap', 'HTML Hero')], [('C Charmer', 'attack',
# 'Segfault Slam', 2, 2, 2, ['HTML Hero', 'Python Pal']), ('Linux Legend', 'attack', 'Bash Bonk', 2, 1, 0,
# ['HTML Hero'])], [('HTML Hero', 'attack', 'Entity Eruption', 2, 2, 2, ['C Charmer', 'Linux Legend']),
# ('Python Pal', 'attack', 'Syntax Strike', 4, 1, 3, ['Linux Legend'])], [('C Charmer', 'defend', 'Buffer Overflow
# Block', 7, 5), ('Linux Legend', 'defend', 'Firewall', 2, 0)], [('HTML Hero', 'swap', 'Haskell Heroine')],
# [('C Charmer', 'swap', 'Binary Bot')], [('Haskell Heroine', 'attack', 'Lambda Lunge', 3, 1, 0, ['Binary Bot']),
# ('Python Pal', 'swap', 'C Charmer')], [('Binary Bot', 'attack', 'Keyboard Bash', 2, 1, 0, ['C Charmer']),
# ('Linux Legend', 'attack', 'Root Reckoning', 4, 2, 5, ['C Charmer', 'Haskell Heroine'])], [('Haskell Heroine',
# 'attack', 'Monadic Might', 5, 1, 2, ['Linux Legend']), ('C Charmer', 'defend', 'Compiler Crash', 3,
# 0)]] >>> calculate_comprpg_stats(history, "example_game2_stats.csv")
#
# player,attacks,defends,items,swaps,attempted damage,attempted protection,electricity used,turns taken
# 0,4,2,1,2,10,9,12,5
# 1,4,1,0,3,14,3,7,5
